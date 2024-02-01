#!/usr/bin/env python3
def summation_i_squared(n):
    # Check if n is a valid number (int and positive)
    if not isinstance(n, int) or n < 1:
        return None

    # Use the formula to calculate the sum of squares
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6

    return int(sum_of_squares)


# Test the function
if __name__ == "__main__":
    n = 5
    print(summation_i_squared(n))
