import bouncy_numbers


def test_check_number_is_increase():
    assert bouncy_numbers.number_is_increase(134468)
    assert bouncy_numbers.number_is_increase(12)
    assert bouncy_numbers.number_is_increase(123)
    assert bouncy_numbers.number_is_increase(1235)


def test_check_number_not_is_increase():
    assert not bouncy_numbers.number_is_increase(21)


def test_check_number_is_decrease():
    assert bouncy_numbers.number_is_decrease(66420)
    assert bouncy_numbers.number_is_decrease(21)
    assert bouncy_numbers.number_is_decrease(321)


def test_check_number_not_is_decrease():
    assert not bouncy_numbers.number_is_decrease(12)
    assert not bouncy_numbers.number_is_decrease(1231)
    assert not bouncy_numbers.number_is_decrease(34534)


def test_check_number_is_bouncy():
    assert bouncy_numbers.number_is_bouncy(155349)


def test_frequency():
    """ In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
        Find the least number for which the proportion of bouncy numbers is exactly 99%.
    """
    assert bouncy_numbers.bouncy_number(0.5) == 538
    
