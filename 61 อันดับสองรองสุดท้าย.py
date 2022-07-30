"""อันดับสองรองสุดท้าย CR:นายปุญญพันธ์ ทิพย์ชัชวาลกุล"""
def main():
    """doc"""
    mnn = int(input())
    mnn2 = int(input())
    mnn, mnn2 = mnn2*(mnn >= mnn2)+mnn*(mnn < mnn2), mnn2*(mnn <= mnn2)+mnn*(mnn > mnn2)
    for _ in range(8):
        if mnn - mnn2 != 0:
            temp = int(input())
            if mnn > temp:
                mnn2 = mnn
                mnn = temp
            elif temp > mnn and temp < mnn2:
                mnn2 = temp
        else:
            mnn2 = int(input())
            mnn, mnn2 = mnn2*(mnn >= mnn2)+mnn*(mnn < mnn2), mnn2*(mnn <= mnn2)+mnn*(mnn > mnn2)
    print("Almost the min :", mnn2)
main()
