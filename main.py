import uteis


#programa_principal

num = int(input('digite um valor:'))
fat=uteis.fatorial(num)
uteis.linha()
print(f"o fatorial de {num} é {fat}")
uteis.linha()
print(f"o dobro de {num} é {uteis.dobro(num)}")
uteis.linha()
print(f"o triplo de {num} é {uteis.triplo(num)}")
uteis.linha()