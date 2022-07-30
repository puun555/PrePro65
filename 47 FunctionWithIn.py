"""TheFunctionWithin CR:P'นายเขมฐิติ หวังทรัพย์ทวี"""
def func_f(var_x):
    """Func F"""
    return 2 * var_x

def func_g(var_x):
    """Func G"""
    return (3 * var_x ** 4) - (var_x ** 3) + (2 * var_x ** 2) + 10

def func_h(var_x, var_y, var_z):
    """Func H"""
    return ((var_z + var_x) ** 2) - (var_x * var_y) + (var_y ** 2)

def func_i(var_a, var_b, var_c, var_d):
    """Func I"""
    return (var_a ** 2 + var_b ** 2 - var_c ** 2) \
        / (var_d ** 2 - 2 * var_a * var_d + 2 * var_a)

def main():
    """TheFunctionWithin"""
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
    print(func_f(func_f(var_a)))
    print(func_g(func_f(var_a - var_b)))
    print(func_h(func_f(var_a + var_b), func_f(var_a + var_c), func_g(func_f(var_d ** 2))))
    print(func_i(func_h(func_f(var_a + var_b), func_f(var_a - var_c), func_g(func_f(var_d ** 2))),\
    func_g(func_f(var_a - var_b)),\
    func_f(func_f(func_f(func_f(func_f(var_c))))),\
    var_d ** 8))
main()
