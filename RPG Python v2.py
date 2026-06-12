from random import randint
from random import choice
from time import sleep

minha_vida = ini_vida = 100
game_over = moedas = 0
espada = escudo = cura = 0
cont_cura = tot_cura = cont_escudo = cont_espada = 0
fase = 1

print('\033[1mMini game de RPG em python\033[m')
nome = str(input('Digite seu nome: ')).title().strip()

def l():
    print('-=' * 25)
def personagem():
    print(' [1] Guerreiro/a \n [2] Arqueiro/a \n [3] Mago/Bruxa')
    while True:
        tipo = str(input('Qual você quer ser? '))
        if tipo == '1':
            pers = 'Guerreiro/a'
            break
        elif tipo == '2':
            pers = 'Arqueiro/a'
            break
        elif tipo == '3':
            pers = 'Mago/Bruxa'
            break
        else:
            print('ERRO! Digite apenas as opções informadas')
    sleep(0.5)
    return pers
pers = personagem()
def ql_inimigo():
    l()
    inimigos = ['Dragão', 'Goblin', 'Slime', 'Vampiro', 'Lobisomem']
    inimigo = choice(inimigos)
    print(f'''{pers} {nome}, apareceu um {inimigo} no caminho,
o que você vai fazer?''')
    sleep(1)
    return inimigo
def menu():
    l()
    print('''Escolha:
    [1] Atacar
    [2] Cura
    [3] Ver status
    [4] Loja
    [5] Fugir''')
    n = str(input('Qual sua escolha? '))
    if n in ['1','2','3','4','5']:
        n = int(n)
    else:
        print('ERRO! Digite apenas os números que estão no menu.')
    return n
def meu_ataque():
    global ini_vida
    meu_dano = randint(5, 40) + espada
    print('Você atacou seu inimigo')
    sleep(1)
    meu_critico = randint(0, 10)
    if meu_critico == 10:
        print('CRITICO')
        meu_dano += 30
    print(f'- Seu ataque deu {meu_dano} de dano -')
    ini_vida -= meu_dano
    sleep(0.6)
    return meu_dano, meu_critico, ini_vida
def ata_inimigo():
    global minha_vida
    ini_dano = randint(9 + (fase * 2), 14 + (fase *6)) - escudo
    if ini_dano < 0:
        ini_dano = 0
    ini_critico = randint(0,10)
    if ini_critico == 0:
        print('Seu inimigo acertou um dano CRITICO')
        ini_dano += 30
    print(f'- O ataque inimigo deu {ini_dano} de dano em você -')
    minha_vida -= ini_dano
    sleep(1)
    return minha_vida, ini_critico
def verificacao():
    global minha_vida, ini_vida, fase, moedas, inimigo
    if ini_vida <= 0:
        print('Você \033[1;32mVENCEU\033[m, Parabéns')
        moedas_fase = randint(5, 15)
        moedas += moedas_fase
        print(f'Você recebeu {moedas_fase} moedas por ter vencido o {inimigo}')
        sleep(1)
        fase += 1
        minha_vida = 100
        ini_vida = 100
        inimigo = ql_inimigo()
    return moedas, fase
def curar():
    global cura, minha_vida, cont_cura, tot_cura
    if cont_cura >= 1:
        cura = randint(18, 40)
        print(f'- Você recuperou {cura} de vida -')
        minha_vida += cura
        tot_cura += 1
        cont_cura -= 1
    elif cura <= 0:
        print('Você não possui cura \nCompre na loja')
    sleep(1.5)
    return cura, minha_vida, cont_cura
def status():
    print()
    print(f'{'STATUS':=^25}')
    print(f'Você: {pers} {nome}')
    print(f'Fase: {fase}')
    print(f'Inimigo: {inimigo}')
    print(f'Sua vida: {minha_vida}')
    print(f'Vida do inimigo: {ini_vida}')
    if fase > 1:
        print(f'Inimigos derrotados: {fase - 1}')
    print(f'Moedas: {moedas}')
    print(f'Poções de cura: {cont_cura}')
    print(f'Escudos: {cont_escudo} ---> +{escudo} de defesa')
    print(f'Espadas: {cont_espada} ---> +{espada} de dano')
    print(f'{'':=^25}')
    while True:
        resp = str(input('Digite "v" para voltar: ')).strip().lower()
        if resp == 'v':
            break
        print('ERRO! Digite apenas "v" para voltar')
    sleep(0.5)
def loja():
    global moedas, cura, cont_cura, escudo, espada, cont_escudo, cont_espada
    print('>>> LOJA <<<')
    mercado = {'Poção de vida': 5, 'Armadura': 8, 'Espada': 20}
    for contador, (item, valor) in enumerate(mercado.items()):
        print(f'[{contador}] {item} {'-' * (25 -  (len(item)))} {valor} moedas')
    while True:
        resp = str(input('Deseja comprar alguma coisa?[s/n] ')).strip().lower()[0]
        if resp in ['s', 'n']:
            break
        print('ERRO!Por favor digite apenas "s" ou "n"')
    if resp == 's':
        while True:
            compra = str(input('O que você deseja comprar? '))
            mercadoria = list(mercado.items())
            if compra in ['0','1','2']:
                compra = int(compra)
                item, valor = mercadoria[compra]
                break
            print('ERRO! Digite apenas as opções informadas')
        if compra == 0:
            if moedas >= 5:
                moedas -= 5
                cont_cura += 1
                sleep(0.5)
                print(f'Você comprou {item} por {valor} moedas')
                sleep(0.5)
            else:
                sleep(0.5)
                print('Moedas insuficiente')
                sleep(0.5)
        elif compra == 1:
            if moedas >= 8:
                moedas -= 8
                escudo += 5
                cont_escudo += 1
                sleep(0.5)
                print(f'Você comprou {item} por {valor} moedas')
                sleep(0.5)
            else:
                sleep(0.5)
                print('Moedas insuficiente')
                sleep(0.5)
        elif compra == 2:
            if moedas >= 20:
                moedas -= 20
                espada += 10
                cont_espada += 1
                sleep(0.5)
                print(f'Você comprou {item} por {valor} moedas')
                sleep(0.5)
            else:
                sleep(0.5)
                print('Moedas insuficiente')
                sleep(0.5)
    elif resp == 'n':
        print(end='')
def fugir():
    global game_over
    print('Você fugiu')
    t = str(input('Acabar o jogo por aqui?[S/N] ')).strip().upper()
    if t == 'S':
        game_over += 1
    elif t == 'N':
        ql_inimigo()
    return game_over, t
def fim():
    if game_over == 1:
        print()
        print(f'{'ESTATÍSTICAS':=^30}')
        print(f'Morreu na fase: {fase}')
        if fase > 1:
            print(f'Inimigos derrotados: {fase - 1} ')
        elif fase == 0:
            print(f'Inimigos derrotados: 0 ')
        print(f'Você usou a cura {tot_cura}x')
        print(f'Morreu com {moedas} moeda/s')
        print(f'Morreu com {cont_escudo} escudo/s')
        print(f'Morreu com {cont_espada} espada/s')


inimigo = ql_inimigo()
while True:
    n = menu()
    if n == 1:
        meu_dano, meu_critico, ini_vida = meu_ataque()
        if ini_vida <= 0:
            moedas, fase = verificacao()
        else:
            ata_inimigo()
        if minha_vida <= 0:
            print('Você \033[4mMORREU\033[m.\033[1;31mGame over\033[m')
            game_over += 1
    elif n == 2:
        cura, minha_vida, cont_cura = curar()
    elif n == 3:
        status()
    elif n == 4:
        loja()
    elif n == 5:
        fugir()
    if game_over == 1:
        fim()
        break