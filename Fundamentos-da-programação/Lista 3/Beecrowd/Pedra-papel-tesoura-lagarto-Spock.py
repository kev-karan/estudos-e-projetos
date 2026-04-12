c = int(input())

for x in range(c):
    rajesh, sheldon = input().split()

    if rajesh == sheldon:
        print("empate")
    else:
        if rajesh == "tesoura":
            if sheldon == "papel" or sheldon == "lagarto":
                print("rajesh")
            else:
                print("sheldon")

        elif rajesh == "papel":
            if sheldon == "pedra" or sheldon == "spock":
                print("rajesh")
            else:
                print("sheldon")

        elif rajesh == "pedra":
            if sheldon == "tesoura" or sheldon == "lagarto":
                print("rajesh")
            else:
                print("sheldon")

        elif rajesh == "spock":
            if sheldon == "tesoura" or sheldon == "pedra":
                print("rajesh")
            else:
                print("sheldon")

        elif rajesh == "lagarto":
            if sheldon == "spock" or sheldon == "papel":
                print("rajesh")
            else:
                print("sheldon")
