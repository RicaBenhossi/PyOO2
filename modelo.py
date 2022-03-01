import reprlib
from reprlib import repr


class Programa:
    def __init__(self, nome, ano_lancamento):
        self._nome = nome.title()   # If we use __, the attribute is set as private and will not be passed to children
        self._ano = ano_lancamento  # by heritage. To avoid it we use only one _ just to sinalize to programmers that
        self._likes = 0             # this attribute is protected. BUT this is only by convention.

    def __str__(self):
        return f"{self.nome}\n\tLançamento: {self.ano_lancamento}\n\t{self.likes} Likes"

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def ano_lancamento(self):
        return self._ano

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


class Filme(Programa):
    def __init__(self, nome, ano_lancamento, duracao):
        super().__init__(nome, ano_lancamento)  # super allows you to access the mother class from where you inherited
        self._duracao = duracao

    def __str__(self):
        return f"{self.nome}\n\tLançamento: {self.ano_lancamento}\n\tDuração: {self.duracao} min\n\t" \
               f"{self.likes} Likes"

    @property
    def duracao(self):
        return self._duracao


class Serie(Programa):
    def __init__(self, nome, ano_lancamento, temporadas):
        super().__init__(nome, ano_lancamento)
        self._temporadas = temporadas

    def __str__(self):
        return f"{self.nome}\n\tLamçamento: {self.ano_lancamento}\n\tTemporada(s): {self.temporadas}\n\t" \
               f"{self.likes} Likes"

    @property
    def temporadas(self):
        return self._temporadas


class Playlitst:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # This dunder method is what make a list iterable. When we implement it here, we gain list behaviours without set
    # this class as a LIST. It calls DUCK TYPING (I don´t wnat know if it is a duck.I just want it "quacks" like one)
    def __getitem__(self, item):
        return self._programas[item]

    # This dunder method allow us to use LEN in our object.
    def __len__(self):
        return len(self._programas)

    @property
    def tamanho(self):
        return len(self.programas)


def gera_like(likes: int, programa_like):
    x = 0
    while x < likes:
        programa_like.dar_likes()
        x += 1


filme = Filme("vingadores - guerra infinita", 2018, 160)
gera_like(3, filme)

serie1 = Serie("atlanta", 2018, 2)
gera_like(5, serie1)

serie2 = Serie('todo mundo odeia o chris', 2009, 7)
gera_like(10, serie2)

serie3 = Serie("ghost", 2021, 1)
gera_like(20, serie3)

lista = [serie2, serie3, serie1]
minha_playlist = Playlitst("Ver já!", lista)

# After implement __len__ in class Playlist we gain the ability to use LEN() in our object
print(f"Sua lista possui {len(minha_playlist)} programa(os).")

# After implement __getitem__ in class Playlist we gain all the particularity of a list, BUT without using heritage.
# This is called DUCK TYPING. That means that I don´t want my class to become a list (trough heritage), I want it just
# have some behaviours of a list, like be iterable, allow me to us "IN" and "FOR IN".
for programa in minha_playlist:
    print(programa)
