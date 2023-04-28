from time import sleep

ok = 'ok'
start = input(str('Podemos começar ? [S/N]: ')).strip().upper()

while ok == 'ok':
    if start == 'S':
        sleep(0.5)
        print('1° Pergunta:\nQual é a função usada para obter o tamanho de uma lista em Python? \na) lenght()\nb) size()\nc) count()\nd) len()\ne) sum()')
        answer = input(str('Qual a opçao correta? [a,b,c,d,e]: ')).strip().lower()
        if answer == 'd':
            print('Parabéns, resposta correta 🥳')
            ok = '##'
        else:
            print('Que pena você errou,\na resposta correta é a letra "d) len()"😔')
            ok = '##'
    elif start == 'N':
        print('É uma pena pois eu dou as ordens aqui então vou iniciar de qualquer jeito 😊')
        sleep(1)
        print('1° Pergunta:\nQual é a função usada para obter o tamanho de uma lista em Python? \na) lenght()\nb) size()\nc) count()\nd) len()\ne) sum()')
        answer = input(str('Qual a opçao verdadeira? [a,b,c,d,e]: ')).strip().lower()
        if answer == 'd':
            print('Parabéns, resposta correta 🥳')
            ok = '##'
        else:
            print('Que pena você errou,\na resposta correta é a letra "d) len()"😔')
            ok = '##'
    else:
        print('Você só pode escrever "S" ou "N" pois não sou inteligente, seja compreensível 😊')
        sleep(1)
        start = input(str('Podemos ir para 1° pergunta ? [S/N]: ')).strip().upper()


sleep(1)
start2 = input(str('Podemos ir para 2° pergunta ? [S/N]: ')).strip().upper()
ok = '##'

while ok == '##':
    if start2 == 'S':
        sleep(0.5)
        print('2° Pergunta:\nQual é o operador usado para verificar se um valor está em uma lista em Python? \na) in\nb) out\nc) not\nd) and\ne) or')
        answer = input(str('Qual a opçao correta? [a,b,c,d,e]: ')).strip().lower()
        if answer == 'a':
            print('Parabéns, resposta correta 🥳')
            ok = 'ok'
        else:
            print('Que pena você errou,\na resposta correta é a letra "a) in"')
            ok = 'ok'
    elif start2 == 'N':
        print('É uma pena pois eu dou as ordens aqui então vou iniciar de qualquer jeito 😊')
        sleep(1)
        print('2° Pergunta:\nQual é o operador usado para verificar se um valor está em uma lista em Python? \na) in\nb) out\nc) not\nd) and\ne) or')
        answer = input(str('Qual a opçao correta? [a,b,c,d,e]: ')).strip().lower()
        if answer == 'a':
            print('Parabéns, resposta correta 🥳')
            ok = 'ok'
        else:
            print('Que pena você errou,\na resposta correta é a letra "a) in"')
            ok = 'ok'
    else:
        print('Você só pode escrever "S" ou "N" pois não sou inteligente seja compreensível 😊')
        sleep(1)
        start2 = input(str('Podemos ir para 2° pergunta ? [S/N]: ')).strip().upper()


sleep(1)
start3 = input(str('Podemos ir para a última pergunta ? [S/N]: ')).strip().upper()
ok = 'ok'

while ok == 'ok':
    if start3 == 'S':
        sleep(0.5)
        print('3° Pergunta:\nQual é o método usado para adicionar um item a uma lista em Python?\na) add()\nb) insert()\nc) append()\nd) extend()\ne) push()')
        answer = input(str('Qual a opçao correta? [a,b,c,d,e]: ')).strip().lower()
        if answer == 'c':
            print('Parabéns, resposta correta 🥳')
            ok = 'fim'
        else:
            print('Que pena você errou,\na resposta correta é a letra "c) append()"')
            ok = 'fim'
    elif start3 == 'N':
        print('É uma pena pois eu dou as ordens aqui então vou iniciar de qualquer jeito 😊')
        sleep(1)
        print('3° Pergunta:\nQual é o método usado para adicionar um item a uma lista em Python?\na) add()\nb) insert()\nc) append()\nd) extend()\ne) push()')
        answer = input(str('Qual a opçao correta? [a,b,c,d,e]: ')).strip().lower()
        if answer == 'c':
            print('Parabéns, resposta correta 🥳')
            ok = 'fim'
        else:
            print('Que pena você errou,\na resposta correta é a letra "c) append()"')
            ok = 'fim'
    else:
        print('Você só pode escrever "S" ou "N" pois não sou inteligente seja compreensível 😊')
        sleep(1)
        start3 = input(str('Podemos ir para 3° pergunta ? [S/N]: ')).strip().upper()



sleep(2.5)
print('Foi divertido jogar com você')
sleep(1.5)
print('Recomendo testar também o jogo de adivinhação numéria\nque está no meu perfil do github')
sleep(2.5)
print('Em breve colocarei mais códigos na plataforma do GitHub')
sleep(2.5)
print('Até a próxima 😊')

    