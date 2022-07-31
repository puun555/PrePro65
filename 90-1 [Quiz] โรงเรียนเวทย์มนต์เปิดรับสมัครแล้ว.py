"""IG: few.pz [Quiz] โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว CR:นายพีรณัฐ หมัดสอ"""
def main():
    """ Main function """
    name = input()
    age = int(input())
    sex = input()
    height = float(input())

    sex = sex.lower()
    msg = "You can not join this school."
    if 13 <= age <= 15:
        if sex == "male":
            if height >= 160:
                msg = "You can study in junior high school."
        else:
            if height >= 155:
                msg = "You can study in junior high school."
    elif 16 <= age <= 18:
        if sex == "male":
            if height >= 170:
                msg = "You can study in senior high school."
        else:
            if height >= 165:
                msg = "You can study in senior high school."

    if sex == "male":
        print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
    else:
        print("Miss %s Age: %d Height: %.2f" %(name, age, height))
    print(msg)
main()
