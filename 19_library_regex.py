"""
Portfolio: Regular Expressions (re)
Topic: re.search, re.findall, re.match, groups
"""

import re


def main():
    print("=== Regular Expressions (re) Demo ===\n")

    text = "Contact: alice@mail.com and bob@test.org, phone 123-456-7890"

    # search: first match
    match = re.search(r"\w+@\w+\.\w+", text)
    if match:
        print("  re.search(r'\\w+@\\w+\\.\\w+'):", match.group())

    # findall: all matches
    emails = re.findall(r"\w+@\w+\.\w+", text)
    print("  re.findall (emails):", emails)

    # groups
    m = re.search(r"(\d{3})-(\d{3})-(\d{4})", text)
    if m:
        print("  Phone groups:", m.groups())
        print("  Full match:", m.group(0))

    # match vs search: match only at start
    line = "hello world"
    print("\n  re.match(r'hello', line):", re.match(r"hello", line) is not None)
    print("  re.match(r'world', line):", re.match(r"world", line) is not None)
    print("  re.search(r'world', line):", re.search(r"world", line) is not None)


if __name__ == "__main__":
    main()
