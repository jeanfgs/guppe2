"""
Recebendo dados de usuário
"""

nome = input("Qual é o seu nome?")

print(f"Seja bem vindo(a){nome}")

idade = int(input("Qual a sua idade?"))

cor_cabelo = input("Qual a cor do seu cabelo?")

print(f"A pessoa com o nome de {nome} tem {idade} anos e seu cabelo é {cor_cabelo} e nasceu em {2021 - idade}")
