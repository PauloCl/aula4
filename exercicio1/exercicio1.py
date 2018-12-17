#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Programa para popular uma lista, e verificar números em par e impar."""


def verifica_lista(lista):
    lista_parcial = []
    for numero in lista:
        par_ou_impar = False
        if (numero % 2) == 0:
            par_ou_impar = True
        else:
            par_ou_impar = False
        lista_parcial.append(par_ou_impar)
    return lista_parcial
