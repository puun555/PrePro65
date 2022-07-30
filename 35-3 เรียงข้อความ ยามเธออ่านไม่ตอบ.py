"""เรียงข้อความ ยามเธออ่านไม่ตอบ CR:P'พัณณิตา สายศร"""
def main():
    """เรียงข้อความ ยามเธออ่านไม่ตอบ"""
    txt1 = input().capitalize()
    txt2 = input().capitalize()
    txt3 = input().capitalize()
    swap = sorted([txt1, txt2, txt3], key=len)

    print(*swap, sep="\n")
main()
