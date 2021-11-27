from random import randint
lista = list ()
jogos = list ()
print('*'* 30)
print('Jogo da Quina')
print('*'* 30)
quant = int(input('Quantos jogo voce quer?'))
tot = 0
while tot <= quant:
  cont = 0
  while True:
    num = randint(1,60)
    if num not in lista:
      lista.append(num)
      cont += 1
      if cont >= 6 :
        break
        lista.sort()
        jogos.append(lista[:])
        lista.clear
        tot += 1
        print('-='*3,f'Soreando {quant} jogos','-='* 3)
        for i, l in enumerate(jogos): 
         print(f'jogo {i+l}: {l}')
