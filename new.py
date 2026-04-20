def power(x, n):
    """
    Compute x raised to the power n.
    Handles negative exponents and avoids recursion for efficiency.
    """
    if n == 0:
        return 1
    if x == 0 and n != 0:
        raise ValueError("0 raised to non-zero power is undefined for negative exponents")
    
    result = 1.0
    abs_n = abs(n)
    for _ in range(abs_n):
        result *= x
    
    if n < 0:
        return 1 / result
    return result

# Example usage with error handling
try:
    x = float(input("Enter the base (x): "))
    n = int(input("Enter the exponent (n): "))
    result = power(x, n)
    print(f"{x} raised to the power {n} is {result}")
except ValueError as e:
    print(f"Error: {e}")
except:
    print("Invalid input. Please enter numbers.")
