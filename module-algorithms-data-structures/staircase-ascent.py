def count_ways(n_steps: int) -> int:
    # unique combination of numbers (1,2,3) that would sum to n
    # combinatorics: diff order of same numbers
    threes = n_steps // 3
    



if __name__ == "__main__":
    assert count_ways(1) == 1
    assert count_ways(2) == 2 # [1, 1], [2]
    assert count_ways(3) == 4 # [1, 1, 1], [1, 2], [3], [2, 1]
    assert count_ways(4) == 7 # [1, 1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2], [3, 1], [1, 3]