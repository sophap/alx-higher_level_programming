#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    x = 0
    sum = 0
    if isinstance(roman_string, str):
        for x in range(len(roman_string) - 1):
            if rom_num[roman_string[x]] >= rom_num[roman_string[x + 1]]:
                sum += rom_num[roman_string[x]]
            else:
                sum -= rom_num[roman_string[x]]
            x += 1
            sum += rom_num[roman_string[x]]
            return sum
        else:
            return 0
