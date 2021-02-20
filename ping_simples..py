# Importadndo a Biblioteca recursos do Sistema Opracional.
import os
# Disparador de Ping Simples.
print('#'*40) # Imprimindo #*60 vezes.
ip_ou_host = input(' Digite o IP a ser verification : ') # Foi Criado uma Variavel .
print('-'*30) # Imprimindo #*60 vezes.
os.system('ping -n 6 {}'.format(ip_ou_host))# Chamando o Modulo System da Biblioteca os - comando Ping vai numero de Pacotes eo Ip {}.
print('-'*30) # Imprimindo #*60 vezes.


# Ola e um Simples Disparador de Pings.
