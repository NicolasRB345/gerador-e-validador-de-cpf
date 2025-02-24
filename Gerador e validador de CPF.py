# Validador de CPF #

import random
import os

variavel_controle_1 = True

while True:
    variavel_controle_1 = True
    variavel_controle_2 = True
    frase = "O que deseja"
    print("-" * 20)
    print(f'{"O que deseja?":^{20}}')
    print("-" * 20)
    print("1- Gerar CPF [G]")
    print("2- Validar CPF [V]")
    escolha = input("Escolha: ").upper()
    os.system("cls")

    # GERANDO CPF--------------------------------

    if escolha == "G":
        while variavel_controle_1:
            os.system("cls")
            cpf = ""
            for digito in range(3):
                for digito2 in range(3):
                    novo_numero = str(random.randint(0, 3))
                    cpf += novo_numero

                if len(cpf) < 11:
                    cpf += "."

            cpf_pontuado = cpf
            cpf_não_pontuado = cpf.replace(".", "")

            # Penultimo digito do cpf

            indice = 0
            contador = 10
            soma = 0

            for numero in range(9):
                soma += int(cpf_não_pontuado[indice]) * contador
                contador -= 1
                indice += 1

            vezes_10 = soma * 10
            resto_divisao = vezes_10 % 11
            penultimo_dig = resto_divisao if resto_divisao <= 9 else 0
            cpf_não_pontuado += str(penultimo_dig)

            # Ultimo digito do cpf

            indice = 0
            contador = 11
            soma = 0

            for numero_2 in range(10):
                soma += int(cpf_não_pontuado[indice]) * contador
                contador -= 1
                indice += 1

            vezes_10 = soma * 10
            resto_divisao = vezes_10 % 11
            ultimo_dig = resto_divisao if resto_divisao <= 9 else 0

            cpf_pontuado += f"-{penultimo_dig}"
            cpf_pontuado += str(ultimo_dig)
            print(f"CPF gerado: {cpf_pontuado}")

            while True:
                gerar_mais = input("Gerar mais um CPF? [S]im [N]ão : ").upper()

                if gerar_mais == "S":
                    break
                elif gerar_mais == "N":
                    variavel_controle_1 = False
                    break
                else:
                    os.system("cls")
                    print("Por favor, digite apenas S ou N")
                    continue

    # VERIFICANDO CPF------------------------------

    elif escolha == "V":
        while variavel_controle_2:
            cpf = input("Digite o CPF no formato xxx.xxx.xxx-yy: ")
            os.system("cls")
            cpf_não_tracado = cpf.replace("-", "")
            cpf_repartido_1 = cpf_não_tracado.replace(".", "")
            # analisando pernultimo digito
            cpf_repartido_1 = cpf_repartido_1[:9]

            indice = 0
            contador = 10
            soma = 0
            try:
                for numero in range(9):
                    soma += int(cpf_repartido_1[indice]) * contador
                    contador -= 1
                    indice += 1

                vezes_10 = soma * 10
                resto_divisao = vezes_10 % 11
                penultimo_dig = resto_divisao if resto_divisao <= 9 else 0
                cpf_repartido_1 += str(penultimo_dig)

                indice = 0
                contador = 11
                soma = 0

                for numero_2 in range(10):
                    soma += int(cpf_repartido_1[indice]) * contador
                    contador -= 1
                    indice += 1

                vezes_10 = soma * 10
                resto_divisao = vezes_10 % 11
                ultimo_dig = resto_divisao if resto_divisao <= 9 else 0

                validacao_1 = cpf[12] == str(penultimo_dig)
                validacao_2 = cpf[13] == str(ultimo_dig)

                if validacao_1 and validacao_2:
                    os.system("cls")
                    print(f"O CPF {cpf} é válido.")
                else:
                    os.system("cls")
                    print(f"O CPF {cpf} não é válido")

                while True:
                    escolha = input(
                        "Deseja verificar outro CPF?: [S]im [N]ão: "
                    ).upper()
                    if escolha == "S":
                        break
                    elif escolha == "N":
                        variavel_controle_2 = False
                        break
                    else:
                        os.system("cls")
                        print("Por favor, digite apenas S ou N.")
                        continue
            except:
                print(
                    "Parece que houve um erro de digitação do CPF, use o modelo sugerido."
                )
                continue
    else:
        print("Digite apenas [G]erar ou V[alidar].")
        continue
