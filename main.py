nome=input("Qual é o seu nome?")
Mes_Nascimento= int(input("Qual o mês do seu nascimento"))
Ano_Nascimento= int(input("Qual o ano do seu nascimento?"))

idade= 2022  - Ano_Nascimento


if Mes_Nascimento < 8 :
  mes= idade * 12 + (8 - Mes_Nascimento)
  dias = mes * 30
  print(f"Olá {nome}, feliz em lhe conhecer nesse ano de 2022 você possui {idade} anos ou {mes} meses ou aproximadamente {dias}  dias")
elif Mes_Nascimento >= 8 and Mes_Nascimento <=12:
  mes= idade * 12 + 8
  dias = mes * 30
  print(f"Olá {nome}, feliz em lhe conhecer nesse ano de 2022 você possui {idade} anos ou {mes} meses ou aproximadamente {dias} dias")

