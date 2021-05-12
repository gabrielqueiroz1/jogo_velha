#iniciamos as variáveis "core" do jogo da velha
X = "X"
O = "O"
VAZIO = " "

#iniciamos o tabuleiro com os 9 espaços "VAZIOS"
tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]
jogada = 0
# tabuleiro = [0, 1, 2,
#              3, 4, 5,
#              6, 7, 8]

#o jogo_valido precisa iniciar com "True" para que ele entre no nosso while
jogo_valido = True
#como ainda não temos vencedor, precisamos inciá-lo com False para que
#consigamos entrar no while e iniciar o jogo
vencedor = False

#iniciamos os dois jogadores com "vazio" porque ainda vamos escolher quem irá
#escolher "X" ou "O"
jogador1 = VAZIO
jogador2 = VAZIO
jog = 0

def tabuleiroAtualizado():
    for i in range(0, 9, 3):
        print(i, "|", i+1, "|", i+2, "      ",
              tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])

#perguntamos para o jogador a preferência dele em "X" ou "O"
while jogador1 != 'X' or jogador1 != 'O':
    jogador1 = input("Escolha X ou O: ").upper().strip()

    if jogador1 == X:
        jogador2 = O
        break
    if jogador1 == O:
        jogador2 = X
        break
    else:
        print("Digite uma das opções pedida.")

#representação do tabuleiro em números para que os jogadores tenham uma base
#de onde jogar
tabuleiroAtualizado()

while jogo_valido:
    jogada += 1
    jog += 1
    if jog > 2:
        jog = 1
    casa = int(input("Jogador(a){} -> Escolha onde jogar: ".format(jog)))
    while casa < 0 or casa > 8:
        print("Digite uma casa correta.")
        casa = int(input("Jogador(a){} -> Escolha onde jogar: ".format(jog)))

    if jogada % 2 == 1:
        if tabuleiro[casa] == VAZIO:
            tabuleiro[casa] = jogador1
        else:
            while tabuleiro[casa] != VAZIO:
                print("Essa casa já está ocupada. Escolha outra.")
                tabuleiroAtualizado()
                casa = int(input())
                if tabuleiro[casa] == VAZIO:
                    tabuleiro[casa] = jogador1
                    break
    if jogada % 2 == 0:
        if tabuleiro[casa] == VAZIO:
            tabuleiro[casa] = jogador2
        else:
            while tabuleiro[casa] != VAZIO:
                print("Essa casa já está ocupada. Escolha outra.")
                tabuleiroAtualizado()
                casa = int(input())
                if tabuleiro[casa] == VAZIO:
                    tabuleiro[casa] = jogador2
                    break

    tabuleiroAtualizado()

    # verificar se o jogo acabou
    # horizontal
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
            vencedor = tabuleiro[i]

    # vertical
    if not vencedor:
        for i in range(3):
            if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
                vencedor = tabuleiro[i]

    # diagonal
    if not vencedor:
        for i in range(0, 3, 2):
            if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
                vencedor = tabuleiro[i]

    if vencedor:
        jogo_valido = False
        print("Vencedor: ", vencedor)
    else:
        if not VAZIO in tabuleiro:
            jogo_valido = False
            print("Jogo empatou: Deu velha!")
