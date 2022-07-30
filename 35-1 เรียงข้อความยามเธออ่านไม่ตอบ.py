"""เรียงข้อความ ยามเธออ่านไม่ตอบ CR:P'Earth(นายศุภกร ดาราสุนทโร)"""
def main():
    """เรียงข้อความ ยามเธออ่านไม่ตอบ"""
    word_1 = input().capitalize()
    word_2 = input().capitalize()
    word_3 = input().capitalize()
    if len(word_1) > len(word_2):
        tmp = word_2
        word_2 = word_1
        word_1 = tmp
    if len(word_1) > len(word_3):
        tmp = word_3
        word_3 = word_1
        word_1 = tmp
    if len(word_2) > len(word_3):
        tmp = word_3
        word_3 = word_2
        word_2 = tmp
    print("%s\n%s\n%s" %(word_1, word_2, word_3))
main()
