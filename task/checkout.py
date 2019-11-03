#!/usr/bin/env python3
from typing import Callable


def parse_check(check: str) -> dict:
    parsed_check = {char: check.count(char) for char in set(check)}
    return parsed_check

def parse_product_table(products_data: str) -> dict:
    if not products_data:
        raise ValueError
    products = {}
    products_splited: list = products_data.split('\n')
    for product in products_splited:
        product_fields: list = product.split(';')

        name = product_fields[0].strip()
        price = int(product_fields[1])
        rule = product_fields[2].strip() if product_fields[2].strip() else None

        products[name] = [price, rule]
    return products

def parse_price_rule(input_rule: str) -> Callable:
    if (not input_rule) or (not input_rule.strip()):
        return lambda count, price: count * price    
    
    splited_rule = input_rule.split('for')
    if len(splited_rule) == 2:
        try:
            left_operand, right_operand = [int(x) for x in splited_rule]
        except ValueError:
            raise ValueError('Wrong input parameters. Operand should be integer')
        parsed_function = lambda count, price: (count // left_operand) \
                         * right_operand + (count % left_operand) * price
    else:
        try:
            left_operand, right_operand = [int(x) for x in input_rule.split('+')]
        except ValueError:
            raise ValueError('Wrong input parameters. Operand should be integer')
        parsed_function = lambda count, price: \
                    count * price - (count // (left_operand + right_operand)) \
                    * right_operand * price
    return parsed_function


def calculate_price(product_table: dict, products: dict) -> float:
    check_sum = 0.0 
    for product in products:
        count = products[product]
        price = product_table[product][0]
        rule_str = product_table[product][1]
        rule_func = parse_price_rule(rule_str)
        
        position_price = rule_func(count, price)


        check_sum += position_price

    return check_sum 