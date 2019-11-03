#!/usr/bin/env python3

from checkout import parse_product_table, parse_check, calculate_price

def read_input_file(file_name: str) -> str:
    file = open(file_name, 'r')
    content_str = file.read()
    file.close()
    return content_str


def main():
    product_rules = read_input_file('./product_rules.txt')
    products_check = read_input_file('./products_check.txt')
   
    product_rules_parsed = parse_product_table(product_rules)
    products_check_parsed = parse_check(products_check)
    print('Product rules:\n\n', product_rules_parsed) 
    print('Products check:\n\n', products_check_parsed)

    total_price = calculate_price(product_rules_parsed, products_check_parsed)
    print('Total price is', total_price)


if __name__ == '__main__':
    main()

