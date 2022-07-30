"""Fibonacci CR:P'นายภูริวัจน์ ปิติพงศ์มนตรี"""

def fibonacci(num):
    """process_Fibonacci"""
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def main(num):
    """Fibonacci"""
    print(fibonacci(num))

main(int(input()))
