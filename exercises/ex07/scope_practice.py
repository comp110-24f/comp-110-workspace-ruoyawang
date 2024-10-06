def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
            # If fn
        index += 1
    return copy


word: str = "yoyo"
print(remove_chars(word, "o"))
print(word)
