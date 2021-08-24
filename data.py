class Classe:
    def __init__(self, name, main_attributes, strenght, dexterity, constitution, intelligence, wisdom, charisma,
                 is_magic, is_ranged, descricao, gp_dados, gp_valor, gp_mult, hp_max, hp_dice, atq_status, lado_dados, range):
        self.name = name
        self.main_attributes = main_attributes
        self.attributes = {
            "Força": strenght,
            "Destreza": dexterity,
            "Constituição": constitution,
            "Ingeligência": intelligence,
            "Sabedoria": wisdom,
            "Carisma": charisma,
        }
        self.hp_max = hp_max
        self.hp_dice = hp_dice
        self.ataque_bonus = atq_status
        self.lados_dados_dano = lado_dados
        self.is_magic = is_magic
        self.is_ranged = is_ranged
        self.range = range
        self.descricao = descricao
        self.gp_dados = gp_dados
        self.gp_valor = gp_valor
        self.gp_mult = gp_mult


class ListaDeClasses:
    def __init__(self):
        """Modela as classes que o usuário pode escolher para o seu personagem"""
        self.classes = [
            Classe(
                name="guerreiro",
                main_attributes="For, Con e Des",
                atq_status="Força",
                gp_dados=5,
                gp_valor=4,
                gp_mult=10,
                strenght=15,
                dexterity=13,
                constitution=14,
                intelligence=8,
                wisdom=12,
                charisma=10,
                lado_dados=10,
                hp_max=10,
                hp_dice=10,
                is_magic=False,
                is_ranged=False,
                range=5,
                descricao="O guerreiro é uma classe física corpo-a-corpo, que, com anos de estudo, \naprendeu as melhores"
                          " técnicas de luta. Ataque e defesa são suas palavras-chave."
                   ),
            Classe(
                name="mago",
                main_attributes="Int, Des e Con",
                atq_status="Inteligência",
                gp_dados=4,
                gp_valor=4,
                gp_mult=10,
                strenght=8,
                dexterity=14,
                constitution=13,
                intelligence=15,
                wisdom=12,
                charisma=10,
                lado_dados=8,
                hp_max=6,
                hp_dice=6,
                is_magic=True,
                is_ranged=True,
                range=40,
                descricao="O mago é uma classe mágica à distância, que, com anos de estudo, \naprendeu a dobrar a trama "
                          "mágica do universo. Estudo e poder são suas palavras-chave."
        ),
            Classe(
                name="monge",
                main_attributes="Des, For e Con",
                atq_status="Destreza",
                gp_dados=5,
                gp_valor=4,
                gp_mult=1,
                strenght=14,
                dexterity=15,
                constitution=13,
                intelligence=10,
                wisdom=12,
                charisma=8,
                lado_dados=8,
                hp_max=8,
                hp_dice=8,
                is_magic=False,
                is_ranged=False,
                range=5,
                descricao="O monge é uma classe física corpo-a-corpo que usa mais agilidade do que força. \nEquilíbrio e "
                          "disciplina são suas palavras-chave."
            ),
            Classe(
                name="clérigo",
                main_attributes="Sab, For e Con",
                atq_status="Força",
                gp_dados=5,
                gp_valor=4,
                gp_mult=10,
                strenght=14,
                dexterity=12,
                constitution=13,
                intelligence=10,
                wisdom=15,
                charisma=8,
                lado_dados=6,
                hp_max=8,
                hp_dice=8,
                is_magic=True,
                is_ranged=False,
                range=5,
                descricao="O clérigo é uma classe mágica corpo-a-corpo que possui poderes graças à sua fé, \nnormalmente para ajudar seus aliados. "
                          "Defender e curar são suas palavras-chave."
            ),
            Classe(
                name="bárbaro",
                main_attributes="For, Des e Con",
                atq_status="Força",
                gp_dados=2,
                gp_valor=4,
                gp_mult=10,
                strenght=15,
                dexterity=14,
                constitution=13,
                intelligence=8,
                wisdom=10,
                charisma=12,
                lado_dados=10,
                hp_max=12,
                hp_dice=12,
                is_magic=False,
                is_ranged=False,
                range=5,
                descricao="O bárbaro é uma classe física corpo-a-corpo que canaliza uma energia primal para dar mais"
                          "\ndano em seus oponentes. Força bruta e ataque são suas palavras-chave."
            ),
            Classe(
                name="patrulheiro",
                main_attributes="Sab, Des e Con",
                atq_status="Destreza",
                gp_dados=5,
                gp_valor=4,
                gp_mult=10,
                strenght=12,
                dexterity=14,
                constitution=13,
                intelligence=10,
                wisdom=15,
                charisma=8,
                lado_dados=8,
                hp_max=8,
                hp_dice=8,
                is_magic=True,
                is_ranged=True,
                range=50,
                descricao="O patrulheiro é uma classe física à distância especializado em rastrear e abater suas presas."
                          "\nPrecisão e sobrevivência são suas palavras-chave."
            ),
            Classe(
                name="bruxo",
                main_attributes="Car, Des e Con",
                atq_status="Carisma",
                gp_dados=4,
                gp_valor=4,
                gp_mult=10,
                strenght=8,
                dexterity=14,
                constitution=13,
                intelligence=12,
                wisdom=10,
                charisma=15,
                lado_dados=8,
                hp_max=8,
                hp_dice=8,
                is_magic=True,
                is_ranged=True,
                range=30,
                descricao="O bruxo é uma classe mágica à distância que adquiriu poderes pelo pacto com uma entidade \nsobrenatural. " 
                          "Ambição e ocultismo são suas palavras-chave."
            ),
            Classe(
                name="paladino",
                main_attributes="Car, For e Des",
                atq_status="Força",
                gp_dados=5,
                gp_valor=4,
                gp_mult=10,
                strenght=14,
                dexterity=13,
                constitution=12,
                intelligence=10,
                wisdom=8,
                charisma=15,
                lado_dados=8,
                hp_max=10,
                hp_dice=10,
                is_magic=True,
                is_ranged=False,
                range=5,
                descricao="O paladino é uma classe mágica corpo-a-corpo dedicado a eliminar o mal do mundo.\n"
                          "Dedicação e justiça são suas palavras-chave."
            ),
]

    def imprimir_classes(self):
        """Retorna os nomes das classes disponíveis."""
        lista_de_nomes = ""
        for i in range(len(self.classes) - 1):
            lista_de_nomes += f'{self.classes[i].name}, '
        lista_de_nomes += f'e {self.classes[len(self.classes)- 1].name}'
        return f"{lista_de_nomes}."

## TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE ##
    def pt_find_classes(self):
            """Retorna os nomes das classes como uma lista"""
            lista_de_nomes = []
            for i in range(len(self.classes)):
                lista_de_nomes.append(self.classes[i].name)
            return lista_de_nomes

    def pt_find_classes_attributes(self):
            """Retorna os atributos mais fortes das classes como uma lista."""
            lista_de_status = []
            for i in range(len(self.classes)):
                lista_de_status.append(self.classes[i].main_attributes)
            return lista_de_status
## TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE TESTE ##

class Races:
    """Modela as raças"""
    def __init__(self, name, bonus, strenght, dexterity, constitution, intelligence, wisdom, charisma, speed, size, has_extra, descricao):
        self.name = name
        self.bonus_attributes = bonus
        self.attributes = {
            "Força": strenght,
            "Destreza": dexterity,
            "Constituição": constitution,
            "Ingelicência": intelligence,
            "Sabedoria": wisdom,
            "Carisma": charisma,
        }
        self.speed = f"{speed} feet de movimento"
        self.size = size
        self.extra_features = has_extra
        self.descricao=descricao


class RacesList:
    def __init__(self):
        """Modela as raças que o usuário pode escolher para o seu personagem"""
        self.races = [
            Races(
                name="humano",
                bonus="Todos os atributos +1",
                strenght=1,
                dexterity=1,
                constitution=1,
                intelligence=1,
                wisdom=1,
                charisma=1,
                speed=30,
                size="médio",
                has_extra="não possui características extras",
                descricao="Os seres humanos são os mais jovens das raças comuns, tarde para chegar na cena mundial e \n"
                          "de curta duração em comparação com anões, elfos e dragões.Talvez seja por causa de suas vidas \n"
                          "mais curtas que eles se esforçam para conseguir o máximo que puderem nos anos que são dadas.",
            ),
            Races(
                name="meio-orc",
                bonus="For +2 e Con +1",
                strenght=2,
                dexterity=0,
                constitution=1,
                intelligence=0,
                wisdom=0,
                charisma=0,
                speed=30,
                size="médio",
                has_extra="possui Visão Noturna (60ft.) e Relentless Endurance",
                descricao="Quer seja provando seu poder em tribos bárbaras, quer seja tentando sobreviver em favelas em grandes cidades, "
                          "\nos meio-orcs se firmam através de sua força física, sua resistência e da pura determinação que herdaram de \n"
                          "seus ancestrais humanos.",
                   ),
            Races(
                name="elfo",
                bonus="Des +2 e Int +1",
                strenght=0,
                dexterity=2,
                constitution=0,
                intelligence=1,
                wisdom=0,
                charisma=0,
                speed=30,
                size="médio",
                has_extra="possui Visão Noturna (60ft.), Ancestralidade Feérica e Transe",
                descricao="Elfos são um povo mágico de graça sobrenatural, vivendo no mundo sem pertencer inteiramente à ele. \n"
                          "Em geral, amam a natureza e a magia, a arte e o estudo, a música e a poesia, e as coisas boas do mundo.",
            ),
            Races(
                name="meio-elfo",
                bonus="Car +2 e Dex +1",
                strenght=0,
                dexterity=1,
                constitution=0,
                intelligence=0,
                wisdom=0,
                charisma=2,
                speed=30,
                size="médio",
                has_extra="possui Visão Noturna (60ft.) e Ancestralidade Feérica",
                descricao="Vagando entre dois mundos mas, na verdade, não pertencendo a nenhum dos dois, meio-elfos \n"
                          "combinam o que alguns dizem ser as melhores qualidades dos seus parentes elfos e humanos: \n"
                          "a curiosidade, inventividade e ambição humanas temperadas pelos sensos refinados, amor a natureza \n"
                          "e gostos artísticos dos elfos.",
            ),
            Races(
                name="anão",
                bonus="Con +2 e For +1",
                strenght=1,
                dexterity=0,
                constitution=2,
                intelligence=0,
                wisdom=0,
                charisma=0,
                speed=30,
                size="médio",
                has_extra="possui Visão Noturna (60ft.) e Resiliência Anã",
                descricao="Corajosos e destemidos, anões são conhecidos como grande guerreiros, mineiros e artesões \n"
                          "habilidosos em trabalho com pedra e metal. Embora a altura deles fica abaixo de 5ft (1,5m), \n"
                          "anões são tão largos e robustos que pode pesar tanto quanto um humano. Para eles, tudo deve \n"
                          "ser sólido e durador, como as montanhas que amam, resistindo à passagem dos séculos com \n"
                          "resistência e pouca mudança",
            ),
        ]

    def imprimir_races(self):
        """Retorna os nomes das raças disponíveis."""
        lista_de_nomes = ""
        for i in range(len(self.races) - 1):
            lista_de_nomes += f'{self.races[i].name}, '
        lista_de_nomes += f'e {self.races[len(self.races)- 1].name}'
        return f"{lista_de_nomes}."

## pt = prettytable
    def pt_find_races(self):
            """Retorna os nomes das raças como uma lista"""
            lista_de_nomes = []
            for i in range(len(self.races)):
                lista_de_nomes.append(self.races[i].name)
            return lista_de_nomes

    def pt_find_races_attributes(self):
            """Retorna os bônus de atributos das raças como uma lista."""
            lista_de_status = []
            for i in range(len(self.races)):
                lista_de_status.append(self.races[i].bonus_attributes)
            return lista_de_status

    def pt_find_races_extra(self):
            """Retorna os bônus de atributos das raças como uma lista."""
            lista_de_extras = []
            for i in range(len(self.races)):
                lista_de_extras.append(self.races[i].extra_features)
            return lista_de_extras

class Antecedentes:
    """Modela os antecedentes"""
    def __init__(self, name, equips, descricao, gp):
        self.name = name
        self.equips = equips
        self.descricao = descricao
        self.gp = gp


class ListaDeAntecedentes:
    """Antecedentes que o usuário pode escolher para o seu personagem"""
    def __init__(self):
        self.bgs = [
            Antecedentes(
                name="artesão de guilda",
                equips="uma ferramenta de artesão e uma bolsa extra",
                descricao="Como um membro respeitado de guilda você tem benefícios. Seus companheiros de guilda vão \n"
                          "lhe providenciar alimentação e hospedagem, e pagar por seus custos funerais, sem necessário. \n"
                          "Guildas costumam ter um grande poder político, se você for acusado de um crime a guilda irá \n"
                          "lhe dar suporte caso seja inocente ou seu crime justificável. Você deve pagar 5po por mês para \n"
                          "fazer parte de sua guilda.",
                gp=0,

            ),
            Antecedentes(
                name="acólito",
                equips="uma bata e um símbolo religioso",
                descricao="Você tem o respeito de outros de sua fé, e pode fazer as cerimônias religiosas de sua divindade. \n"
                          "Você e seus companheiros podem esperar cura e cuidado grátis em um templo de sua fé, apesar de \n"
                          "precisar pagar componentes caros. Sua religião e doações lhe sustentam em um estilo de vida Modesto."
                          "\nVocê também pode ter elos com um templo em particular, seja onde morou ou onde mora agora, e enquanto \n"
                          "próximo dele você tem assistência garantida de seus sacerdotes, desde que não seja algo perigoso.",
                gp=15,
            ),
            Antecedentes(
                name="charlatão",
                equips="um kit de disfarce e dois dados viciados",
                descricao="Você criou uma segunda identidade que inclui documentos, conhecidos e disfarces. \n"
                          "Você também consegue forjar documentos, incluindo oficiais e cartas pessoais, desde que \n"
                          "tenha um exemplo do documento ou escrita que está tentando copiar.",
                gp=15,
            ),
            Antecedentes(
                name="eremita",
                equips="um kit de herbalismo e um cobertor de inverno",
                descricao="Sua peregrinação lhe garantiu uma poderosa descoberta, de acordo com seu afastamento; \n"
                          "uma verdade sobre os deuses, cosmos, forças da natureza ou mesmo história. Pode ser \n"
                          "informação importante para um grupo, ou perigosa para os que lhe exilaram, um dos motivos \n"
                          "de seu retorno à sociedade. O mestre trabalhará com você sobre a natureza e impacto \n"
                          "de sua descoberta.",
                gp=5,
            ),
            Antecedentes(
                name="escolástico",
                equips="um kit de escrita e um livro emprestado",
                descricao="Você tem acesso livre à maior parte das bibliotecas de sua ordem. Apesar de algumas \n"
                          "informações serem preciosas ou secretas, você tem uma boa idéia sobre como lidar com a \n"
                          "burocracia. \nAdicionalmente você recebe tratamento preferencial em outras bibliotecas e \n"
                          "com professores e escolásticos.",
                gp=10,
            ),
            Antecedentes(
                name="forasteiro",
                equips="uma armadilha de caçador e um troféu de uma presa",
                descricao="Você tem uma memória excelente para mapas e geografia, e sempre pode se lembrar de terreno, \n"
                          "postos de civilização e outros traços em volta. Você também pode encontrar comida e água para \n"
                          "você e até mais cinco pessoas a cada dia, desde que a região os ofereça.",
                gp=10,
            ),
            Antecedentes(
                name="herói do povo",
                equips="uma pá e uma panela de ferro",
                descricao="Vindo do povo comum você encontra espaço entre eles. Sempre pode encontrar lugar para se esconder, \n"
                          "descansar ou se recuperar entre o povo comum, a não ser que tenha se mostrado um perigo para eles; \n"
                          "a plebe lhe esconde da lei ou de quem o persegue, apesar de não arriscarem a vida por você.",
                gp=10,
            ),
            Antecedentes(
                name="nobre",
                equips="um sinete e roupas chiques",
                descricao="Graças a seu título as pessoas tendem a esperar o melhor de você. Você é bem recebido em alta \n"
                          "sociedade, e as pessoas assumem que você tem o direito de estar onde está. O povo comum tenta \n"
                          "evitar lhe desagradar, e você pode conseguir uma audiência com nobres locais. Além disso, você \n"
                          "tem o serviço de até três servos fiéis à sua família, atendentes, mensageiro, mordomos, etc. \n"
                          "Seus servos são plebeus que realizam funções simples, mas não lutam por você nem o acompanham \n"
                          "em situações perigosas.",
                gp=25,
            ),
            Antecedentes(
                name="órfão",
                equips="uma faca pequena e um bichinho de estimação",
                descricao="Você conhece os padrões e fluxos secretos das cidades, e pode encontrar passagens que outros \n"
                          "perderiam. Fora de combate você e seus companheiros podem se mover de um local a outro na \n"
                          "cidade em metade do tempo.",
                gp=10,
            ),
            Antecedentes(
                name="soldado",
                equips="uma medalha de patente e um troféu tirado de um oponente caído",
                descricao="Você tem uma patente de sua carreira como soldado. Soldados leais a sua organização ainda \n"
                          "reconhecem sua autoridade e influência, prestam deferência a você se de patente menor. Você \n"
                          "pode usar sua influência para emprestar cavalos e equipamentos simples, ou ter acesso a \n"
                          "fortaleza e acampamentos militares onde sua patente é reconhecida.",
                gp=10,
            ),
        ]

    def imprimir_antecedentes(self):
        """Retorna os nomes dos antecedentes disponíveis."""
        lista_de_nomes = ""
        for i in range(len(self.bgs) - 1):
            lista_de_nomes += f'{self.bgs[i].name}, '
        lista_de_nomes += f'e {self.bgs[len(self.bgs)- 1].name}'
        return f"{lista_de_nomes}."

    def pt_find_bgs(self):
            """Retorna os nomes dos antecedentes como uma lista."""
            lista_de_nomes = []
            for i in range(len(self.bgs)):
                lista_de_nomes.append(self.bgs[i].name)
            return lista_de_nomes

    def pt_find_bg_golds(self):
            """Retorna os golds iniciais dos antecedentes como uma lista."""
            lista_de_money = []
            for i in range(len(self.bgs)):
                lista_de_money.append(self.bgs[i].gp)
            return lista_de_money

    def pt_find_bg_equips(self):
            """Retorna os equips iniciais dos antecedentes como uma lista."""
            lista_de_equips = []
            for i in range(len(self.bgs)):
                lista_de_equips.append(self.bgs[i].equips)
            return lista_de_equips

    def get_bg_gold(self, bg_escolhido, char_gold):
        """Adiciona o gold vindo do BG na ficha de personagem"""
        for i in self.bgs:
            a = bg_escolhido.name
            if i.name == a:
                if i.gp > 0:
                    char_gold += i.gp
                    print(f"E adicionando as {i.gp} peças de ouro do antecedente, você agora possui {char_gold} peças de ouro.")
                    return i.gp
                else:
                    print(f"Esse antecedente não começa com outro extra.")
                    return 0

import zoeira

class Escolhas:
    def confirmacao(self, escolha):
        print(escolha.descricao)
        a_escolher = input("\nVai manter essa escolha? Digite 'sim' ou 'não': ")
        if a_escolher in zoeira.lista_respostas_positivas:
            return False
        else:
            return True


    def escolher_coisa(self, coisa_escolhida, lista_da_coisa):
        """Seleciona a opção dentre a lista de opções. Retorna a opção se existir, senão retorna None"""
        for i in lista_da_coisa:
            if i.name == coisa_escolhida:
                return i
        print("Essa opção não está na lista.")