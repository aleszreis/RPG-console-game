import random

class Dice:
    def __init__(self):
        self.lados = 0
        self.qtde = 0

    def roll_gold(self, qtde, lados, multiply):
        print("\nShow! Agora é hora de rolar as suas peças de ouro...")
        print(f"Essa classe rola {qtde}d{lados}, e multiplica por {multiply}.")
        concatenated = ""
        total = 0
        for i in range(qtde):
            resultado = random.randint(1, lados)
            total += resultado
            concatenated += f" {str(resultado)}"
        total *= multiply
        print(f"Seus resultados foram:{concatenated}, multiplicados por {multiply}. O total de gold ganho é {total}.")
        return total

    def roll_dice(self, qtde, lados):
        result = 0
        for i in range(qtde):
            result += random.randint(1, lados)
        return result

    def roll_d20(self, qtde):
        result = 0
        for i in range(qtde):
            result += random.randint(1, 20)
            return result

    def roll_initiative(self, user):
        result = random.randint(1, 20) + user.init_bonus
        if result < 0:
            result = 1
        print(f"{user.name} tirou {result} na iniciativa.")
        return result