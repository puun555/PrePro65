"""Cr. P'tam"""
def main():
    """main"""
    startx = 0
    gotox = 0
    beforex = 0
    linex = input().split()
    for i in linex:
        gotox = abs(float(i) - beforex)
        startx += gotox
        beforex = float(i)
    print("%0.2f" %startx)
main()
