#include <stdio.h>
#include <string.h>

void abertura()
{
    printf("*************************\n");
    printf("*     Jogo de Forca     *\n");
    printf("*************************\n\n");
}

void chuta(char chutes[26], int* tentativas)
{
    char chute;
    scanf(" %c", &chute);

    chutes[(*tentativas)] = chute;
    (*tentativas)++;
}

int jaChutou(int tentativas, char* chutes, char letra)
{
    int achou = 0;

    for (int j = 0; j < tentativas; j++) {
        if (chutes[j] == letra) {
            achou = 1;
            break;
        }
    }

    return achou;
}

void desenhaForca(char* palavraSecreta, int tentativas, char* chutes)
{
    for (int i = 0; i < strlen(palavraSecreta); i++) {

        int achou = jaChutou(tentativas, chutes, palavraSecreta[i]);

        if (achou) {
            printf("%c ", palavraSecreta[i]);
        } else {
            printf("_ ");
        }
    }
    printf("\n");
}

void escolhePalavra(char* palavraSecreta)
{
    sprintf(palavraSecreta, "MELANCIA");
}

int main()
{
    char palavraSecreta[20];

    int acertou = 0;
    int enforcou = 0;

    char chutes[26];
    int tentativas = 0;

    escolhePalavra(palavraSecreta);
    abertura();

    do {

        desenhaForca(palavraSecreta, tentativas, chutes);
        chuta(chutes, &tentativas);

    } while (!acertou && !enforcou);
}