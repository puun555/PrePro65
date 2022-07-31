'''Mala xiang guo'''
def main():
    '''main'''
    ingrediant = ['celery stalks', 'carrots', 'potatoes',\
'mushrooms', 'tofu', 'lotus root', 'cabbage', 'instant noodles',\
'glass noodle', 'wonton', 'beef', 'pork loin', 'chicken', 'fish balls',\
'cheese ball', 'octopus', 'fish', 'shrimp', 'mussels']
    spicy_lv = ['Mild', 'Medium', 'Hot', 'Extra hot']
    arr_order = []

    #condition
    howspicy = 0
    con = True
    con1 = False

    # get input
    while True:
        order = input()
        if order.lower() == 'stop':
            break
        if not order.isnumeric():
            arr_order.append(order.lower())
            con1 = True
        else:
            howspicy += int(order)
            con1 = False

    # check order
    for i in arr_order:
        if i in ingrediant and con == True:
            con = True
        else:
            con = False

    #print condition
    if arr_order == []:
        print("Huh? you didn't order anything!")
    elif not con:
        print("Get out!")
    elif howspicy == 0 or con1 == True:
        print('Please choose a spicy level!')
    elif con:
        print("%s Mala xiang guo is here."%spicy_lv[howspicy-1])
main()
