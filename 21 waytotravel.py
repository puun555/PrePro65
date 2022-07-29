"""Way to travelling"""
def dis(distance):
    '''วัดระยะทางไปแบบไหนดี'''
    if distance >= 300:
        return 'Private jet'
    elif distance >= 20:
        return 'Car'
    elif distance >= 1:
        return 'Motorcycle'
    elif distance < 0:
        return "Error"
    else:
        return 'Walk'

def main():
    '''main'''
    weather = input()
    how_im = input()
    distance = float(input())
    if weather == 'rainy':
        if how_im == 'important':
            print(dis(distance))
        else:
            print('Not go')
    else:
        print(dis(distance))
main()
