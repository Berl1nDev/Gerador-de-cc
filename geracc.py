#-- coding: UTF-8 --

#--'coded by berl1n'--#

import random, os





from sqlalchemy import true
#By: Berl1nDev
mag = '\033[1;95m'
azul = '\033[1;94m'
verm = '\033[1;31m'
verd = '\033[1;92m'
amare = '\033[1;93m'
print(f''' {mag}

                          _                  _               
                         | |                | |              
  __ _  ___ _ __ __ _  __| | ___  _ __    __| | ___    ___ ___ 
 / _` |/ _ \ '__/ _` |/ _` |/ _ \| '__/  / _` |/ _ \  / __/ __|
| (_| |  __/ | | (_| | (_| | (_) | |    | (_| |  __/  | (_| (__ 
 \__, |\___|_|  \__,_|\__,_|\___/|_|     \__,_|\___|  \___\___|
  __/ |                                                   
 |___/                                               

                         {azul}  Coded By \033[1;93m$Berl1nDev\033[1;93m \033[1;94mAnd\033[1;94m \033[1;92mSp4wnDev\033[1;92m
''')

s = True
n = False
list = [2022, 2023, 2024, 2025]
nume = random.randrange(1, 9999999999999999)
cvv = random.randrange(1, 999)
data1 = random.randrange(1, 31)
data2 = random.randrange(1, 12)
data3 = random.choice(list)
cpf = random.randrange(1, 99999999999)

var = str(input('\033[1;31mVoce deseja inserir sua BIN? s ou n?:\033[1;31m '))

if var == 's':
    nume = random.randrange (1, 9999999999999999)
    bin = int(input('Digite a BIN de 6 digitos: '))

    print('Numero Do Cartao:',nume)
    print('CVV Do Cartao:',cvv)
    print('Data Do Cartão:',data1, data2, data3)
    print('CPF CADASTRADO:',cpf)





if var == 'n':
    nume = random.randrange (1, 9999999999999999)
    
    print('Numero Do Cartao:',nume)
    print('CVV Do Cartao:',cvv)
    print('Data Do Cartão:',data1, data2, data3)
    print('CPF CADASTRADO:',cpf)