'''fastserver'''
def sec(server, sec1):
    '''tosec'''
    if sec1 == "Millisecond":
        return server/1000
    elif sec1 == "Microsecond":
        return server/1000000
    elif sec1 == "Nanosecond":
        return server/1000000000
    elif sec1 == "Picosecond":
        return server/1000000000000

def main(server1, s1sec, server2, s2sec):
    '''main'''
    fasts1 = sec(server1, s1sec)
    fasts2 = sec(server2, s2sec)

    if fasts1 < fasts2:
        print("Server A, %.6f second\nFaster than server B , %d times"%(fasts1, fasts2//fasts1))
    elif fasts1 > fasts2:
        print("Server B, %.6f second\nFaster than server A , %d times"%(fasts2, fasts1//fasts2))
    else:
        print("equal")
main(int(input()), input(), int(input()), input())
