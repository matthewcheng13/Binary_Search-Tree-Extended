class Binary_Search_Tree:

    class __BST_Node:

        def __init__(self, value):
            self.value = value
            self.height = 1
            self.left_child = None
            self.right_child = None

    def __init__(self):
        self.__root = None

    def __set_height(self,node):
        # case of no children always has a height of 1
        if (node.left_child == None) and (node.right_child == None):
            return 1
        # if there is no left child, right's height + 1 must be used
        elif node.left_child == None:
            return node.right_child.height + 1
        # if there is no right child, left's height + 1 must be used
        elif node.right_child == None:
            return node.left_child.height + 1
        # either left child is taller or right child's height is greater than or equal to left child's height
        else:
            if node.left_child.height > node.right_child.height:
                return node.left_child.height + 1
            else:
                return node.right_child.height + 1
            
    def __get_node_height(self,node):
            if node == None:
                return 0
            else:
                return node.height
            
    def __rotation(self,t,right):
        # perform rotation on a right-leaning tree
        if right:
            new_t = t.right_child
            floater = new_t.left_child
            new_t.left_child = t
            t.right_child = floater
            t.height = self.__set_height(t)
            new_t.height = self.__set_height(new_t)
            return new_t
        # perform rotation on a left-leaning tree
        else:
            new_t = t.left_child
            floater = new_t.right_child
            new_t.right_child = t
            t.left_child = floater
            t.height = self.__set_height(t)
            new_t.height = self.__set_height(new_t)
            return new_t

    def __balance(self,t):
        # set the current balance
        balance = self.__get_node_height(t.right_child) - self.__get_node_height(t.left_child)
        # if unbalanced, perform the necessary rotations
        # then return the new root of the subtree
        if balance == 2:
            if self.__get_node_height(t.right_child.right_child) - self.__get_node_height(t.right_child.left_child) == -1:
                t.right_child = self.__rotation(t.right_child,False)
                return self.__rotation(t,True)
            else:
                return self.__rotation(t,True)
        elif balance == -2:
            if self.__get_node_height(t.left_child.right_child) - self.__get_node_height(t.left_child.left_child) == 1:
                t.left_child = self.__rotation(t.left_child,True)
                return self.__rotation(t,False)
            else:
                return self.__rotation(t,False)
        # if balanced, return original root of the subtree
        else:
            return t

    def __rins(self,value,node):
        # base case
        if node == None:
            new_node = Binary_Search_Tree.__BST_Node(value)
            return new_node
        # recursive case
        else:
            if node.value == value:
                raise ValueError
            elif node.value > value:
                node.left_child = self.__rins(value,node.left_child)
                node.height = self.__set_height(node)
            else:
                node.right_child = self.__rins(value,node.right_child)
                node.height = self.__set_height(node)
            return self.__balance(node)

    def insert_element(self, value):
        self.__root = self.__rins(value,self.__root)

    def __rrem(self,value,node):
        # if the node does not exist in the tree
        if node == None:
            raise ValueError
        # base case
        if node.value == value:
            if node.left_child == None:
                return node.right_child
            elif node.right_child == None:
                return node.left_child
            else:
                cur = node.right_child
                while cur.left_child != None:
                    cur = cur.left_child
                node.value = cur.value
                node.right_child = self.__rrem(cur.value,node.right_child)
                return node
        # recursive cases
        elif node.value > value:
            node.left_child = self.__rrem(value,node.left_child)
            node.height = self.__set_height(node)
        else:
            node.right_child = self.__rrem(value,node.right_child)
            node.height = self.__set_height(node)
        return self.__balance(node)

    def remove_element(self, value):
        self.__root = self.__rrem(value,self.__root)

    def __rin_order(self,node):
        # performs string concatenation for each node
        # conditionals check if one or both children are missing and
        # returns the values that are present, with the parent's value
        # being in between left and right
        if (node.left_child == None) and (node.right_child == None):
            return str(node.value)
        elif node.left_child == None:
            right = self.__rin_order(node.right_child)
            return str(node.value) + ', ' + right
        elif node.right_child == None:
            left = self.__rin_order(node.left_child)
            return left + ', ' + str(node.value)
        else:
            left = self.__rin_order(node.left_child)
            right = self.__rin_order(node.right_child)
            return left + ', ' + str(node.value) + ', ' + right

    def in_order(self):
        # left node right
        if self.get_height() == 0:
            return '[ ]'
        else:
            return '[ ' + self.__rin_order(self.__root) + ' ]'

    def __rto_list(self,return_list,node):
        if (node.left_child == None) and (node.right_child == None):
            return_list.append(node.value)
        elif node.left_child == None:
            return_list.append(node.value)
            self.__rto_list(return_list,node.right_child)
        elif node.right_child == None:
            self.__rto_list(return_list,node.left_child)
            return_list.append(node.value)
        else:
            self.__rto_list(return_list,node.left_child)
            return_list.append(node.value)
            self.__rto_list(return_list,node.right_child)

    def to_list(self):
        to_return = []
        if self.get_height() == 0:
            return []
        self.__rto_list(to_return,self.__root)
        return to_return


    def __rpre_order(self,node):
        # performs string concatenation for each node
        # conditionals check if one or both children are missing and
        # returns the values that are present, with the parent's value first
        if (node.left_child == None) and (node.right_child == None):
            return str(node.value)
        elif node.left_child == None:
            right = self.__rpre_order(node.right_child)
            return str(node.value) + ', ' + right
        elif node.right_child == None:
            left = self.__rpre_order(node.left_child)
            return str(node.value) + ', ' + left
        else:
            left = self.__rpre_order(node.left_child)
            right = self.__rpre_order(node.right_child)
            return str(node.value) + ', ' + left + ', ' + right

    def pre_order(self):
        # node left right
        if self.get_height() == 0:
            return '[ ]'
        else:
            return '[ ' + self.__rpre_order(self.__root) + ' ]'

    def __rpost_order(self,node):
        # performs string concatenation for each node
        # conditionals check if one or both children are missing and
        # returns the values that are present, with the parent's value last
        if (node.left_child == None) and (node.right_child == None):
            return str(node.value)
        elif node.left_child == None:
            right = self.__rpost_order(node.right_child)
            return right + ', ' + str(node.value)
        elif node.right_child == None:
            left = self.__rpost_order(node.left_child)
            return left + ', ' + str(node.value)
        else:
            left = self.__rpost_order(node.left_child)
            right = self.__rpost_order(node.right_child)
            return left + ', ' + right + ', ' + str(node.value)

    def post_order(self):
        # left right node
        if self.get_height() == 0:
            return '[ ]'
        else:
            return '[ ' + self.__rpost_order(self.__root) + ' ]'

    def get_height(self):
        if self.__root == None:
            height = 0
        else:
            height = self.__root.height
        return height

    def __str__(self):
        return self.in_order()

if __name__ == '__main__':
    pass

