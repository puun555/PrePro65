'''Minesweeper CR:P'ปันปัน'''

def main():
    '''main'''

    # get variable
    height_in, width_in = input().split("x")
    width = int(width_in)
    height = int(height_in)
    numbomb = int(input())

    #get array
    arr1 = []

    #build array maping
    for i in range(height):
        arr1.append([])
        for j in range(width):
            arr1[i].append(0)
    #loops input possitions
    for _ in range(numbomb):
        row_in, col_in = input().split(',')
        row = int(row_in)
        col = int(col_in)
        # add "*" to the minebomb possition
        arr1[row][col] = '*'
        # loops check score around the minebomb
        for row1 in range(height):
            for col1 in range(width):
                # check if possition around the minebomb +1 to that possition
                if row-1 <= row1 <= row+1 and col-1 <= col1 <= col+1:
                    if arr1[row1][col1] != '*':
                        arr1[row1][col1] += 1
    #print the array
    for i in arr1:
        for j in i:
            print(j, end=' ')
        print()
main()
