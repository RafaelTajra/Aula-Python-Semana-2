idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))

if idade < 18 or renda < 2000:
    print("Cliente Bronze")

elif renda < 5000:
    print("Cliente Prata")

elif renda < 10000:
    print("Cliente Ouro")

else:
    print("Cliente Diamante")