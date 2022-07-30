"""ProfileAgain CR:P'Earth(นายศุภกร ดาราสุนทโร)"""
def main():
    """ProfileAgain"""
    gender = input()
    code_id = input()
    name = input()
    surname = input()
    age = input()
    job = input()
    print("======")
    print("ID : " + code_id[:6])
    print(("Name : " + gender.lower().replace("female", "Mrs. ").replace("male", "Mr. "))\
        + name.capitalize() + " " + surname.capitalize())
    print("Age : " + age + " years old")
    print("Occupation : " + job.upper())
    print("======")
main()
