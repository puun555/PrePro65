"""Cr. P'ปุญญพันธ์"""
def main():
    """doc"""
    num = int(input())
    dtt = []
    for _ in range(num):
        nmm = input().split()
        nmm[0], nmm[2] = nmm[2], nmm[0]
        dtt += [nmm]
    dtt.sort()
    job = []
    tmp = 1
    for i in dtt:
        if i[0] not in job:
            job += [i[0]]
    for i in job:
        print("OCCUPATION :", i.upper())
        for j in dtt:
            if j[0] == i:
                print("%d. %s, %s"%(tmp, j[1], j[2]))
                tmp += 1
        tmp = 1
main()
