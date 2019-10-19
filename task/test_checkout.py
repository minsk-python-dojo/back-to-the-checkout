from string import ascii_uppercase
from random import choice

from checkout import parse_check


def test_parse_str_one_item_returns_dict_with_one_key():
    our_check = choice(ascii_uppercase)
    our_dict = parse_check(our_check)
    assert (our_dict == {our_check: 1})

def test_parse_str_two_same_items_returns_dict_with_one_key():
    our_check = choice(ascii_uppercase) * 2
    our_dict = parse_check(our_check)
    assert (our_dict == {our_check[0]: 2})
