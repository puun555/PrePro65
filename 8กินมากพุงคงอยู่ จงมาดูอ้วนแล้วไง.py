'''กินมากพุงคงอยู่ จงมาดูอ้วนแล้วไง'''
def main():
    '''main'''
    name = input()
    weight = int(input())
    height = int(input())/100
    bmi = weight/(height*height)
    print("Name: %s\nWeight: %d kg.\nHeight: %.2f m.\nBMI: %.2f"%(name, weight, height, bmi))
main()
