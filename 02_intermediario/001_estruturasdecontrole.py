"""
Estruturas de controle em python servem para controlar o fluxo de execução de um programa, definindo condições, repetiçoes e desvios logicos.
"""

# Estruturas condicionais são usadas para executar blocos que dependem de uma condição (Se)

#If Executa um bloco de codigo caso a condição seja verdadeira
idade = 18
if idade >= 18:
    print("Voce é maior de idade")
#Neste caso o print so vai ser executado se a variavel idade for maior ou igual que 18

#Else Fornece um outro caminho caso a condição do if seja falsa
idade = 16
if idade >= 18:
    print("Voce é maior de idade")
else:
    print("Voce é menor de idade")
#Neste caso adicionamos o else então caso a condição desejada for falsa ele vai exibir o print do else

#Elif Permite que voce teste mais condições depois do if e antes de chegar no else 
media = 10
if media >= 9:
    print("Passou de ano igual um mestre !")
elif media >= 5:
    print("Passou de ano mas precisa melhorar !")
else:
    print("Nos vemos de novo ano que vem.")
# Aqui pode acontecer 3 condições, caso a nota seja 9 ou maior vai cair no if, caso ela não caia no if vai verificar a condição no elif e caso essa tambem seja falsa ai ele retorna o bloco do else

#Laços de repetição são usados para executar varias vezes um bloco de codigo

#For percorre uma sequencia como listas, strings ou intervalos(range)
for numero in range(1, 6):
    print(numero)  # Saída: 1, 2, 3, 4, 5
# No caso ele percorre o intervalo começando em 1 terminando em 5(1 a menos que 6 regra do python)
for numero in range(1, 6, 2):
    print(numero)   # Saída: 1, 3, 5
# No caso ele percorre o intervalo começando em 1 terminando em 5(1 a menos que 6 regra do python) e avançando de 2 em 2
# Voce pode trocar os numeros para ver o que acontece

#While Repete o bloco de codigo enquanto a condição for verdadeira
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    #Neste caso ele vai exibir o bloco de codigo identado a ele até que o contador que começa em 0 seja maior que 5
    #Por isso nesse caso adicionamor o contador (pode ser outro nome de variavel) que sempre no final do bloco ele vai acumular +1 assim impedindo a execução infinita do codigo.

#Break interrompe o laço antes que ele termine 
contador = 0
while contador < 5:
    if(contador == 3):
        break
    print(contador)
    contador += 1
    #Neste caso adicionamos o break que interrompe o while quando atigir a condição desejada 
    #Tambem podemos usar ele no for

#Continue Pula para a próxima iteração, ignorando o restante do bloco atual.
contador = 0
while contador < 5:
    if(contador == 3):
        continue
    print(contador)
    contador += 1
    #Neste caso ele so vai interromper e ignorar o print quando o contador for igual a 3, pode verificar que o numero não é impresso

#Pass Usado como um placeholder quando um bloco de código não faz nada e sera implementado no futuro
contador = 0
while contador < 5:
    if(contador == 3):
        pass
    print(contador)
    contador += 1