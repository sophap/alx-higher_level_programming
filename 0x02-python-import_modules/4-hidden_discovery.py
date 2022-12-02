#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for item in list:
        if item[0] != '_':
            print(item)
