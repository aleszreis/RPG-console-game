from dice import Dice
from char_model import UserChar
from enemies_model import EnemiesList
from zoeira import lista_exclamacoes
import random

dice = Dice()
lista_inimigos = EnemiesList()

inimigo = lista_inimigos.new_enemy()

# tabela de xp

# tabela de xp
class Combate:
    """Primeiro turno de combate e subsequentes"""
    def combat_start(self, player, enemy):
        inimigo = enemy.name
        exclamacao = random.choice(lista_exclamacoes)
        print(f"{exclamacao}! Um {inimigo} apareceu!")
        print("Começa um combate!")
        combate = True
        # p_in = dice.roll_initiative(player)
        # en_in = dice.roll_initiative(enemy)
        player_in = 2
        enemy_in = 5
        if player_in >= enemy_in:
            #jogador vai primeiro!
            print(f"Sua iniciativa é maior! Você joga primeiro.")
            self.player_turn(player, enemy)
        else:
            print(f"O primeiro turno é de {inimigo}.")
        while combate:
            self.enemy_turn(enemy, player)
            if self.is_end(player, enemy, player):
                combate = False
            else:
                self.player_turn(player, enemy)
                if self.is_end(enemy, player, player):
                    combate = False
        # check se level up
        self.is_leveled_up(player)

# iniciativa
# rounds
    def imprimir_acoes(self, user):
        """Retorna os nomes das ações possíveis."""
        lista_de_nomes = ["Atacar", "Esperar"]
        if user.is_magic:
            lista_de_nomes.append("Usar Magia")
        return lista_de_nomes

    def player_turn(self, user, target):
        """Orienta ao player e o faz agir em seu turno"""
        print("\n<É o seu turno>")
        user_turn = 2
        choosing = True
        while choosing:
            acoes = self.imprimir_acoes(user)
            action = input(f"O que você quer fazer? {acoes}\n").lower()
            if user_turn == 0:
                print("Você perdeu sua vez.")
                choosing = False
            elif action == "atacar":
                choosing = False
                if user.atacar(target):
                    user.dar_dano(user, target)
            elif action == "esperar":
                choosing = False
                print("Você aguarda pelo próximo movimento do inimigo.")
            elif action == "usar magia" and user.is_magic:
                choosing = False
                # TODO: criar uma lista de magia, dentro de classes, para as classes mágicas. O jogador tem uma lista de magias que
                #  é expandida qnd ele upa de nível. Imprimir ela aqui e permitir escolha do jogador.
            else:
                print("Ação inválida.")
                user_turn -= 1

    def enemy_turn(self, attacker, target):
        """Inimigo ataca o jogador"""
        print(f"\n<É o turno de {attacker.name}>")
        print(f"{target.name} vai receber um ataque de {attacker.name}!")
        if attacker.ataque(attacker, target):
            attacker.dano(attacker, target)


# check se target morreu
    def is_end(self, target, attacker, user):
        """Checa se o alvo  desse turno morreu, retornando True/False"""
        if target.hp_atual <= 0:
            target.hp_atual = 0
            print(f"O HP de {target.name} é {target.hp_atual}/{target.hp_max}.")
            name_titled = target.name.title()
            print(f"{name_titled} morreu!")
            print(f"\nA vitória é de {attacker.name}.")
            vitorioso = attacker
            target.is_dead = True
            if vitorioso == user:
                print("Parabéns!")
                user.xp_atual += target.exp
            return True
        else:
            print(f"O hp de {target.name} é {target.hp_atual}/{target.hp_max}.")
            return False

# check se final de combate


# check se level up
    def is_leveled_up(self, player):
        """Checa se o personagem passou de nível e, se sim, chama pela função que adiciona os bônus do lvl up"""
        xp_pro_lv = {
            1: 15,
            2: 30,
            3: 60,
            4: 120,
            5: 240,
        }

        if player.level > len(xp_pro_lv):
            print(f"{player.name} não ganha mais experiência por já ter alcançado o nível máximo.")
        else:
            while player.xp_atual >= xp_pro_lv[player.level]:
                player.xp_atual -= xp_pro_lv[player.level]
                player.level += 1
                print(f'\n<{player.name} subiu para o nível {player.level}!>')
                player.level_up_bonus(player.classe)
                if player.level > len(xp_pro_lv):
                    print(f"\n{player.name} chegou ao nível máximo! Parabéns!\n")
                    return

            if player.level < len(xp_pro_lv):
                print(f"{player.name} está no nível {player.level}, com {player.xp_atual} de xp. Faltam {xp_pro_lv[player.level] - player.xp_atual} de xp para alcançar o nível {player.level + 1}.")