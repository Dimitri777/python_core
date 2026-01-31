"""
Portfolio: Frozenset (immutable set)
Topic: set vs frozenset; frozenset as dict key or set element
"""


def main():
    print("=== Set vs Frozenset ===\n")

    # set is mutable
    s = {1, 2, 3}
    s.add(4)
    print("  set: mutable, can add/remove ->", s)

    # frozenset is immutable
    fs = frozenset({1, 2, 3})
    print("  frozenset: immutable ->", fs)
    try:
        fs.add(4)
    except AttributeError as e:
        print("  fs.add(4) -> AttributeError:", e)

    # frozenset can be dict key (set cannot)
    print("\n--- Frozenset as dict key ---")
    d = {frozenset({"a", "b"}): "group_ab", frozenset({"c"}): "group_c"}
    print("  d[frozenset({'a','b'})] =", d[frozenset({"a", "b"})])
    print("  d[frozenset({'c'})] =", d[frozenset({"c"})])

    # frozenset can be element of set (set of sets: use frozenset)
    print("\n--- Set of sets (use frozenset) ---")
    set_of_sets = {frozenset({1, 2}), frozenset({2, 3})}
    print("  set_of_sets =", set_of_sets)


if __name__ == "__main__":
    main()
