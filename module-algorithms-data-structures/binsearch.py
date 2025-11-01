def binsearch(nums, n) -> int | None:
    start_idx = 0 # 0
    end_idx = len(nums) # 4 - 1 = 3

    print(f"searching for n={n}")

    while start_idx < end_idx:
        mid_idx = (start_idx + end_idx) // 2 # (0+3)//2 = 1
        mid = nums[mid_idx] # mid=1
        if mid == n:
            print(f"found for n={n}")
            return mid_idx
        elif mid < n:
            start_idx = mid_idx+1
        else:
            end_idx = mid_idx

    print(f"did not find for n={n}")
    return None


if __name__ == '__main__':
    a = (0,1,3,4)
    b = (-5,-2,0)

    cases = (
        (a,0,0),
        (a,1,1),
        (a,3,2),
        (a,4,3),
        (b,-5,0),
        (b,-2,1),
        (b,0,2),
        (a,2,None),
        (a,5,None),
        (a,-2,None),
        (b,-10,None),
        (b,1,None),
        (b,-3,None)
    )

    for nums, n, exp in cases:
        assert binsearch(nums, n) == exp

    print('ok')
