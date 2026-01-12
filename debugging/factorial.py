#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1    # هذا هو التصحيح الذي أضفناه
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        print(factorial(num))
    except ValueError:
        print("Error")
