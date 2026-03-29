#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    printf("******************************************\n");
    printf("* Bem vindo ao nosso jogo de adivinhação *\n");
    printf("******************************************\n");

    int segundos = time(0);
    srand(segundos);

    int numeroGrande = rand();

    int numeroSecreto = numeroGrande % 100;
    int chute;
    int tentativas = 1;
    float pontos = 1000;

    int acertou = 0;

    int nivel;
    printf("Qual o nível de dificuldade?\n");
    printf("(1) Fácil (2) Médio (3) Difícil\n\n");
    printf("Escolha: ");
    scanf("%d", &nivel);

    int numeroDeTentativas;

    switch (nivel)
    {
    case 1:
        numeroDeTentativas = 20;
        break;
    case 2:
        numeroDeTentativas = 10;
        break;
    default:
        numeroDeTentativas = 5;
        break;
    }

    for (int i = 1; i <= numeroDeTentativas; i++)
    {

        printf("Tentativa %d\n", tentativas);
        printf("Qual é o seu chute? ");

        scanf("%d", &chute);
        printf("Seu chute foi %d\n", chute);

        if (chute < 0)
        {
            printf("Você não pode chutar números negativos!\n");
            continue;
        }

        acertou = (chute == numeroSecreto);
        int maior = chute > numeroSecreto;

        if (acertou)
        {
            break;
        }
        else if (maior)
        {
            printf("Seu chute foi maior que o número secreto\n");
        }
        else
        {
            printf("Seu chute foi menor que o número secreto\n");
        }

        tentativas++;

        float pontosPerdidos = abs(chute - numeroSecreto) / (float)2;
        pontos = pontos - pontosPerdidos;
    }

    printf("Fim de jogo!\n");

    if (acertou)
    {
        printf("Você ganhou!\n");
        printf("Você acertou em %d tentativas!", tentativas);
        printf("Total de pontos: %.1f\n", pontos);
    }
    else
    {
        printf("Você perdeu! Tente de novo!\n");
    }
}