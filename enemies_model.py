import random
from dice import Dice

dice = Dice()

class Enemies:
    """Modela os inimigos"""
    def __init__(self, name, ac, hp_max, hp_atual, atq_bonus, qtde_dados_dano, lados_dados_dano, xp, init_bonus, level, melee, magic, speed, range):
        self.name = name
        self.level = level
        self.ac = ac
        self.hp_max = hp_max
        self.hp_atual = hp_atual
        self.is_melee = melee
        self.rage = range
        self.is_magic = magic
        self.speed = speed
        self.ataque_bonus = atq_bonus
        self.qtde_dados_dano = qtde_dados_dano
        self.lados_dados_dano = lados_dados_dano
        self.is_dead = False
        self.exp = xp
        self.init_bonus = init_bonus
        self.init = 0


    def ataque(self, user, target):
        result = dice.roll_d20(1) + user.ataque_bonus
        if result >= target.ac:
             print(f"{user.name} acerta!")
             return True
        else:
            print(f"{user.name} erra o ataque.")
            return False

    def dano(self, attacker, target):
        result = dice.roll_dice(attacker.qtde_dados_dano, attacker.lados_dados_dano)
        print(f"O ataque deu {result} de dano.")
        target.hp_atual -= result
        return result

class EnemiesList:
    """Lista de inimigos possíveis"""
    def __init__(self):
        self.monsters = [
            Enemies(
                name="geleinha",
                level=1,
                ac=12,
                hp_max=6,
                hp_atual=6,
                melee=True,
                range=5,
                magic=False,
                speed=15,
                atq_bonus=1,
                qtde_dados_dano=1,
                lados_dados_dano=4,
                xp=10,
                init_bonus=0
            ),
            Enemies(
                name="kobold arqueiro",
                level=1,
                ac=12,
                hp_max=6,
                hp_atual=6,
                melee=False,
                range=25,
                magic=False,
                speed=30,
                atq_bonus=1,
                qtde_dados_dano=1,
                lados_dados_dano=6,
                xp=17,
                init_bonus=0
            ),
            Enemies(
                name="zumbi",
                level=2,
                hp_max=22,
                ac=8,
                hp_atual=22,
                melee=True,
                range=5,
                magic=False,
                speed=30,
                atq_bonus=2,
                qtde_dados_dano=1,
                lados_dados_dano=6,
                xp=10,
                init_bonus=-2,
            ),
            Enemies(
                name="esqueleto",
                level=1,
                ac=15,
                hp_max=10,
                hp_atual=10,
                melee=True,
                range=5,
                magic=False,
                speed=30,
                atq_bonus=2,
                qtde_dados_dano=1,
                lados_dados_dano=6,
                xp=100,
                init_bonus=3
            ),
        ]

    def new_enemy(self):
        """Retorna um inimigo aleatório"""
        return random.choice(self.monsters)

    # def format_enemies_data(self, name):
    #     for i in enemies_data.name:
    #         print(i)"="print(enemies_data[i])

## metodos
