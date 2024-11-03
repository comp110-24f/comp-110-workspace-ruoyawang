my_number: list[float] = list()  # constructor version!
my_number.append(1.5)

game_points: list[int] = [102, 86, 94]
grocery_list: list[str] = ["bananas", "milk", "bread"]
grocery_list[1] = "eggs"
grocery_list.append("bananas")
print(grocery_list)
print(grocery_list[len(grocery_list) - 1])
grocery_list.pop(2)
print(grocery_list)
print(grocery_list.pop(2))

my_name: str = "Mia"
# my_name[2] = "i" # does not work!
name_as_list: list[str] = list(my_name)
print(name_as_list)
name_as_list[2] = "i"
print(name_as_list)
name_as_list.insert(2, "h")
print(name_as_list)
print(name_as_list[-1])

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(y)

a: list[int] = [2, 4]
b: list[int] = a
a.append(6)
print(b)
# Stack: a|id:0 (just like declaring a function although not a function)
# b|id:0
# Heap: {id:0|list[int]
# 0  | 2
# 1  | 4
# 2  | 6

a: str = "24"
b: str = a
a += "6"
print(b)

# Stack: a|"24""246" b|"24"
