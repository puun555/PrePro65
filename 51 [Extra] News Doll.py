"""Prepro"""
def move(posi, kum):
    """Yakmakkkkkkkk"""
    if kum == "Stop":
        print(posi)
    elif posi == 1 and (kum == "East"  or kum == "South"):
        move(((2*(kum == "East"))+(3*(kum == "South"))), input().capitalize())
    elif posi == 2 and (kum == "West" or kum == "South"):
        move(((1*(kum == "West"))+(4*(kum == "South"))), input().capitalize())
    elif posi == 3 and (kum == "East" or kum == "North"):
        move(((4*(kum == "East"))+(1*(kum == "North"))), input().capitalize())
    elif posi == 4 and (kum == "West" or kum == "North"):
        move(((3*(kum == "West"))+(2*(kum == "North"))), input().capitalize())
    else:
        move(posi, input().capitalize())
def main():
    """rubkanaa"""
    pos = int(input())
    kum = input().capitalize()
    move(pos, kum)
main()
