'''[Quiz] โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว CR:นางสาวศิโรรัตน์ นามบุญ'''
def main():
    '''out'''
    name = input()
    age = int(input())
    gender = input().replace("Male", "Mr.").replace("Female", "Miss")
    height = float(input())
    text = ""
    if age >= 13 and age <= 15:
        if gender == "Mr." and height >= 160 or gender == "Miss" and height >= 155:
            text = "You can study in junior high school."
        else:
            text = "You can not join this school."
    elif age >= 16 and age <= 18:
        if gender == "Mr." and height >= 170 or gender == "Miss" and height >= 165:
            text = "You can study in senior high school."
        else:
            text = "You can not join this school."
    else:
        text = "You can not join this school."
    print(gender, name+" Age: %d Height: %.2f" %(age, height))
    print(text)
main()
