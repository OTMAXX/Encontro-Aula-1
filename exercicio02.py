
# Entrada
# Faça um sistema que leia dois valores ao final mostre o resultado:
# Nome do Usuário = (variável de entrada) ou seja, pode receber qualquer valor = nome_usuario
# Valor salário = (variável de entrada) ou seja, pode receber qualquer valor = receita
# Valor dispesa = (variável de entrada) ou seja, pode receber qualquer valor = despesa
# Valor resultado = (variável de saída) ou seja, pode receber qualquer valor = resultado

# Processo
# Resultado = receita-despesa
# Resultado = qtde_bolo * valor_venda
# Resultado = 20*15
# Resultado = 300

# Saída
# Resultado = "O resultado é: " + resultado
# Resultado = "O resultado é: " + str(resultado)

#Inciciar a programação
# Palavra reservada "print" = imprime na tela o que estiver entre parênteses
# Palavra reservada "input" = recebe um valor do usuário
# Palavra reservada "float" = converte um valor para número decimal, ou seja, um número com casas decimais (10.75, 20,55, 1,75 etc)
# Palavra reservada "str" = converte um valor para texto, ou seja, uma sequência de caracteres (letras, números, símbolos, etc)
# Palavra reservada "int" = converte um valor para número inteiro, ou seja, um número sem casas decimais (10, 20, 30, etc)


print("Sistema de Controle Financeiro")
print("$============$$==============$")

# Entrada de dados
nome= input("Digite o nome do usuário: ")
receita = float(input("Digite o valor da receita: "))
despesa = float(input("Digite o valor da despesa: "))   

# Processamento
resultado = receita-despesa

#Saída
print("O resultado é: " + "R$ " + str(resultado))
