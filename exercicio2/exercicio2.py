#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leia dez números inseridos pelo usuário e responda:
- Qual o maior número e qual o seu índice?
- Qual o menor número e qual o seu índice?
- Qual a soma dos números pares?
- Qual a soma dos números ímpares?
- Qual a soma da divisão dos números de índice par, pelos números de índice ímpar?
- Imprima os números na ordem inversa em que foram digitados.
EXTRA: Leia um número arbitrário de números digitados pelo usuário, pare a entrada
        de dados quando o usuário entrar com o número zero (0).
"""


def ler_10_numeros():
    lista = []
    for contador in range(10):
        numero = int(input("Digite o {}º número:".format(contador)))
        lista.append(numero)
    return lista


def ler_numeros():
    lista = []
    continuar = True
    contador = 0
    while continuar == True:
        numero = int(input("Digite o {}º número:".format(contador)))
        lista.append(numero)
        contador += 1
        opcao = str(input("Deseja continuar? [S/N]")[0].lower())
        if opcao == 's':
            continuar = True
        else:
            continuar = False
    return lista


def numeros_inversos(lista):
    lista_parcial = []
    for numero in reversed(lista):
        lista_parcial.append(numero)


def soma_indices_pares(lista):
    soma = 0
    for cont, numero in enumerate(lista):
        if (cont % 2) == 0:
            soma += numero
    return soma


def soma_indices_impares(lista):
    soma = 0
    for cont, numero in enumerate(lista):
        if (cont % 2) != 0:
            soma += numero
    return soma


def divisao_numeros(lista):
    soma_numeros_pares =  soma_indices_pares(lista)
    soma_numeros_impares = soma_indices_pares(lista)
    return soma_numeros_pares / soma_numeros_impares


def soma_pares(lista):
    soma = 0
    for numero in lista:
        if (numero % 2) == 0:
            soma += numero
    return soma


def soma_impares(lista):
    soma = 0
    for numero in lista:
        if (numero % 2) != 0:
            soma += numero
    return soma


def maior_numero(lista):
    maior = 0
    contador_final = 0
    for contador, numero in enumerate(lista):
        if contador == 0:
            maior = numero
        elif  numero > maior:
            maior = numero
            contador_final = contador
    return maior, contador_final


def menor_numero(lista):
    menor = 0
    contador_final = 0
    for contador, numero in enumerate(lista):
        if contador == 0:
            menor = numero
        elif  numero < menor:
            menor = numero
            contador_final = contador
    return menor, contador_final
