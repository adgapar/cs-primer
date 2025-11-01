cache = {}

def count_ways(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    if n in cache:
        return cache[n]

    count = 0
    # first step is 1
    count += count_ways(n-1)
    # first step is 2
    count += count_ways(n-2)
    # first step is 3
    count += count_ways(n-3)

    if count not in cache:
        cache[n] = count

    return count


if __name__ == "__main__":
    assert count_ways(1) == 1
    assert count_ways(2) == 2
    assert count_ways(3) == 4
    assert count_ways(4) == 7
    assert count_ways(5) == 13
    
    for n in range(5, 10):
        print(f"n={n}: ways={count_ways(n)}")

    # n=5
    # 1 -> all combinations of n=4 -> 7
    # 2 -> all combinations of n=3 -> 4
    # 3 -> all combinations of n=2 -> 2

    # n=4
    # 1 -> 111, 12, 21, 3 (4)
    # 2 -> 11, 2
    # 3 -> 1

    # n=3
    # 111
    # 12
    # 21
    # 3

    # n=2
    # 11
    # 2

    # n=1
    # 1