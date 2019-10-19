from dataclasses import dataclass
from collections import defaultdict
from typing import Callable


@dataclass
class StoreItem:
    name: str
    price: int
    rule: Callable

    @classmethod
    def from_str(cls, item_line: str):
        (name, price_str, rule_str) = item_line.split(';')
        price = int(price_str)
        if '+' in rule_str:
            left_operand = int(rule_str[0])
            right_operand = int(rule_str[2])
            off_count = left_operand + right_operand
            rule = lambda count: price * (count - count // off_count)
        else:
            left_operand = int(rule_str[0])
            right_operand = int(rule_str[4:])
            off_price = (left_operand * price - right_operand)
            rule = lambda count: count * price - off_price * (count // left_operand)
        return cls(name, price, rule)


ITEMS_DATA = (
    'A;50;2+1\n'
    'B;100;2for170\n'
    'C;18;3+1'
)

check_line = 'AABCCCABAAAABBB'

store_items = [
    StoreItem.from_str(item_line)
    for item_line in ITEMS_DATA.splitlines()
]

items_map = {
    store_item.name: store_item
    for store_item in store_items
}


check_item_count = defaultdict(int)

for item_name in check_line:
    check_item_count[item_name] += 1

print(f"A price: {items_map['A'].rule(check_item_count['A'])}")
print(f"B price: {items_map['B'].rule(check_item_count['B'])}")
