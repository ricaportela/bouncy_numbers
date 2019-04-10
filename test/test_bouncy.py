from bouncy_numbers import number_is_increase, number_is_decrease, number_is_bouncy, bouncy_number


def test_check_number_is_increase():
    assert number_is_increase(134468)
    assert number_is_increase(12)
    assert number_is_increase(123)
    assert number_is_increase(1235)

def test_check_number_not_is_increase():
    assert not number_is_increase(21)

def test_check_number_is_decrease():
    assert number_is_decrease(66420)
    assert number_is_decrease(21)
    assert number_is_decrease(321)

def test_check_number_not_is_decrease():
    assert not number_is_decrease(12)
    assert not number_is_decrease(1231)
    assert not number_is_decrease(34534)

def test_check_number_is_bouncy():
    assert number_is_bouncy(155349)

def test_frequency():
    """In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
        Find the least number for which the proportion of bouncy numbers is exactly 99%.
    """
    assert bouncy_number(0.5) == 538
    assert bouncy_number(0.9) == 21780
