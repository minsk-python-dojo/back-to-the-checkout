from string import ascii_uppercase
from random import choice
import pytest

from checkout import parse_check, parse_product_table, calculate_price, parse_price_rule


def test_parse_str_one_item_returns_dict_with_one_key():
    our_check = choice(ascii_uppercase)
    our_dict = parse_check(our_check)
    assert (our_dict == {our_check: 1})

def test_parse_str_two_same_items_returns_dict_with_one_key():
    our_check = choice(ascii_uppercase) * 2
    our_dict = parse_check(our_check)
    assert (our_dict == {our_check[0]: 2})

def test_parse_product_table_returns_dict_of_products_when_non_empty_string_is_passed():
    input_string = (
        'A;50;2+1\n'
        'B;100;2for170\n'
        'C;18; '
        )
    our_dict = parse_product_table(input_string)
    expected = {'A': [50, '2+1'],
                'B': [100, '2for170'],
                'C': [18, None]
                }
    assert (our_dict == expected)

def test_parse_product_table_raises_value_error_when_empty_string_is_passed():
    input_string = ''
    with pytest.raises(ValueError):
        parse_product_table(input_string)

def test_calculate_price_return_correct_sum_with_non_empty_products_table():
    input_check = {'A': 1, 'B': 1, 'C': 1}
    input_product_table = {
        'A': [50, '2+1'], 
        'B': [100, '2for170'], 
        'C': [18, None]
    }
    result = calculate_price(input_product_table, input_check)
    expected = 168
    assert result == expected

def test_parse_price_rule_return_plus_function_when_string_plus_rule():
    input_rule = '2+1'
    expected = 100
    parsed_rule_function = parse_price_rule(input_rule)
    parsed_rule_function_result = parsed_rule_function(3, 50)
    assert parsed_rule_function_result == expected

def test_parse_price_rule_return_for_function_when_string_for_rule():
    input_rule = '2for170'
    expected = 170
    parsed_rule_function = parse_price_rule(input_rule)
    parsed_rule_function_result = parsed_rule_function(2, 100)
    assert parsed_rule_function_result == expected