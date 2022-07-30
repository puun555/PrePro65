'''	วันจันทร์ฉันคิดถึงเธออยู่ วันอังคารไปหาได้ไหม'''
def main():
    '''main'''
    sec = int(input())
    anssec = sec%60
    minutes = sec//60
    ansminutes = minutes%60
    hourr = minutes//60
    anshourr = hourr%24
    ansdays = hourr//24
    print("%02d:%02d:%02d:%02d"%(ansdays, anshourr, ansminutes, anssec))
main()
