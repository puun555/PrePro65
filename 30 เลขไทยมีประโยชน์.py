'''เลขไทยมีประโยชน์'''
def main():
    '''main'''
    mul = 1
    discount = 1
    # check nation state
    check_thai = input()
    if check_thai == "N":
        mul = 5
        check_nation = input()
        # check the multipy of no thai nation
        if check_nation == "Vietnam" or check_nation == "India" or check_nation == "Singapore":
            mul = 2.5
    #input age
    age = int(input())
    # check coupon state
    check_coupon = input()
    if check_coupon == "Y":
        discount -= int(input())/100
    # check cost state and print state
    if 10 < age <= 20:
        cost = 20*mul*discount
    elif 20 < age <= 60:
        cost = 40*mul*discount
    else:
        cost = 0
    print("%.2f"%cost)
main()
