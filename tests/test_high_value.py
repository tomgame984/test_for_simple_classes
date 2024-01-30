from lib.high_value import *

"""
get_highest tests:
1.  If first value is higher than second value then return "First value is higher"

2.  If second value is higher than first value then return "Second value is higher"

3.  If first value and second value equal then return "Values are equal".
"""

def test_first_value_higher_than_second_value():
    values = HighValue(8, 4)
    assert values.get_highest() == "First value is higher"

def test_second_value_higher_than_first_value():
    values = HighValue(3, 10)
    assert values.get_highest() == "Second value is higher"

def test_first_value_and_second_value_equal():
    values = HighValue(8, 8)
    assert values.get_highest() == "Values are equal"

"""
add tests:
1. Initiate values class and assign value to first_value and second_vlue
add - Increase first value
return get_highest based on changed state.

2.Initiate values class and assign value to first_value and second_vlue
add - Increase second value
return get_highest based on changed state.
"""

def test_increase_first_value():
    values = HighValue(3, 10)
    values.add(10, 'first')
    assert values.get_highest() == "First value is higher"

def test_increase_second_value():
    values = HighValue(12, 10)
    values.add(10, 'second')
    assert values.get_highest() == "Second value is higher"

def test_multiple_value_increases_result_is_equal():
    values = HighValue(5, 10)
    values.add(10, 'second')
    values.add(15, 'first')
    assert values.get_highest() == "Values are equal"

def test_multiple_value_additions_with_negative():
    values = HighValue(5, 10)
    values.add(-5, 'second')
    values.add(-15, 'first')
    assert values.get_highest() == "Second value is higher"

def test_multiple_value_increases_result_is_both_zero():
    values = HighValue(5, 10)
    values.add(-10, 'second')
    values.add(-5, 'first')
    assert values.get_highest() == "Values are equal"