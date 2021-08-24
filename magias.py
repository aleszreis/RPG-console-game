class Magia:
    def __init__(self, nome, nr_dados, lados_dados, descricao):
        self.nome = nome
        self.numero_de_dados = nr_dados
        self.lados_dados = lados_dados
        self.descricao = descricao

                # "numero de dados" e "lado de dados", nome, descrição
                #  ("recupera" ou "inflige"), resultado ("HP" ou "dano), tal que a frase fique:
                #  "{user.name} {descrição} {resultado dos dados} de {resultado}"
class ListaDeMagias:
    def __init__(self):
        self.magias = {
        Magia(
            nome="Curar",
            nr_dados=1,
            lados_dados=4,
            descricao="HP"
        ),
        Magia(
            nome="Resturação",
            nr_dados=1,
            lados_dados=6,
            descricao="HP"
        ),
        Magia(
            nome="Auxílio divino",
            nr_dados=1,
            lados_dados=8,
            descricao="HP"
        ),
        Magia(
            nome="Cura maior",
            nr_dados=2,
            lados_dados=6,
            descricao="HP"
        ),
        Magia(
            nome="Infligir dano",
            nr_dados=1,
            lados_dados=4,
            descricao="dano"
        ),
        Magia(
            nome="Bola de Fogo",
            nr_dados=3,
            lados_dados=6,
            descricao="dano"
        ),
        Magia(
            nome="Raio de Gelo",
            nr_dados=1,
            lados_dados=4,
            descricao="dano"
        ),
        Magia(
            nome="Terremoto",
            nr_dados=1,
            lados_dados=6,
            descricao="dano"
        ),
        Magia(
            nome="Mísseis mágicos",
            nr_dados=2,
            lados_dados=4,
            descricao="dano"
        ),

        }