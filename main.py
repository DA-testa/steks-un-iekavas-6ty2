# python3
# Arturs Ivautenko 221RDB358 1.grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for I, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, I+1))
        
        if next in ")]}":
            if not opening_brackets_stack:
                return I+1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return I+1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
