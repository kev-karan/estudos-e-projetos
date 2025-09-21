function alterarStatus(id) {
    const gameClicado = document.getElementById(`game-${id}`);
    const imagem = gameClicado.querySelector('.dashboard__item__img');
    const botao = gameClicado.querySelector('.dashboard__item__button, .dashboard__item__button--return');

    if (imagem.classList.contains('dashboard__item__img--rented')) {
        Devolver(imagem, botao);
    } else {
        imagem.classList.add('dashboard__item__img--rented');
        botao.classList.add('dashboard__item__button--return');
        botao.textContent = 'Devolver';
    }
}

function Devolver(imagem, botao) {
    if (confirm('Você deseja devolver o jogo?')) {
        imagem.classList.remove('dashboard__item__img--rented');
        botao.classList.remove('dashboard__item__button--return');
        botao.textContent = 'Alugar';
    } else {
        alert('Devolução do jogo cancelada!');
    }
}
