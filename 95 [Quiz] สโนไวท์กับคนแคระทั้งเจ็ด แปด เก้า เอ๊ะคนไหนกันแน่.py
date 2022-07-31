"""IG: few.pz [Quiz] สโนไวท์กับคนแคระทั้งเจ็ด แปด เก้า เอ๊ะคนไหนกันแน่ CR:N'นายพีรณัฐ หมัดสอ"""

def main():
    """ Main function """
    crewmates = [int(input()) for _ in range(9)]
    for imposter_a in crewmates:
        remaining_crewmates = [*crewmates]
        remaining_crewmates.remove(imposter_a)
        for imposter_b in remaining_crewmates:
            party = [*remaining_crewmates]
            party.remove(imposter_b)
            if sum(party) == 100:
                for i in party:
                    print(i)
                return
    print("ERROR")

main()
