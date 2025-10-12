import time

def verify(digits: str) -> bool:
    """
    1789372997 -> payload
    From right to left:
    7 -> x2 = 14 -> -9 = 5
    9 -> x1 = 9
    9 -> x2 = 18 -> -9 = 9
    2 -> x1 = 2
    7 -> x2 = 14 -> -9 = 5
    3 -> x1 = 3
    9 -> x2 = 18 -> -9 = 9
    8 -> x1 = 8
    7 -> x2 = 14 -> -9 = 5
    1 -> x1 = 1

    Total sum = 5 + 9 + 9 + 2 + 5 + 3 + 9 + 8 + 5 + 1 = 56
    Check digit = (10 - (total_sum % 10)) % 10 = (10 - 6) % 10 = 4
    Full account number = 17893729974
    """
    payload = digits[:-1]
    last_digit = int(digits[-1])
    
    # Calculate total sum
    total_sum = 0
    for i, digit in enumerate(reversed(payload)):
        int_digit = int(digit)
        addition = int_digit * (2 - i % 2)
        total_sum += addition // 10 + addition % 10

    # Calculate check digit
    correct_check_digit = (10 - (total_sum % 10)) % 10
    
    return correct_check_digit == last_digit



if __name__ == "__main__":
    assert verify("17893729974") is True
    assert verify("17893729975") is False

    