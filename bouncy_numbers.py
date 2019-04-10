""" This is the problem:

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. 
In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

"""
from itertools import count


def number_is_increase(number: int) -> bool:
    num_str = str(number)
    previous = 0
    for c in num_str:
        c = int(c)
        if previous > c:
            return False
        previous = c
    return True


def number_is_decrease(number: int) -> bool:
    num_str = ''.join(reversed(str(number)))
    return number_is_increase(int(num_str))


def number_is_bouncy(number: int) -> bool:
    return (not number_is_increase(number)) and (not number_is_decrease(number))


def bouncy_number(freq: float) -> int:
    bouncy_qty = 0
    for i in count(100):
        if number_is_bouncy(i):
            bouncy_qty += 1
            freq_calculated = bouncy_qty / i
            if freq_calculated >= freq:
                return i

