// Isso é um comentário.

alert('Bem-vindo ao jogo do número secreto!');
let dificuldade = prompt('Escolha a dificuldade: 1 para fácil, 2 para médio e 3 para difícil.');
let nivelDificuldade;
if (dificuldade == 1) {
    nivelDificuldade = 10;
} else {
    if (dificuldade == 2) {
        nivelDificuldade = 100;
    } else {
        nivelDificuldade = 1000;
    }
}

let numeroSecreto = parseInt(Math.random() * nivelDificuldade + 1);
console.log(numeroSecreto);
console.log(nivelDificuldade);
let chute;
let tentativas = 1;

while (chute != numeroSecreto) {
    chute = prompt(`Escolha um número entre 1 e ${nivelDificuldade}`);
    if (chute == numeroSecreto) {
        break;
    } else {
        if (chute > numeroSecreto) {
            alert(`O número secreto é menor que ${chute}.`);
        } else {
            alert(`O número secreto é maior que ${chute}.`);
        }
        tentativas++;
    }
}

let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';

alert(
    `Isso aí! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`
);
