def num_instances(inp_str: str, search_str: str):
    count = 0  # To count occurrences of search_str
    index = 0  # To iterate through inp_str

    while index <= len(inp_str) - len(search_str):  # HelloHelloHEllo (15 - 2)
        sub_index = 0
        match = True
        while sub_index < len(search_str):
            if inp_str[index + sub_index] != search_str[sub_index]:
                match = False
            sub_index += 1
        if match == True:
            count += 1
            index += len(search_str)
        else:
            index += 1
    print(count)


num_instances("HelloHelloHEllo", "ll")  # Output should be 3


def multiple_each_val_by_idx(num: int) -> str:
    num = str(num)
    index = 0
    new_num = ""
    while index < len(num):
        new_num += str(int(num[index]) * index)
        index += 1
    print(new_num)
    return new_num


multiple_each_val_by_idx(num=12345)


def main() -> None:
    x: str = "x"
    y: str = "y"
    z: str = x
    y = x
    x = "y"

    if not (x != y and x != "y"):
        print(f"x: {x}")
    else:
        print("'if' condition not met.")


main()
