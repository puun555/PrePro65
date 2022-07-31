"""Cr. P'pan"""
def main():
    """Drop Drop"""
    grade = float(input())
    if grade >= 2:
        print("I'm so happy.")
    elif grade >= 1:
        next_grade = 4 - grade
        print("%.2f" %next_grade)
    else:
        print("I'm so sad.")
main()