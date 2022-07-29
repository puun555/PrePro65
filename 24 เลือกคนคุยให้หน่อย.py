'''find my gf'''
def gftype(type1, type2):
    '''gf type'''
    if (type1 == 'Calm' and type2 == 'Empathetic') \
        or (type2 == 'Calm' and type1 == 'Empathetic'):
        print('Ice')
    elif (type1 == 'Reliable' and type2 == 'Courageous') \
        or (type2 == 'Reliable' and type1 == 'Courageous'):
        print('Fern')
    elif (type1 == 'Optimistic' and type2 == 'Cheerful') \
        or (type2 == 'Optimistic' and type1 == 'Cheerful'):
        print('Bam')
    elif (type1 == 'Attractive' and type2 == 'Creative') \
        or (type2 == 'Attractive' and type1 == 'Creative'):
        print('Tangmo')
    elif (type1 == 'Cheerful' and type2 == 'Creative') \
        or (type2 == 'Cheerful' and type1 == 'Creative'):
        print('Mild')
    elif (type1 == 'Reliable' and type2 == 'Optimistic') \
        or (type2 == 'Reliable' and type1 == 'Optimistic'):
        print('Prae')
    elif (type1 == 'Calm' and type2 == 'Courageous') \
        or (type2 == 'Calm' and type1 == 'Courageous'):
        print('Dream')
    elif (type1 == 'Attractive' and type2 == 'Empathetic') \
        or (type2 == 'Attractive' and type1 == 'Empathetic'):
        print('Aom')

def main():
    '''main'''
    gftype1 = input().strip()
    gftype2 = input().strip()
    gftype(gftype1, gftype2)
main()
