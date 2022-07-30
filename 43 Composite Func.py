"""Composite_function CR:นายภูริวัจน์ ปิติพงศ์มนตรี"""

def function_g(num):
    """funtion_g"""
    x_of_g = (num**3)+(4*num) - 1
    return x_of_g

def function_f(num):
    """funtion_f"""
    x_of_f = (15 + num - (num**3)) / (((num**2)/3) + 11)
    return x_of_f

def main():
    """main"""
    num = float(input())
    type_f = input().lower()
    if type_f == "gof":
        num = function_f(num)
        ans = function_g(num)
        print("%.2f" %ans)
    elif type_f == "fog":
        num = function_g(num)
        ans = function_f(num)
        print("%.2f" %ans)
main()
