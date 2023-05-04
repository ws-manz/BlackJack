# Blackjack
Este é um simples jogo de blackjack (21) criado em Python.

## Como Jogar
O objetivo do blackjack é vencer o dealer (banqueiro) obtendo uma mão total de cartas com um valor mais próximo de 21 do que a mão do dealer, sem ultrapassar 21.

O jogo começa com duas cartas para cada jogador, incluindo o dealer. As cartas do jogador são distribuídas de frente para cima, enquanto a primeira carta do dealer é distribuída de frente para cima e a segunda de frente para baixo.

Cada carta tem um valor de ponto. Cartas numéricas são valorizadas pelo seu número, cartas faciais (Rei, Rainha e Valete) têm um valor de 10 pontos e o Ás pode valer 1 ou 11, dependendo do valor que torna a mão mais próxima de 21.

Após receber suas duas primeiras cartas, o jogador pode optar por ficar com sua mão atual (stand) ou pedir mais cartas (hit) para tentar se aproximar de 21.

Se o jogador ultrapassar 21 pontos, ele perde automaticamente (bust).

Depois que o jogador ficar satisfeito com sua mão, é a vez do dealer jogar. O dealer irá revelar sua carta de baixo e, se a soma de suas cartas for inferior a 17, ele continuará a receber mais cartas até que sua mão total seja 17 ou mais.

Se o dealer ultrapassar 21 pontos, ele perde e o jogador ganha. Caso contrário, a mão do jogador é comparada com a do dealer e a mão mais próxima de 21 vence.

## Como Executar o Jogo
Certifique-se de ter o Python 3.x instalado em seu computador. Para jogar, basta baixar o arquivo blackjack.py e executá-lo no terminal com o seguinte comando:

```python
python blackjack.py
```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um Pull Request com melhorias ou correções. Para grandes mudanças, por favor, abra um issue primeiro para discutir o que você gostaria de mudar.

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
