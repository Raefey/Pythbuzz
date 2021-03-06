from fizzbuzz import fizzbuzz


def test_is_divisible_by_true():
    assert fizzbuzz.is_divisible_by(15, 5) == True

def test_is_divisible_by_false():
    assert fizzbuzz.is_divisible_by(107, 5) == False

def test_is_divisible_by_15_true():
    assert fizzbuzz.is_divisible_by_15(60) == True

def test_is_divisible_by_15_false():
    assert fizzbuzz.is_divisible_by_15(72) == False

def test_is_divisible_by_5_true():
    assert fizzbuzz.is_divisible_by_5(100) == True

def test_is_divisible_by_5_false():
    assert fizzbuzz.is_divisible_by_5(73) == False

def test_is_divisible_by_3_true():
    assert fizzbuzz.is_divisible_by_3(21) == True

def test_is_divisible_by_3_false():
    assert fizzbuzz.is_divisible_by_3(22) == False

def test_say_fizzbuzz():
    assert fizzbuzz.say(15) == 'Fizzbuzz'

def test_say_buzz():
    assert fizzbuzz.say(5) == 'Buzz'

def test_say_fizz():
    assert fizzbuzz.say(3) == 'Fizz'

def test_say_fizzbuzz():
    assert fizzbuzz.say(37) == 37
