from random import randint
from random import choice
from time import sleep
print('\033[1mMini game de RPG em python\033[m')

mercado = {'Poção de vida':5,'Armadura':15, 'Espada':20}

sua_vida = ini_vida = 100
cont_cura = game_over = moedas = 0
espada = escudo = cura = 0
fase = 1

nome = str(input('Digite seu nome: ')).title().strip()
print(' [1] Guerreiro/a \n [2] Arqueiro/a \n [3] Mago/Bruxa')
while True:
    tipo = int(input('Qual voçê quer ser? '))
    if tipo == 1:
        pers = 'Guerreiro/a'
        break
    elif tipo == 2:
        pers = 'Arqueiro/a'
        break
    elif tipo == 3:
        pers = 'Mago/Bruxa'
        break
    else:
        print('Resposta Invalida. Tente novamente')
sleep(0.5)

print('-='*25)
while True:
    inimigos = ['Dragão', 'Globin', 'Slime','Vampiro','Lobisomem']
    inimigo = choice(inimigos)
    print(f'''{pers} {nome}, apareceu um {inimigo} no caminho,
o que voçê vai fazer?''')
    sleep(2)

    while True:
        print('-='*25)
        print('''Escolha:
        [1] Atacar
        [2] Cura
        [3] Ver status
        [4] Loja
        [5] Fugir''')
        n = int(input('Qual sua escolha? '))

        if n == 1:
            seu_dano = randint(5, 40) + espada
            print('Voçê atacou seu inimigo')
            sleep(1)
            critico = randint(0, 10)
            if critico == 10:
                print('CRITICO')
                seu_dano += 30
            print(f'- Seu ataque deu {seu_dano} de dano -')
            sleep(1.5)
            ini_dano = randint(2 + fase + 4,15 + fase + 5) - escudo
            if critico == 0:
                print('Seu inimigo acertou um dano CRITICO')
                ini_dano += 30
            print(f'- O ataque inimigo deu {ini_dano} de dano em voçê -')
            sua_vida -= ini_dano
            ini_vida -= seu_dano
            sleep(1.5)
            if ini_vida <= 0:
                print('Voçê \033[1;32mVENCEU\033[m, Parábens')
                moedasFase = randint(1, 10)
                moedas += moedasFase
                print(f'Voçê recebeu {moedasFase} moedas por ter vencido o {inimigo}')
                sleep(1)
                fase += 1
                sua_vida = 100
                ini_vida = 100
                inimigos = ['Dragão', 'Globin', 'Slime', 'Vampiro', 'Lobisomem']
                inimigo = choice(inimigos)
                print('-='*25)
                print(f'{pers} {nome}, apareceu um {inimigo} na sua frente,\no que voçê vai fazer?')
                sleep(1.5)
            elif sua_vida <= 0:
                print('Voçê \033[4mMORREU\033[m.\033[1;31mGame over\033[m')
                game_over += 1
                break

        elif n == 2:
            if cura >= 1:
                cura = randint(10,40)
                print(f'- Voçê recuperou {cura} de vida -')
                sua_vida += cura
                cont_cura += 1
                cura -= 1
            elif cura <= 0:
                print('Voçê não possui cura \nCompre na loja')
            sleep(1.5)

        elif n == 3:
            print()
            print(f'{'STATUS':=^20}')
            print(f'Voçê: {pers} {nome}')
            print(f'Fase: {fase}')
            print(f'Inimigo: {inimigo}')
            print(f'Sua vida: {sua_vida}')
            print(f'Vida do inimigo: {ini_vida}')
            if fase > 1:
                print(f'Inimigos derrotados: {fase - 1}')
            print(f'Moedas: {moedas}')
            while True:
                resp = str(input('Digite "v" para voltar: ')).strip().lower()[0]
                if resp in 'v':
                    break
                print('ERRO! Digite apenas "v" para voltar')
            sleep(0.5)

        elif n == 4:
            print('>>> LOJA <<<')
            for i, (c, v) in enumerate(mercado.items()):
                print(f'[{i}] {c} {'-'*10} {v} moedas')
            while True:
                resp = str(input('Deseja comprar alguma coisa?[s/n] ')).strip().lower()[0]
                if resp in ['s','n']:
                    break
                print('ERRO!Por favor digite apenas "s" ou "n"')
            if resp == 'n':
                continue
            compra = int(input('O que voçê deseja comprar? '))
            mercadoria = list(mercado.items())
            item, preco = mercadoria[compra]
            if compra == 0:
                if moedas >= 5:
                    moedas -= 5
                    cura += 1
                    sleep(0.5)
                    print(f'Voçê comprou {item} por {preco} moedas')
                    sleep(0.5)
                else:
                    sleep(0.5)
                    print('Moedas insuficiente')
                    sleep(0.5)
            if compra == 1:
                if moedas >= 15:
                    moedas -= 15
                    escudo = 5
                    sleep(0.5)
                    print(f'Voçê comprou {item} por {preco} moedas')
                    sleep(0.5)
                else:
                    sleep(0.5)
                    print('Moedas insuficiente')
                    sleep(0.5)
            if compra == 2:
                if moedas >= 20:
                    moedas -= 20
                    espada = 10
                    sleep(0.5)
                    print(f'Voçê comprou {item} por {preco} moedas')
                    sleep(0.5)
                else:
                    sleep(0.5)
                    print('Moedas insuficiente')
                    sleep(0.5)

        elif n == 5:
            print('Voçê fugiu')
            t = str(input('Acabar o jogo por aqui?[S/N] ')).strip().upper()
            if t in 'S':
                game_over += 1
                break
            elif t in 'N':
                inimigos = ['Dragão', 'Globin', 'Slime', 'Vampiro', 'Lobisomem']
                inimigo = choice(inimigos)
                print(f'{pers} {nome} caminhando um {inimigo} aparece, o que voçê vai fazer?')
                sleep(2)

    if game_over == 1:
        print()
        print(f'{'ESTATÍSTICAS':=^30}')
        print(f'Morreu na fase: {fase}')
        if fase > 1:
            print(f'Inimigos derrotados: {fase - 1} ')
        print(f'Voçê usou a cura {cont_cura}x')
        print(f'Morreu com {moedas} moedas')
        break