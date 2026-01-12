# Debugging Exercise: Factorial Calculator

## Overview
This project demonstrates using AI (ChatGPT) to identify and fix a common programming bug: an infinite loop in a factorial calculation function.

## The Bug
Original code had:
```python
while n > 1:
    result *= n
    # Missing: n -= 1
