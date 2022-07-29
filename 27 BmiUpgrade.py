'''bmi Upgrade'''
def main():
    '''main'''
    weight = float(input())
    height = float(input())/100
    age = int(input())
    bmi = weight/height**2
    if age < 18:
        print('Please use BMI for Children and Teens.')
    else:
        if bmi < 16:
            print('Severe Thinness')
        elif bmi < 17:
            print('Moderate Thinness')
        elif bmi < 18.5:
            print('Mild Thinness')
        elif bmi < 25:
            print('Normal')
        elif bmi < 30:
            print('Overweight')
        elif bmi < 35:
            print('Obese Class I')
        elif bmi < 40:
            print('Obese Class II')
        elif bmi >= 40:
            print('Obese Class III')
main()
