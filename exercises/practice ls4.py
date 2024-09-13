def sum(num1: int, num2: int) -> int:
    """sum of two numbers"""
    return num1 + num2


def happy(word: str) -> str:
    """pretend to be happy"""
    return "No, you are not " + word + ", you are happy!"


def sum(num1: int, num2: int) -> int:
    """Add two numbers together"""
    return num1 + num2


print(sum(num1=4, num2=5))


def division(x: int, y: int) -> float:
    return y / x
    print(y % x)


# The reason the print(y % x) statement does not produce any output is because
# it is placed after the return statement in the function. Once Python encounters
# a return statement, it immediately exits the function and returns the specified value,
# so any code after the return is never executed.
def give_cookies(total_cookies: int, num_students: int) -> int:
    print("Extra cookies: " + str(total_cookies % num_students))
    return int((total_cookies - (total_cookies % num_students)) / 2)


print(
    "Each student gets "
    + str(give_cookies(total_cookies=11, num_students=2))
    + "cookies"
)


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        print("match!")
        return "match!"
    else:
        print("no match!")
        return "no match!"


check_first_letter(word="happy", letter="h")
check_first_letter(word="happy", letter="a")
