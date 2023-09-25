#informe n nomes em uma lista. Depois pesquise se o termo esta na lista e qual a sua posição.
lista = []

#inserindo elementos na lista
total = int(input("Nº de elementos: "))
for i in range(total):
    elemento = int(input("Elemento: "))
    lista.append(elemento)

#definindo o item para buscar
p = int(input("Termo de pesquisa: "))

#utilizando a função sort do python para ordenar a lista
lista.sort()
print(lista)

#definindo o tamanho da lista
length = len(lista)
left = 0  #posição left
right = length - 1 #posição right

while(left <= right):

    #definindo a posição do middle
    middle = int((left + right)/2)

    #se o elemento da lista na posição middle é o que está sendo procurado, então finaliza procura.
    if lista[middle] == p:
        print("achou %s na posição " %p, middle)
        break

    #se é MENOR, então muda a posição de RIGHT
    if p < lista[middle]:
        right = middle - 1
        
    #se é MAIOR, então muda a posição de LEFT
    elif p > lista[middle]:
        left = middle + 1
    
    if(left > right):
        print("Valor não encontrado")