#!/usr/bin/python3
"""
factorial_recursive.py - Calculate factorial using recursion
Documentation example with AI assistance (ChatGPT)
"""

import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    The factorial of a non-negative integer n is the product of all positive
    integers less than or equal to n. It is defined as:
        n! = n × (n-1) × (n-2) × ... × 1
    By mathematical convention, 0! = 1.
    
    Parameters:
    -----------
    n : int
        The non-negative integer for which to calculate the factorial.
        Must be >= 0.
    
    Returns:
    --------
    int
        The factorial of n (n!)
    
    Raises:
    -------
    ValueError
        If n is negative (factorial is not defined for negative numbers)
    RecursionError
        If n is too large, causing maximum recursion depth exceeded
    
    Examples:
    ---------
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    """
    # Input validation
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


def main():
    """
    Main function to handle command line execution.
    
    Reads an integer from command line arguments, calculates its factorial,
    and prints the result.
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial_recursive.py <number>")
        print("Example: ./factorial_recursive.py 5")
        sys.exit(1)
    
    try:
        # Convert argument to integer
        num = int(sys.argv[1])
        
        # Calculate factorial
        result = factorial(num)
        
        # Display result
        print(f"The factorial of {num} is: {result}")
        
    except ValueError as e:
        # Handle invalid integer input or negative numbers
        if "invalid literal" in str(e):
            print("Error: Please provide a valid integer")
        else:
            print(f"Error: {e}")
        sys.exit(1)
    except RecursionError:
        # Handle recursion depth limit
        print("Error: Number is too large for recursive calculation")
        print("Try using an iterative approach instead")
        sys.exit(1)


if __name__ == "__main__":
    main()
