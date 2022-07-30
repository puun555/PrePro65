"""I'm MAX IV เพิ่ม MIN CR:P'นายเขมฐิติ หวังทรัพย์ทวี"""

def mac(var_a, var_b):
    """Find Max Number"""
    if var_a >= var_b:
        return var_a
    else:
        return var_b

def mein(var_a, var_b):
    """Find Min Number"""
    if var_a <= var_b:
        return var_a
    else:
        return var_b

def main():
    """I'm MAX IV เพิ่ม MIN"""
    var_mode = input().lower()
    var_input1 = int(input())
    var_input2 = int(input())
    var_input3 = int(input())
    var_input4 = int(input())
    var_input5 = int(input())
    if var_mode == "max":
        get_mac = mac(var_input1, mac(var_input2, mac(
            var_input3, mac(var_input4, var_input5))))
        print("MAX : %d" % get_mac)
    elif var_mode == "min":
        get_mein = mein(var_input1, mein(var_input2, mein(
            var_input3, mein(var_input4, var_input5))))
        print("MIN : %d" % get_mein)
main()
