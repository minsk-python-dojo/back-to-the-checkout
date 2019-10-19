#!/usr/bin/env python3


def parse_check(check: str) -> dict:
    parsed_check = {}
    for char in check:
        parsed_check[char] = check.count(char)
    return parsed_check