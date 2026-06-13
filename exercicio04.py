
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
# Palavra reservada "try" = inicia um bloco de código que pode gerar uma exceção (erro) e permite tratar essa exceção de forma adequada, evitando que o programa seja interrompido abruptamente. O bloco "try" é seguido por um bloco "except" que define como lidar com a exceção caso ela ocorra.



print("Sistema de Controle Financeiro")
print("$============$$==============$")

try:
    # Entrada de dados
    nome= input("Digite o nome do usuário: ")
    receita = float(input("Digite o valor da receita: "))
    despesa = float(input("Digite o valor da despesa: "))   
except ValueError:
    print("Valor inválido. Por favor, digite um número válido para receita e despesa.")


    # Processamento

else:   # O bloco "else" é executado se o bloco "try" for executado sem gerar uma exceção. 
        #Ele é usado para definir um código que deve ser executado quando não ocorrer nenhum erro no bloco "try". 
        # Se uma exceção ocorrer no bloco "try", o código dentro do bloco "else" será ignorado e o programa passará 
        # para o bloco "except" para tratar a exceção.

    resultado = receita-despesa

    #Saída
print("O resultado é: " + "R$ " + str(resultado))
#ou este print
#print(f"O resultado é: R$ {resultado:.2f}")  # O formato :.2f é usado para exibir o resultado com 2 casas decimais.

if resultado > 0:
    print("Parabéns! Você teve um saldo positivo.")

elif resultado < 0:
    print("Cuidado! Você teve um saldo negativo.")

# if ==> Se
# Palavra reservada "if" = inicia uma estrutura de controle de fluxo que permite executar um bloco de código se uma 
# condição for verdadeira. A sintaxe básica é: if condição: bloco de código. O bloco de código dentro do "if" será 
# executado apenas se a condição for avaliada como verdadeira.

# Else ==> Senão
# Palavra reservada "elif" = é uma abreviação de "else if" e é usada em conjunto com a estrutura "if" para criar múltiplas condições. 
# A sintaxe básica é: if condição1: bloco de código1 elif condição2: bloco de código2 else: bloco de código3. 
# O bloco de código dentro do "elif" será executado apenas se a condição1 for falsa e a condição2 for verdadeira.

print("===============Fim do programa.===============")