from Binary_Search_Tree import Binary_Search_Tree

class Fraction:

  def __init__(self, numerator, denominator):
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    c = 0
    while d != 0:
      print(c)
      print(n,d)
      c += 1
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    if self.to_float() < other.to_float():
      return True
    else:
      return False

  def __gt__(self, other):
    if self.to_float() > other.to_float():
      return True
    else:
      return False

  def __eq__(self, other):
    if self.to_float() == other.to_float():
      return True
    else:
      return False

  def to_float(self):
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  def __repr__(self):
    return str(self)

if __name__ == '__main__':
  #requires Binary_Search_Tree.py file
  #create a bunch of fraction objects and store them in an array.
  #Then insert each item from the array into a balanced BST.

  numerators = [2,4,5,8,17]
  denominators = [1,3,7,11,13]

  fractions = []
  for n in numerators:
    for d in denominators:
      fractions.append(Fraction(n,d))

  tree = Binary_Search_Tree()
  for f in fractions:
    tree.insert_element(f)
  
  in_order_rep = tree.to_list()

  print("Test 1: Sort Fractions with No Errors")
  print(f"Original: {fractions}")
  print(f"In-order: {in_order_rep}")

  numerator = 2
  denominator = 3

  fractions = []
  fractions.append(Fraction(numerator,denominator))
  fractions.append(Fraction(numerator*2,denominator*2))

  print("Test 2: Catch ValueError")
  try:
    for f in fractions:
      tree.insert_element(f)
    in_order_rep = tree.to_list()
  except ValueError:
    print(f"Correctly caught ValueError when inserting {fractions[1]}")

  
