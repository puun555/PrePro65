'''คณิตศาสตร์เข้าใจยากแต่รักเธอมากเข้าใจไหม CR:นายชนัญญู ลิ้มเจริญ'''
def convert(text):
    '''convert'''
    new = ''
    for var in range(1, len(text)-1):
        new += text[var]
    return new.split(', ')

def main():
    '''main'''
    lsa = input()
    lsa = convert(lsa)
    lsa.reverse()
    lsc = []
    math = 0
    math2 = 0
    for num in range(len(lsa)):
        count = 0
        math = 0
        for var in range(-num-1, 0):
            if num == 0:
                math = int(lsa[-1])
                break
            elif count == 0:
                math2 = 1/int(lsa[var])
            else:
                math = int(lsa[var]) + math2
                math2 = 1/math
            count += 1
        lsc.append(round(math, 6))
    print(lsc)
main()
