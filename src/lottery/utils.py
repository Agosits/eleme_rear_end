CONSTANT = 10000


def lottery_algorithm(sh_args=None, sz_args=None, total=None):
    assert sh_args, "invalid sh_args"
    assert sz_args, "invalid sz_args"
    assert total and isinstance(total, int), " invalid total"
    temp_number = reverse_int_number(int(round(sh_args * sz_args * CONSTANT)))
    try:
        lottery_number = temp_number % total + 1
    except Exception as e:
        print(str(e), "compute remainder error ")
        raise
    else:
        return lottery_number


def reverse_int_number(number=None):
    assert number and isinstance(number, int)
    reversed_str_number = int(str(number)[::-1])
    return reversed_str_number


if __name__ == "__main__":
    print(lottery_algorithm(2894.47, 9975.42, 150000))
