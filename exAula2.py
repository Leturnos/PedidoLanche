class FazerSanduiche:
    def __init__(self):
        self.pao = ""  # Tipos de pão
        self.carne = ""  # Tipos de carne
        self.queijo = ""  # Tipos de queijo
        self.vegetal = ""  # Tipos de vegetal
        self.molho = ""  # Tipos de molho

    def escolher_pao(self, pao):
        self.pao = pao

    def escolher_carne(self, carne):
        self.carne += carne
        
    def escolher_queijo(self, queijo):
        self.queijo += queijo

    def escolher_vegetal(self, vegetal):
        self.vegetal += vegetal

    def escolher_molho(self, molho):
        self.molho += molho

    def pedido_final(self):
        print("Pedido final:")
        print(f"Pão: {self.pao}")
        print(f"Carne: {self.carne}")
        if self.queijo != "":
            print(f"Queijo: {self.queijo}")
        if self.vegetal != "":
            print(f"Vegetal: {self.vegetal}")
        if self.molho != "":
            print(f"Molho: {self.molho}")


# Criação de um objeto da classe
sanduiche = FazerSanduiche()

# Escolha do pão
while True:
    try:
        pao_escolhido = int(input("Escolha o pão: \n1 - Integral \n2 - Brioche \n3 - Francês\n"))
    except ValueError:
        print("Digite apenas 1,2 ou 3")
        continue
    if pao_escolhido == 1:
        sanduiche.escolher_pao("Integral")
    elif pao_escolhido == 2:
        sanduiche.escolher_pao("Brioche")
    elif pao_escolhido == 3:
        sanduiche.escolher_pao("Francês")
    else:
        print("Opção inválida!")
        continue
    if (pao_escolhido == 1 or pao_escolhido == 2 or pao_escolhido == 3):
        break

# Escolha da carne 
cont = 0
while True:
    try:
        carne_escolhida = int(input("Escolha a carne: \n1 - Frango \n2 - Carne bovina \n3 - Hambúrguer vegetariano\n"))
    except ValueError:
        print("Digite apenas 1,2 ou 3")
        continue
    if carne_escolhida == 1:
        sanduiche.escolher_carne("Frango")
        cont += 1
    elif carne_escolhida == 2:
        sanduiche.escolher_carne("Carne bovina")
        cont += 1
    elif carne_escolhida == 3:
        sanduiche.escolher_carne("Hambúrguer vegetariano")
        cont += 1
    else:
        print("Opção inválida!")
        continue
    if (cont < 2) and (carne_escolhida == 1 or carne_escolhida == 2 or carne_escolhida == 3):
        carne_2 = input("Deseja uma segunda carne? (s/n)>> ")
        if carne_2.lower() == 's':
            sanduiche.escolher_carne(" e ")
            continue
        else:
            break
    else:
        break

# Escolha do queijo 
cont = 0
while True:
    try:
        queijo_escolhido = int(input("Escolha o queijo(opcional): \n1 - Cheddar \n2 - Muçarela\n3 - Sem queijo\n"))
    except ValueError:
        print("Digite apenas 1,2 ou 3")
        continue
    if queijo_escolhido == 1:
        sanduiche.escolher_queijo("Cheddar")
        cont += 1
    elif queijo_escolhido == 2:
        sanduiche.escolher_queijo("Muçarela")
        cont += 1
    elif queijo_escolhido == 3:
        cont += 1
        break
    else:
        print("Opção inválida!")
        continue
    if (cont < 2) and (queijo_escolhido == 1 or queijo_escolhido == 2):
        queijo_2 = input("Deseja um segundo queijo? (s/n)>> ")
        if queijo_2.lower() == 's':
            sanduiche.escolher_queijo(" e ")
            continue
        else:
            break
    else:
        break

# Escolha do vegetal
cont = 0
while True:
    try: 
        vegetal_escolhido = int(input("Escolha o vegetal(opcional): \n1 - Alface \n2 - Tomate\n3 - Cebola\n4 - Sem vegetal\n"))
    except ValueError:
        print("Digite apenas 1,2,3 ou 4")
        continue
    if vegetal_escolhido == 1:
        sanduiche.escolher_vegetal("Alface")
        cont += 1
    elif vegetal_escolhido == 2:
        sanduiche.escolher_vegetal("Tomate")
        cont += 1
    elif vegetal_escolhido == 3:
        sanduiche.escolher_vegetal("Cebola")
        cont += 1
    elif vegetal_escolhido == 4:
        cont += 1
        break
    else:
        print("Opção inválida!")
        continue
    if (cont < 3) and (vegetal_escolhido == 1 or vegetal_escolhido == 2 or vegetal_escolhido == 3):
        vegetal_2 = input("Deseja mais um vegetal? (s/n)>> ")
        if vegetal_2.lower() == 's':
            sanduiche.escolher_vegetal(" e ")
            continue
        else:
            break
    else:
        break

# Escolha do molho
cont = 0
while True:
    try:
        molho_escolhido = int(input("Escolha o molho(opcional): \n1 - Maionese \n2 - Ketchup\n3 - Mostarda\n4 - Sem molho\n"))
    except ValueError:
        print("Digite apenas 1,2 ou 3")
        continue
    if molho_escolhido == 1:
        sanduiche.escolher_molho("Maionese")
        cont += 1
    elif molho_escolhido == 2:
        sanduiche.escolher_molho("Ketchup")
        cont += 1
    elif molho_escolhido == 3:
        sanduiche.escolher_molho("Mostarda")
        cont += 1
    elif molho_escolhido == 4:
        cont += 1
        break
    else:
        print("Opção inválida!")
        continue
    if (cont < 3) and (molho_escolhido == 1 or molho_escolhido == 2 or molho_escolhido == 3):
        molho_2 = input("Deseja mais um molho? (s/n)>> ")
        if molho_2.lower() == 's':
            sanduiche.escolher_molho(" e ")
            continue
        else:
            break
    else:
        break

# Exibir o pedido final
sanduiche.pedido_final()
