"""ตารางสูตรคูณแบบตามใจฉัน CR:P'Earth(นายศุภกร ดาราสุนทโร)"""
def main():
    """ตารางสูตรคูณแบบตามใจฉัน"""
    num_n, num_m = int(input()), int(input())
    print("-----")
    for i in range(2, num_n+1):
        for j in range(1, num_m+1):
            print("%d x %d = %d" % (i, j, (i*j)))
        print("-----")
main()
