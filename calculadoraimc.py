#Calculadora de IMC

#Solicitar ao usuário dados de peso e altura

peso = float(input("Digite o seu peso (em quilogramas):"))
altura = float (input("Digite sua altura (em metros):"))

#Calcular IMC

imc = peso / (altura ** 2)

print("Seu IMC é:")
print (imc)

#Informar o que o valor do IMC indica

if imc < 18.5:
    print ("Você é parte da classificação: Magreza")
elif imc >= 18.5 and imc < 25:
    print ("Você é parte da classificação: Normal")
elif imc >= 25 and imc < 30:
    print ("Você é parte da classificação: Sobrepeso")
elif imc >= 30 and imc < 40:
    print ("Você é parte da classificação: Obesidade")
else: print("Você é parte da classificação: Obesidade Grave")