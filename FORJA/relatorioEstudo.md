# **Relatório de Estudos | FORJA Select 25.2**

> Este relatório deve ser preenchido por cada equipe para comprovar o aprendizado realizado durante a **Etapa 2 - Estudo** do processo seletivo.  
> O objetivo é registrar o que foi estudado, o que foi aprendido e como o conteúdo pode contribuir para o desenvolvimento do jogo.

---

## 👥 **Equipe**

**Nome da equipe:**  Arcádia  
**Nome do jogo:**  Ismália  
**Integrante:**  Kelwin Karan Leal Silva  
**Email:**  <kkls@cesar.school>

---

## 🎯 **Tema do Estudo**

Nesse estudo, utilizarei a formação "[Desenvolvendo Jogos 2D com Unity](https://www.alura.com.br/formacao-desenvolvendo-jogos-2d-unity)" da plataforma Alura, nessa formação vou aprender:

- A criar jogos 2D completos e funcionais;

- Entender como aplicar física, áudio e animações dentro de um jogo;

- Aprender boas práticas de programação e padrões de projetos utilizados na área;

- Desenvolver habilidades práticas na Unity, criando um jogo desde a implementação das primeiras mecânicas até o polimento final.

---

## 📚 **Materiais Utilizados**

- [Get Started with Unity: In-Editor Tutorial](https://learn.unity.com/tutorial/get-started-with-unity-in-editor-tutorial) — Unity Learn  

- [C# language documentation](https://learn.microsoft.com/en-us/dotnet/csharp/) — Microsoft

- [Unity: criando um jogo metroidvania 2D](https://www.alura.com.br/curso-online-unity-criando-jogo-metroidvania-2d) — Alura  

- [Unity: criando menus, coletáveis e batalha final em um jogo 2D](https://www.alura.com.br/curso-online-unity-criando-menus-coletaveis-batalha-final-jogo-2d) — Alura  

> Dica: inclua links sempre que possível.

---

## 💡 **Principais Aprendizados**

Liste os **tópicos mais relevantes** ou **conceitos que você aprendeu** durante o estudo.  
Podem ser resumos, insights, anotações ou observações práticas.

1. Estrutura e Organização do Projeto

    - Criação e organização de GameObjects: compreender a hierarquia da cena e a importância de estruturar objetos logicamente.

    - Prefabs: criação de objetos pré-fabricados para padronizar e agilizar a produção (inimigos, coletáveis, chefões etc).

    - Importação e gerenciamento de assets: manter uma estrutura limpa de pastas, separando scripts, sprites, animações e sons.

2. Sistema de Input e Controle do Jogador

    - Configuração do novo Input System: mapeamento profissional e flexível dos controles.

    - Movimentação e física: uso de Rigidbody2D e Time.deltaTime para movimento fluido e frame independent.

    - Pulo e verificação de chão: lógica de detecção de colisão e controle de estados de movimento.

    - Obs: Time.deltaTime garante que o personagem se mova com a mesma velocidade em qualquer máquina, essencial para desempenho consistente.

3. Gerenciamento do Jogo

    - Game Manager: script central para gerenciar lógica global (pontuação, estados de jogo, vitória, derrota).

    - Core Game Loop: ciclo principal do jogo, controlando início, jogo ativo, vitória e reinício.

    - FindObjectsOfType: usado para encontrar e manipular todos os objetos de um tipo específico (como coletáveis).

4. Inimigos e IA

    - Criação e controle de inimigos: movimentação, detecção do jogador e comportamento reativo.

    - Uso de RequireComponent: garante que scripts essenciais (como Rigidbody2D e Collider2D) estejam presentes.

    - Máquina de estados (State Machine): definição de comportamentos e transições, especialmente para o chefão.

5. Combate e Interações

    - Sistema de ataque e dano: implementação da troca de dano entre player e inimigos.

    - Script de vida reutilizável: componente genérico para qualquer entidade que possa sofrer dano.

    - Partículas e efeitos visuais: sistema de partículas ativado via script para dar feedback ao jogador.

    Obs: separar scripts como vida e dano permite reutilização e consistência em diferentes personagens e objetos.

6. Arte, Animação e Tilemap

    - Animator Controller: controle de estados de animação (idle, andar, ataque, morte).

    - Transições de animações: sincronização suave entre estados.

    - Criação de mapas com Tilemap: construção modular e eficiente de cenários 2D.

    - Tile Colliders e Physics Materials: ajustes de colisão para fluidez na movimentação.

7. Áudio e Feedback Sonoro

    - Sistema de som escalável: uso de Audio Mixer e grupos de som.

    - Sons de ambiente (BGM) e efeitos sonoros (SFX): camadas sonoras para imersão.

    - Exposição de parâmetros de áudio via script: controle dinâmico de volumes e efeitos.

8. Interface e Fluxo do Jogo

    - Criação de menus e HUD com Canvas: telas de início, opções, vitória e derrota.

    - Botões e eventos UI: manipulação de botões com eventos profissionais.

    - Exibição dinâmica de coletáveis: atualização da interface conforme o progresso do jogador.

    - Tela de créditos e retorno ao menu: fechamento completo do ciclo de gameplay.

9. Câmera e Cinemática

    - Cinemachine: câmera dinâmica que segue o jogador de forma fluida.

    - Configuração de limites e suavização de movimento — evita cortes bruscos e mantém a imersão.

10. Otimização e Boas Práticas

    - Reutilização de assets e scripts — reduz redundâncias e melhora desempenho.

    - Correção de colisões do Tilemap — solução de problemas comuns em plataformas 2D.

    - Uso de Physics Material 2D — evita que o personagem “grude” em paredes.

    - Eventos e triggers otimizados — execução de comportamentos apenas quando necessário.

---

## 🧩 **Amostras ou Evidências do Estudo**

Inclua **prints, links, trechos de código, protótipos ou arquivos** que demonstrem o aprendizado.  
O que for imagem ou vídeo, coloque no Drive, deixe público e compartilhe o link aqui.

> Exemplo:
>
> - Capturas de tela do projeto em execução
> - Link para o repositório ou protótipo
> - GIFs mostrando o funcionamento

[![Certificado: Formação Desenvolva jogos com Unity](https://github.com/kev-karan/estudos-e-projetos/blob/main/FORJA/Kelwin%20Karan%20Leal%20Silva%20-%20Forma%C3%A7%C3%A3o%20Desenvolva%20jogos%20com%20Unity%20-%20Alura_page-0001.jpg?raw=true)](https://cursos.alura.com.br/degree/certificate/abbd70fb-9037-4258-b57c-7d614b5d9bfc?lang=pt_BR)

[Jogo: Kev web build](https://play.unity.com/en/games/6b5f9a99-41de-4cb5-9da5-c98bfb84a1f2/kev-web-build)

[Jogo: A Vingança de Zorgon 2D](https://kevkaran.itch.io/a-vinganca-de-zorgon-2d)

~~~markdown
![Exemplo de Tilemap](link-da-imagem-ou-gif)
~~~

---

## ❓ **Dúvidas e Pontos a Revisar**

Registre dúvidas ou tópicos que ainda geram dificuldade.  
Isso ajuda a FORJA a direcionar mentorias futuras.

- Diferença entre Awake(), Start() e Update() e em que casos cada um é ideal.

- Como organizar prefabs e assets para projetos maiores.

- Persistência de dados entre cenas (pontuação, progresso, configurações).

~~~markdown
- Como otimizar o uso de colisores em Tilemaps grandes?
- É possível trocar o Tile Palette em tempo de execução?
~~~

---

## 🔁 **Próximos Passos**

Liste o que você pretende estudar ou praticar a seguir.  
Isso mostra intenção de continuidade e evolução.

- Aprender fundamentos e práticas em programação Orientada a Objetos em C#.

- Estudar Level Design: ritmo, progressão, dificuldade e posicionamento de itens e inimigos.

- Como encontrar boas ideias para Jogos, mecanicas, Loops de gameplay, etc.

- Como fazer prototipagem de forma rápida e eficiente para testar ideias.

~~~markdown
- Explorar iluminação 2D na Unity;
- Criar variações de tiles animados;
- Estudar sobre colisões compostas.
~~~
