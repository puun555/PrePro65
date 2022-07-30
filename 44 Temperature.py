"""Temperature CR:P'ทิว(นายธีระวัฒน์ แสงจันทร์)"""
def to_c(temp, kind):
    """to_c"""
    if kind[0] == "F":
        return (temp-32)*5/9
    elif kind[0] == "K":
        return temp-273.15
    elif kind[0] == "R":
        return (temp*5/9)-273.15


def main():
    """main"""
    temp = float(input())
    kind = input()
    if kind[0] != "C":
        temp = to_c(temp, kind[0])
    if kind[2] == "F":
        print("Fahrenheit = %.2f"%((temp*9/5)+32))
    elif kind[2] == "K":
        print("Kelvin = %.2f"%(temp+273.15))
    elif kind[2] == "R":
        print("Rankine = %.2f"%((temp+273.15)*9/5))
    else:
        print("Celsius = %.2f"%temp)
main()
