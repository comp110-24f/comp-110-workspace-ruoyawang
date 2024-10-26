"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
total_orders: int = 0

# ice_cream { "chocolate": 12, "vanilla": 8, "strawberry": 4}
# total_orders 0
# has_pbj False (has_pbj: bool = "pbj" in ice_cream)
# for flavor in ice_cream:

scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
for x in scores:
    print(x)  # print all keys

fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}
for boo in fruit_count:
    ghost = fruit_count[boo]
    print(f"{boo}: {ghost}")
