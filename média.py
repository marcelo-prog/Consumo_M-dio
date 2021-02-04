print("Agora vamos calcular o consumo médio de sua viagen!")
print("Para isso tenha em mãos:")
print("Primeiro o total de litros consumido nessa viagen.")
print("Segundo tenha em mãos o total em quilometros que você percorreu nessa viagen.")

litros=float(input("Digite quantos litros você abasteceu!"))

distância = float(input("Digite o total de quilometros percorridos nessa viagen!"))

média = distância / litros

print("A sua média de consumo foi: {} por litro ".format(média))



