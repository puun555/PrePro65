"""[Quiz] Squid game 2 CR:P'Fern"""
def Last_Person(inf):
    """josephus"""
    person = [x for x in range(1, inf+1)]
    x = 0
    i = 1
    while len(person) > 1:
        if x == len(person)-1:
            print("Round %d : Person %d killed person %d" %(i, person[x], person[0]))
            person.pop(0)
            x = 0
            i = i+1
        elif x == len(person)-2:
            print("Round %d : Person %d killed person %d" %(i, person[x], person[x+1]))
            person.pop(x+1)
            x = 0
            i = i+1
        else:
            print("Round %d : Person %d killed person %d" %(i, person[x], person[x+1]))
            person.pop(x+1)
            x = x+1
            i = i+1
    print("Person", person[x], "is the winner")
Last_Person(int(input()))
