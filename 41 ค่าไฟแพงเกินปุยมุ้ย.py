'''ค่าไฟแพงเกินปุยมุ้ย!!'''
def cal(watt):
    '''cal'''
    unit = (watt/1000)*30
    return unit

def main():
    '''main'''
    television = int(input())
    microwave = int(input())
    dry = int(input())
    light = int(input())
    refrigerator = int(input())

    print("TV %d Watt 1 ea for 3 hours"%television)
    print("%.2f unit."%(cal(television)*3))
    print("Microwave %d Watt 1 ea for 1 hours"%microwave)
    print("%.2f unit."%(cal(microwave)*1))
    print("Hair dryer %d Watt 1 ea for 0.5 hours"%dry)
    print("%.2f unit."%(cal(dry)*0.5))
    print("light bulb %d Watt 4 ea for 5 hours"%light)
    print("%.2f unit."%(cal(light)*5*4))
    print("Refrigerator %d Watt 1 ea for 24 hours"%refrigerator)
    print("%.2f unit."%(cal(refrigerator)*24))
main()
