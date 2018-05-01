class fizzbuzz:

  def is_divisible_by(number, divisor):
      return number % divisor == 0

  def is_divisible_by_15(number):
      return fizzbuzz.is_divisible_by(number, 15)

  def is_divisible_by_5(number):
      return fizzbuzz.is_divisible_by(number, 5)

  def is_divisible_by_3(number):
      return fizzbuzz.is_divisible_by(number, 3)
