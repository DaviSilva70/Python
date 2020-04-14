# coding=utf-8
# Faça um programa que leia um Angulo qualquer e mostre,na tela o valor do seno caseno
# e tangante desse angulo.

# Primeira Forma importando o conjunto total de bibliotaca (Math)
import math
angulo = float(input('Digite seu Angulo : '))
seno = math.sin(math.radians(angulo))
print('O Angulo de {} tem seu Seno {:.2f}'.format(angulo,seno))
cosseno =math.cos(math.radians(angulo))
print('O Angulo de {} do Cosseno ede {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O Angulo e de {} do Tangente {:.2f}\n'.format(angulo,tangente))


# Segunda Forma Forma importando somente as bibliotecas necessarias 
from math import radians,sin,cos,tan
angulo = float(input('Digite o Angulo que voçe deseja:'))
seno = sin(radians(angulo))
print('O Angulo de {}  tem SENO {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O Angulo de {} tem COSSENO E DE {:.2F}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print("O Angulo de {} TANGENTE e de {:.2f}\n".format(angulo, tangente))