from prettytable import PrettyTable
from dice import Dice

table = PrettyTable()
dice = Dice()


class UserChar:
    def __init__(self, name, classe, race, bg, gold):
        self.name = name
        self.level = 1
        self.xp_atual = 0
        self.race = race
        self.classe = classe
        self.bg = bg
        self.attributes = classe.attributes
        self.add_race_attributes(race)
        self.hp_max = classe.hp_max + self.status_bonus("Constituição")
        self.hp_atual = self.hp_max
        self.ac = self.ac_bonus(self.classe)
        self.init_bonus = self.status_bonus("Destreza")
        self.init = 0
        self.ataque_bonus = self.status_bonus(classe.ataque_bonus)
        self.qtde_dados_dano = 1
        self.lados_dados_dano = classe.lados_dados_dano
        self.is_ranged = classe.is_ranged
        self.range = classe.range
        self.speed = race.speed
        self.size = race.size
        self.extra_features = race.extra_features
        self.gp = gold
        self.is_magic = classe.is_magic
        self.is_dead = False

    def add_race_attributes(self, race):
        for i in self.attributes:
            self.attributes[i] += race.attributes[i]

    def imprimir_atributos(self):
        os_nomes = []
        os_valores = []
        atributos = [os_nomes, os_valores]
        for i in self.attributes:
            os_nomes.append(i)
            os_valores.append(self.attributes[i])
        return atributos

    def status_bonus(self, status):
        """Retorna o bônus do status inputado."""
        bonus = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
        return bonus[self.attributes[status]]

    def ac_bonus(self, classe):
        """Retorna o valor da AC calculado com a classe escolhida"""
        v_classe = classe.name
        result = 10 + self.status_bonus("Destreza")
        if v_classe == "bárbaro":
            result += self.status_bonus("Constituição")
        if v_classe == "monge":
            result += self.status_bonus("Sabedoria")
        return result

    def imprimir_extras(self):
        return f"Por ser {self.race.name}, {self.name} {self.extra_features}."

    def print_all(self):
        print("\nSeu personagem está pronto!")
        print(f"{self.name} é um {self.classe.name} {self.race.name} {self.bg.name}.\nSeus atributos são:")
        atrib = self.imprimir_atributos()
        table.add_column("Atributo", atrib[0])
        table.add_column("Valor", atrib[1])
        print(table)
        table.clear()
        print(f"{self.name} tem {self.ac} de AC {self.hp_max} de HP máximo.")
        print(f"Seu tamanho é {self.size} e sua velocidade é {self.speed}.")
        print(self.imprimir_extras())
        print(f"{self.name} começa com {self.gp} peças de ouro.")


    def atacar(self, target):
        result = dice.roll_d20(1) + self.ataque_bonus
        print(f"Você tirou {result} no dado.")
        if result >= target.ac:
            print(f"{self.name} acerta!")
            return True
        else:
            print(f"{self.name} erra o ataque.")
            return False

    def dar_dano(self, attacker, target):
        result = dice.roll_dice(attacker.qtde_dados_dano, attacker.lados_dados_dano)
        print(f"O ataque deu {result} de dano.")
        target.hp_atual -= result
        return result

    def is_leveled_up(self):
        xp_pro_lv = {
            1: 15,
            2: 30,
            3: 60,
            4: 120,
            5: 240,
        }

        if self.level > len(xp_pro_lv):
            print(f"{self.name} não ganha mais experiência por já ter alcançado o nível máximo.")
        else:
            while self.xp_atual >= xp_pro_lv[self.level]:
                self.xp_atual -= xp_pro_lv[self.level]
                self.level += 1
                print(f'\n<{self.name} subiu para o nível {self.level}!>')
                self.level_up_bonus(self.classe)
                if self.level > len(xp_pro_lv):
                    print(f"\n{self.name} chegou ao nível máximo! Parabéns!\n")
                    return

            if self.level < len(xp_pro_lv):
                print(f"{self.name} está no nível {self.level}, com {self.xp_atual} de xp. Faltam {xp_pro_lv[self.level] - self.xp_atual} de xp para alcançar o nível {self.level + 1}.")

    def level_up_bonus(self, classe):
        self.hp_max += classe.hp_max + self.status_bonus("Constituição")
        self.hp_atual = self.hp_max
        if self.level % 2 == 0:
            self.qtde_dados_dano += 1
            self.ataque_bonus += 1
        print(f"{self.name} agora tem {self.hp_atual}/{self.hp_max} de HP, +{self.ataque_bonus} de bônus para atacar e "
              f"dá {self.qtde_dados_dano}d{self.lados_dados_dano} de dano ao acertar.")
