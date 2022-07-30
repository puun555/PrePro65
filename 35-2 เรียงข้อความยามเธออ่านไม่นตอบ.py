"""เรียงข้อความ ยามเธออ่านไม่ตอบ CR:P'โรม(นายกัมปนาท คนคล่อง)"""
def main():
    """good dog"""
    book = [input(), input(), input()]
    book = sorted(book, key=len)
    print(book[0].capitalize(), book[1].capitalize(), book[2].capitalize(), sep="\n")
main()
