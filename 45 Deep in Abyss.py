"""Deep In Abyss CR:P'Earth(นายศุภกร ดาราสุนทโร)"""
def get_curse(depth, decision):
    """ Get curse and name """
    curse = ""
    name = ""
    if depth <= 1350:
        name = "1st Layer : Edge of the Abyss"
        curse = "Light dizziness and nausea."
    elif depth <= 2600:
        name = "2nd Layer : Forest of Temptation"
        curse = "Intense nausea, headaches, and numbness of limbs."
    elif depth <= 7000:
        name = "3rd Layer : Great Fault"
        curse = "Vertigo combined with visual and auditory hallucinations."
    elif depth <= 12000:
        name = "4th Layer : The Goblets of Giants"
        curse = "Intense pain throughout the body and bleeding from every orifice."
    elif depth <= 13000:
        name = "5th Layer : Sea of Corpses"
        curse = "Complete sensory deprivation, confusion and self-harming behavior."
    elif depth <= 15500:
        name = "6th Layer : The Capital of the Unreturned"
        curse = "Loss of humanity or death, or under specific conditions, the Blessing."
    else:
        name = "7th Layer : The Final Maelstrom"
        curse = "Certain death."

    if decision == "DOWN":
        curse = "-"
    return name, curse

def show(name, layer_name, curse):
    """function print"""
    print("Name : %s" %name)
    print(layer_name)
    print("Curse : %s" %curse)

def main():
    """function main"""
    name_1 = input()
    depth_1 = int(input())
    decision_1 = input()
    name_2 = input()
    depth_2 = int(input())
    decision_2 = input()
    name_3 = input()
    depth_3 = int(input())
    decision_3 = input()

    first_layer, first_curse = get_curse(depth_1, decision_1)
    second_layer, second_curse = get_curse(depth_2, decision_2)
    third_layer, third_curse = get_curse(depth_3, decision_3)

    show(name_1, first_layer, first_curse)
    print("---")
    show(name_2, second_layer, second_curse)
    print("---")
    show(name_3, third_layer, third_curse)
main()
