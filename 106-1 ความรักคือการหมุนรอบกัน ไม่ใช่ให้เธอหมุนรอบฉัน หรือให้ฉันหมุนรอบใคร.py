'''[Onsite Day 2] ความรักคือการหมุนรอบกัน ไม่ใช่ให้เธอหมุนรอบฉัน หรือให้ฉันหมุนรอบใคร'''
def deg180nflip(matrix):
    '''sdsdsdsdsd'''
    for i in range(len(matrix)):
        matrix[i].reverse()
    for i in matrix:
        for j in i:
            print(j, end='')
        print()
def deg90(matrix):
    '''sdsdsdsdsd'''
    for i in range(len(matrix[0])):
        for j in range(len(matrix)-1, -1, -1):
            print(matrix[j][i], end='')
        print()
def main():
    '''main'''
    deg_s = input().lower()
    num = int(input())
    matrix = []
    for i in range(num):
        text = input()
        matrix.append([])
        for j in text:
            matrix[i].append(j)
    if len(matrix) > 1:
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                return print('Invalid size')
    if deg_s == '90':
        deg90(matrix)
    elif deg_s == '180':
        matrix.reverse()
        deg180nflip(matrix)
    elif deg_s == 'flip':
        deg180nflip(matrix)
main()
