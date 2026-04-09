#include "forca.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char palavraSecreta[20];
char chutes[26];
int chutesDados = 0;

void abertura()
{
    printf("/*****************/\n");
    printf("/* Jogo de Forca */\n");
    printf("/*****************/\n\n");
}

void chuta()
{
    char chute;
    printf("Qual letra? ");
    scanf(" %c", &chute);

    chutes[chutesDados] = chute;
    chutesDados++;
}

int jaChutou(char letra)
{
    int achou = 0;
    for (int j = 0; j < chutesDados; j++) {
        if (chutes[j] == letra) {
            achou = 1;
            break;
        }
    }

    return achou;
}

void desenhaForca()
{

    printf("Voce ja deu %d chutes\n", chutesDados);

    for (int i = 0; i < strlen(palavraSecreta); i++) {

        if (jaChutou(palavraSecreta[i])) {
            printf("%c ", palavraSecreta[i]);
        } else {
            printf("_ ");
        }
    }
    printf("\n");
}

void adicionaPalavra()
{
    char quer;

    printf("Voce deseja adicinar uma nova palavra no jogo? (S/N)");
    scanf(" %c", &quer);

    if (quer == 'S' || quer == 's') {
        char novaPalavra[20];
        printf("Qual a nova palavra? ");
        scanf("%s", novaPalavra);

        FILE* f;

        f = fopen("palavras.txt", "r+");
        if (f == 0) {
            printf("Desculpe, banco de dados nao disponivel\n\n");
            exit(1);
        }

        int qtd;
        fscanf(f, "%d", &qtd);
        qtd++;

        fseek(f, 0, SEEK_SET);
        fprintf(f, "%d", qtd);

        fseek(f, 0, SEEK_END);
        fprintf(f, "\n%s", novaPalavra);

        fclose(f);
    }
}

void escolhePalavra()
{
    FILE* f;
    f = fopen("palavras.txt", "r");
    if (f == 0) {
        printf("Desculpe, banco de dados nao disponivel\n\n");
        exit(1);
    }

    int qtdDePalavras;
    fscanf(f, "%d", &qtdDePalavras);

    srand(time(0));
    int randomico = rand() % qtdDePalavras;

    for (int i = 0; i <= randomico; i++) {
        fscanf(f, "%s", palavraSecreta);
    }

    fclose(f);
}

int acertou()
{
    for (int i = 0; i < strlen(palavraSecreta); i++) {
        if (!jaChutou(palavraSecreta[i])) {
            return 0;
        }
    }
    return 1;
}

int enforcou()
{
    int erros = 0;
    for (int i = 0; i < chutesDados; i++) {
        int existe = 0;
        for (int j = 0; j < strlen(palavraSecreta); j++) {
            if (chutes[i] == palavraSecreta[j]) {
                existe = 1;
                break;
            }
        }
        if (!existe) {
            erros++;
        }
    }
    return erros >= 5;
}

int main()
{
    abertura();
    escolhePalavra();

    do {

        desenhaForca();
        chuta();

    } while (!acertou() && !enforcou());

    adicionaPalavra();
}