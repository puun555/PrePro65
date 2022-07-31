"""Cr. P'pan"""
def main():
    """Ranking the scores"""
    num = list(map(int, input().split(",")))
    ans = []
    sortt = sorted(num)
    sortt.reverse()
    for i in num:
        ans.append((sortt.index(i))+1)
    print(*ans, sep=",")
main()
