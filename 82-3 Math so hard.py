'''คณิตศาสตร์เข้าใจยากแต่รักเธอมากเข้าใจไหม CR:นายธนกฤต ทรัพย์ประสิทธิ์'''
def main(hector):
    '''main'''
    mat = convert_string(hector)
    mat.insert(0, 0)
    first_word = mat[1]
    word_all = len(mat)
    word_all += 0
    ans = [mat[1]]
    for i in range(2, word_all):
        temp = calc(mat[i-1], mat[i])
        for j in range(i-2, 0, -1):
            temp = calc(mat[j], temp)
        ans.append(round(temp, 6))
    ans[0] = int(first_word)
    print(ans)

def calc(hector, lalo):
    '''You could've shut your mouth, cooked, and made as much money as you ever needed.'''
    ding = hector + (1/lalo)
    return ding

def convert_string(gusfring):
    """Jesse!!!"""
    mat = []
    gus = string_to_list(gusfring)
    ###convert first char###
    mat.append(float(string_replace(gus[0], 0)))
    for i in range(1, len(gus)-1):
        mat.append(float(gus[i]))
    mat.append(float(string_replace(gus[len(gus)-1], len(gus))))
    return mat

def string_replace(string, gusfring):
    '''Shutup Walter'''
    if gusfring == 0:
        return string[1::]
    else:
        return string[:-1:]

def string_to_list(string):
    '''Goodbye Walter'''
    saulgoodman = list(string.split(", "))
    return saulgoodman

main(input())