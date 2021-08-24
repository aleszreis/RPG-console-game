from char_model import UserChar
from data import ListaDeClasses, RacesList, ListaDeAntecedentes, Escolhas
from dice import Dice
from prettytable import PrettyTable
from art import welcome
from combat_system import Combate
from enemies_model import EnemiesList
import random
import zoeira

lista_classes = ListaDeClasses()
races = RacesList()
antecedentes = ListaDeAntecedentes()
escolha = Escolhas()
dado = Dice()
table = PrettyTable()
combate = Combate()
enemies_list = EnemiesList()


char_name = input("Qual vai ser o nome do seu personagem?\n")

a_escolher = True
while a_escolher:
    print("Ok, as classes que existem são:")
    table.add_column("Classes", lista_classes.pt_find_classes())
    table.add_column("Atributos Principais", lista_classes.pt_find_classes_attributes())
    print(table)
    char_classe = escolha.escolher_coisa(input("Qual delas você quer pro seu personagem?\n").lower(), lista_classes.classes)
    table.clear()
    if char_classe != None:
        a_escolher = escolha.confirmacao(char_classe)

char_gold = dado.roll_gold(char_classe.gp_dados, char_classe.gp_valor, char_classe.gp_mult)

a_escolher = True
while a_escolher:
    print("\nAgora escolha uma raça. As opções são essas aqui:")
    table.add_column("Raças", races.pt_find_races())
    table.add_column("Bônus de Atributos", races.pt_find_races_attributes())
    table.add_column("Habilidades Extras", races.pt_find_races_extra())
    print(table)
    char_race = escolha.escolher_coisa(input("Qual delas você quer pro seu personagem?\n").lower(), races.races)
    table.clear()
    if char_race != None:
        a_escolher = escolha.confirmacao(char_race)


a_escolher = True
while a_escolher:
    print("\nPor fim, escolha um dos antecedentes:")
    table.add_column("Antecedentes", antecedentes.pt_find_bgs())
    table.add_column("Peças de Ouro", antecedentes.pt_find_bg_golds())
    table.add_column("Equipamentos Iniciais", antecedentes.pt_find_bg_equips())
    print(table)
    char_bg = escolha.escolher_coisa(input("Qual deles você quer pro seu personagem?\n").lower(), antecedentes.bgs)
    table.clear()
    if char_bg != None:
        a_escolher = escolha.confirmacao(char_bg)

char_gold += antecedentes.get_bg_gold(char_bg, char_gold)

user_char = UserChar(char_name, char_classe, char_race, char_bg, char_gold)
user_char.print_all()

