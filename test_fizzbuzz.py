from fizzbuzz import fizzbuzz


def test_is_divisible_by():
    result = fizzbuzz.is_divisible_by(15, 5)
    assert result == True

def test_is_divisible_by_by_15():
    result = fizzbuzz.is_divisible_by_15(60)
    assert result == True
