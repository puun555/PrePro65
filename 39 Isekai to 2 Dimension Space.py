'''Isekai to 2 Dimensional Space'''
import math
def main():
    '''main'''
    px1 = float(input())
    py1 = float(input())
    distance = float(input())
    deg = int(input())
    side_y = distance*(math.sin(math.radians(deg)))
    side_x = distance*(math.cos(math.radians(deg)))
    print("%.2f"%(px1 + side_x))
    print("%.2f"%(py1 + side_y))
main()
