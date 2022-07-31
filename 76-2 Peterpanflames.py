"""PeterPanflames CR:P'ทิว(นายธีระวัฒน์ แสงจันทร์)"""
def outside(i, long):
    """Hello My Code"""
    line = ""
    for j in range(1, long+1):
        j += 1
        # line+=str(j)
        if j%12 == 0:
            line += '◊'
        elif j%4 == 0 and j%12 != 0:
            line += '♦'
        else:
            line += '.'
    if i == 1:
        line += '\n'
    return line
def inside(long):
    """Hello My Code"""
    line = ""
    for j in range(1, long+1):
        # line+=str(j)
        if j%2 == 0:
            if (j+2)%12 == 0 or j%12 == 0:
                line += '◊'
            elif (j+2)%12 != 0 or j%12 != 0:
                line += '♦'
        else:
            line += '.'
    line += '\n'
    return line
def main():
    """Hello Prepro"""
    word = input()
    long = (len(word)*5)-len(word)+1
    line = ''
    for i in range(6):
        if i == 1 or i == 5:
            line += outside(i, long)
        if i == 2 or i == 4:
            line += inside(long)
        if i == 3:
            index = 0
            for j in range(1, long+1):
                if j%2 != 0:
                    if (j == 1) or (len(word) <= 2 and j == 9) or (j == long and long%3 == 0):
                        line += '♦'
                    elif (j+1)%4 != 0:
                        if (j+3)%12 == 0 or (j-1)%12 == 0:
                            line += '◊'
                        elif(j+3)%12 != 0 or (j-1)%12 != 0:
                            line += '♦'
                    elif (j+1)%4 == 0:
                        line += word[index]
                        index += 1
                else:
                    line += '.'
            line += '\n'
    print(line)
main()
