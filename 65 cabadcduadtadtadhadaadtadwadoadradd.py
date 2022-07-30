'''	cabadcduadtadtadhadaadtadwadoadradd '''
def main():
    '''main'''
    text = input()
    puun = text
    while True:
        wordtocut = input()
        if not wordtocut in text:
            break
        while True:
            text = puun
            if not wordtocut in puun:
                break
            else:
                puun = text.replace(wordtocut, "")
    print(puun)
main()
