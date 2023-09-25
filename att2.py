#Método Bubble Sort para ordernação de listas

lista = []

continuarOrdenando = True
n = int(input("Nº valores: "))

#inserindo elementos na lista
for i in range(n):
    elemento = int(input("Elemento: "))
    lista.insert(i, elemento)

while(continuarOrdenando):
    continuarOrdenando = False
    #iniciando na posição ZERO
    for i in range(n-1):
        #COMPARANDO O VALOR DO ITEM DA POSIÇÃO  ATUAL É MAIOR QUE O ITEM NA POSIÇÃO POSTERIOR.
        if(lista[i] > lista[i+1]):
            #armazena em uma variável auxiliar o valor da posição atual
            aux = lista[i]
            #troca o valor da posição atual pelo valor da posição posterior
            lista[i] = lista[i+1]
            #a posição posterior recebe o valor armazenado na variável auxiliar
            lista[i+1] = aux
            #define para continuar ordenado
            continuarOrdenando = True
#exibe a lista
print(lista)