<h1>VÍDEO POKER</h1>
<h3>Implementação de um jogo de vídeo poker para a disciplina de POO do ICMC-USP, cursada no ano de 2022</h3>
O video poker é um jogo de cartas em que o usuário interage com o computador,
fazendo apostas e tentando conseguir algumas combinações específicas (as mesmas
do poker normal) que lhe dão recompensas proporcionais ao valor que o jogador
apostou.
O baralho usado é um baralho convencional de 52 cartas, ordenadas de 2 até 10 e
depois J (valete), Q (dama), K (rei) e A (ás). Note que o A não serve como 1, ou
seja, ele é a maior carta da sequência e não a menor.
Cada jogo inicia com o jogador recebendo uma quantidade fixa de créditos (200
créditos). Cada rodada inicia com o jogador apostando um certo número de créditos,
maior que zero e menor ou igual ao número de créditos que possui. Feito isso, o
jogador recebe cinco cartas e deve tentar fazer uma das combinações que lhe paguem
os prêmios. Para isso, o jogador pode escolher trocar de zero a cinco cartas que
recebeu. Em seguida, pode trocar mais uma vez as cartas para alcançar alguma
combinação.
As combinações que premiam o jogador, e os respectivos valores são os seguintes:

<pre>
* Dois pares:                    1x aposta
* Trinca:                        2x aposta
* Straight:                      5x aposta
* Flush:                        10x aposta
* Full-House:                   20x aposta
* Quadra:                       50x aposta
* Straight Flush:              100x aposta
* Royal Straight Flush:        200x aposta
</pre>

O jogo acaba quando o jogador decidir não apostar mais (apostar uma quantidade de créditos igual a zero).

<h3>Como rodar o jogo:</h3>
Em seu terminal, acesse o diretório atual e rode o arquivo Poker.py usando o Python. Digite o comando ```python Poker.py```.

Certifique-se de usar as versões mais recentes do Python. Você pode verificar a sua digitando ```python --version``` no terminal. A versão
utilizada durante a produção e teste desta aplicação foi ```Python 3.8.10```.

**Não exclua, modifique ou migre nenhum arquivo deste diretório!**