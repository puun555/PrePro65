'''PeterPanframe'''
def main():
    '''main'''
    text = input()
    statictext1 = ""
    statictext2 = ""
    ptext = ""
    counter = 1
    for j in text:
        if counter%3 == 0:
            statictext1 += "..◊."
            statictext2 += ".◊.◊"
            ptext += "◊."+j+"."
        elif counter%3 == 1 and counter >= 3:
            statictext1 += "..♦."
            statictext2 += ".♦.♦"
            ptext += "◊."+j+"."
        else:
            statictext1 += "..♦."
            statictext2 += ".♦.♦"
            ptext += "♦."+j+"."
        counter += 1
    if len(text)%3 == 0:
        ptext += '◊'
    else:
        ptext += '♦'

    print(statictext1+'.')
    print(statictext2+'.')
    print(ptext)
    print(statictext2+'.')
    print(statictext1+'.')
main()
