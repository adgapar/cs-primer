def convert_to_romain(n: int) -> str:
    """
    Start from the largest number possible:
    1. M - 1000, D -> 500, C -> 100
    2. Check substractive cases
    """
    substractive_cases = {
        4: 'IV', # 4 of ones
        9: 'IX', # 9 of ones
        40: 'XL', # 4 of tens X
        90: 'XC', # 9 of tens
        400: 'CD', # 4 of hundreds C
        900: 'CM' # 9 of hundres
    }

    roman = ''

    # Get all thousands
    thousands = n // 1000
    roman += thousands * 'M'
    n -= thousands*1000

    # n should be less than 1000
    hundreds = n // 100
    if hundreds in (4,9):
        roman += substractive_cases[hundreds*100]
        n -= hundreds*100
    else:
        roman += (n // 500) * 'D'
        n -= (n // 500) * 500
        roman += (n // 100) * 'C'
        n -= (n // 100) * 100

    # n should be less than 100
    tens = n // 10
    if tens in (4,9):
        roman += substractive_cases[tens*10]
        n -= tens * 10
    else:
        roman += (n // 50) * 'L'
        n -= (n // 50) * 50
        roman += (n // 10) * 'X'
        n -= (n // 10) * 10

    # n should be less than 10
    if n in (4,9):
        roman += substractive_cases[n]
    else:
        roman += (n // 5) * 'V'
        n -= (n // 5) * 5
        roman += n * 'I'

    return roman


if __name__ == "__main__":
    cases = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (11, 'XI'),
        (12, 'XII'),
        (14, 'XIV'),
        (39, 'XXXIX'),
        (47, 'XLVII'),
        (50, 'L'),
        (95, 'XCV'),
        (100, 'C'),
        (246, 'CCXLVI'),
        (420, 'CDXX'),
        (500, 'D'),
        (789, 'DCCLXXXIX'),
        (910, 'CMX'),
        (1000, 'M'),
        (1066, 'MLXVI'),
        (1900, 'MCM'),
        (2000, 'MM'),
        (2025, 'MMXXV'),
        (2421, 'MMCDXXI')
    ]

    for num, exp in cases:
        result = convert_to_romain(num)
        assert result == exp, f"Failed in test case ({num},{exp}), got {result}"