#Exibe uma mensagem de boas vindas ao usuário  

print("Bem-vindo a loja do Luis Gustavo!") 

#Solicita ao usuário o valor do produto e a quantidade adquirida 

valor = float(input("Entre com o valor do produto: ")) 

quantidade = float(input("Entre com a quantidade do produto: ")) 

#Faz o cálculo do valor total sem desconto (Valor unitário multiplicado pela quantidade) 

valor_total_sem_desconto = valor * quantidade 

#Determina o desconto com base no valor total sem desconto  

if valor_total_sem_desconto < 2500: 

    desconto = 0 #Sem desconto 

elif valor_total_sem_desconto >= 2500 and valor_total_sem_desconto < 6000: 

    desconto = 0.04 #4% de desconto 

elif valor_total_sem_desconto >= 6000 and valor_total_sem_desconto < 10000: 

    desconto = 0.07 #7% de desconto 

else: 

    desconto = 0.11 #11% de desconto 

#Calcula valor com desconto aplicado 

valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto) 

#Exibe os valores totais -com e sem desconto- formatados com duas casas decimais 

print(f"O valor SEM desconto é {valor_total_sem_desconto:.2f}") 

print(f"O valor COM desconto é {valor_total_com_desconto:.2f}") 