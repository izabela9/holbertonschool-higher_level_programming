#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            x = my_list_1[i]
            y = my_list_2[i]

            if not (isinstance(x, (int, float))
                    and isinstance(y, (int, float))):
                print("wrong type")
                result.append(0)
            elif y == 0:
                print("division by 0")
                result.append(0)
            else:
                division = x / y
                result.append(division)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            continue
    return (result)
