# Nome => Tem que ter mais de 3 caracteres
nome = str(input("Digite seu nome: "))
while len(nome) <= 3:
    nome = str(
        input("Seu nome deve ter mais de 3 caracteres \n Digite seu nome novamente: "))

# Idade => Tem que ter entre 1 a 100 anos
idade = int(input("Digite sua idade: "))
while (idade < 1) or (idade > 100):
    idade = int(input(
        "Você tem que ter entre 1 a 100 anos de idade \n Diga sua idade novamente: "))

# Salário => Tem que ser maior que R$ 0,00
salario = float(input("Digite seu salário: "))
while salario < 1:
    salario = float(input(
        "Seu salário tem que ser maior que R$ 0,00 \n Digite seu salário novamente: R$ "))

# Sexo => Só pode ser [M]- Masculino ou [F]- Feminino
sexo = str(input("Digite seu sexo [M]- Masculino [F]- Feminino : "))
while (sexo != "M") and (sexo != "F"):
    sexo = str(input(
        "Pode somente ser digitado [M]- Masculino ou [F]- Feminino \n Digite novamente:  "))

# Estado civil => Só pode ser [S]- Solteiro [C]- Casado [V]- Viúvo [D]- Divorciado
estado_civil = str(input(
    "Diga seu estado civil [S]- Solteiro(a) [C]- Casado(a) [V]- Viúvo(a) [D]- Divorciado : "))
while (estado_civil != "S") and (estado_civil != "C") and (estado_civil != "V") and (estado_civil != "D"):
    estado_civil = str(input(
        "[S]- Solteiro(a) [C]-Casado(a) [V]- Viúvo(a) [D]- Divorciado \n Escolha somente umas dessas alternativas: "))
# Mensagem pro usuário confirmando todos os dados
print("Tudo validado!")
