'''Toy Factory2 CR:P'เกียร์(นายวรวีร์ วิรวรรณ)'''
def factory2(num):
    '''built a toys'''
    print(num.replace("1", " ^----^").replace("2", "( 0--0 )")\
.replace("3", "<------>").replace("4", "(------)").replace("5", " u----u"))

def main(num1, num2, num3, num4, num5):
    '''main'''
    factory2(num1)
    factory2(num2)
    factory2(num3)
    factory2(num4)
    factory2(num5)
main(input(), input(), input(), input(), input())
