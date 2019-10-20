#!/usr/bin/env python3


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

def calculate_price(product_table: dict, products: dict) -> float:
    check_sum = 0.0 
    return check_sum 