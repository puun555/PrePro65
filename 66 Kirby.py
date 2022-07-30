"""KIRBY CR:นายชญานนท์ สุภากิจ"""
def power(job, enemy, myhealth, count):
    """Calculate Health and ATK"""
    myatk = (job == "sword")*4+(job == "magic")*2+(job == "sleep")*0+(job == "master")*9
    yourhealth = (enemy == "waddle dee")*2+(enemy == "laser ball")*3+\
    (enemy == "waddle doo")*5+(enemy == "heal" or enemy == "none")*0
    youratk = (enemy == "waddle dee")*1+(enemy == "laser ball")*2+\
    (enemy == "waddle doo")*3+(enemy == "heal")*-2+(enemy == "none")*0
    if youratk >= myhealth or (youratk < myhealth and myatk < yourhealth):
        name = ""
    elif youratk < myhealth and myatk >= yourhealth:
        if enemy != "none" and enemy != "heal":
            count += 1
        name = enemy
    return name, myhealth - youratk, count

def fprint(name, health, count):
    """Print"""
    print("------------")
    if name != "" and name != "none" and name != "heal":
        print("- %s had defeated -" %name)
    print("%d HP left" %health)
    if name == "" and health <= 0:
        print("GameOver!\nYou had defeated %d enemies" %count)
    elif name == "none":
        print("Kirby won!\nYou had defeated %d enemies" %count)
    print("------------")

def main():
    """Main"""
    health = int(input())
    count = 0
    while health > 0:
        job = input().lower()
        enemy = input().lower()
        name, health, count = power(job, enemy, health, count)
        fprint(name, health, count)
        if enemy == "none":
            break
main()
