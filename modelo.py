class Programa:
    def __init__(self, nome, ano_lancamento):
        self._nome = nome.title()   # If we use __, the attribute is set as private and will not be passed to children
        self._ano = ano_lancamento  # by heritage. To avoid it we use only one _ just to sinalize to programmers that
        self._likes = 0             # this attribute is protected. BUT this is only by convention.

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

    @property
    def duracao(self):
        return self._duracao


class Serie(Programa):
    def __init__(self, nome, ano_lancamento, temporadas):
        super().__init__(nome, ano_lancamento)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas


filme = Filme('vingadores - guerra infinita', 2018, 160)
filme.dar_likes()
print(f'{filme.nome} ({filme.ano_lancamento}): {filme.likes} curtidas.')

serie = Serie('atlanta', 2018, 2)
serie.dar_likes()
serie.dar_likes()
print(f'{serie.nome} ({serie.ano_lancamento}): {serie.likes} curtidas.')
