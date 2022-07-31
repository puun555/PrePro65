"""ig chulnwza Derivative CR:นายชยธร ชูอ่อน"""
def main():
    """main"""
    inp, count = input().split(','), 0
    inp1, diffed = [], []
    for i in inp:
        inp1.append((count, int(i)))
        count += 1
    for j in inp1:
        diffed.append((j[0]-1, j[1]*j[0]))
    output = []
    count = 0
    for row in diffed:
        if row[0] != count:
            continue
        else:
            output.append(row[1])
            count += 1
    while len(output) != len(inp1):
        output.append(0)
    print(output)
main()
