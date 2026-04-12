while True:
    try:
        N = int(input())
        entrada = input().split()
        
        votos = 0
        for x in entrada:
            votos += int(x)
        
        if votos >= 2 * N / 3:
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break
