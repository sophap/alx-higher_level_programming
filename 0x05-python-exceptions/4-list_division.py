#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for y in range(list_length):
        try:
            quot = my_list_1[y] / my_list_2[y]
        except ZeroDivisionError:
            print("division by 0")
            quot = 0
        except (TypeError, ValueError):
            print("wrong type")
            quot = 0
        except IndexError:
            print("out of range")
            quot = 0
        finally:
            res.append(quot)
    return res
