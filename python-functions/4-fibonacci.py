#!/usr/bin/python3
def fibonacci_sequence(n):
    if n in {0, 1}:
        return n
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
