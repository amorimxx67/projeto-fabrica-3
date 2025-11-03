print("Bem-vindo ao Programa de IMC!")

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em kg): "))

imc = peso / (altura * altura)

print(f"\n{nome}, seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
