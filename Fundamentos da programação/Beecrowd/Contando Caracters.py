maiorPalavra = "" 

while True:
    frase = input().strip()
    if frase == "0":
        break

    palavras = frase.split()
    tamanhos = []

    for p in palavras:
        tamanhos.append(str(len(p)))

        if len(p) >= len(maiorPalavra):
            maiorPalavra = p

    print('-'.join(tamanhos))

print(f"\nThe biggest word: {maiorPalavra}")