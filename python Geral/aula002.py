#Valor da memória

#Na aula anterior, o conceito de váriavel ficou claro. Mas você sabia que esses valores têm um valor na memória? Veja:

nome = 'Python'

print(id(nome))

frase = f'{nome} é orientada a objetos!'

print(id(frase))

#Usa-se id() para identificar esse valor.