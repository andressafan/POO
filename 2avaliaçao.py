class Seguro:  # classe pai
    def __init__(self, num_apolice: int, proprietario):
        self.__num_apolice = num_apolice
        self.__proprietario = proprietario


    @property
    def num_apolice(self):
        return self.__num_apolice

    @property
    def proprietario(self):
        return self.__proprietario


    def calcularValor(self):
        pass

    def calcularPremio(self):
        pass

    def __str__(self):
        pass



class Cliente:
    def __init__(self, cpf: str, nome: str, idade: int):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property  # idade muda?
    def idade(self):
        return self.__idade


    def idade(self):
        pass

    def nome(self):
        pass


class SeguroVida(Seguro):
    def __init__(self, nome_beneficiario: str, num_apolice: int, proprietario):
        super().__init__(num_apolice, proprietario)
        self.__nome_beneficiario = nome_beneficiario

    @property
    def nome_beneficiario(self):
        return self.__nome_beneficiario

    def calcularValor(self):
        pass

    def calcularPremio(self):
        pass

    def __str__(self):
        pass


class SeguroAutomovel(Seguro):
    def __init__(self, numero_licenca: int, nome_modelo: str, ano: int, valor_automovel: float, num_apolice: int,
                 proprietario):
        super().__init__(num_apolice, proprietario)
        self.__numero_licenca = numero_licenca
        self.__nome_modelo = nome_modelo
        self.__ano = ano
        self.__valor_automovel = valor_automovel

    @property
    def numero_licenca(self):
        return self.__numero_licenca

    @property
    def nome_modelo(self):
        return self.__nome_modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def valor_automovel(self):
        return self.__valor_automovel


    def calcularValor(self):
        pass

    def calcularPremio(self):
        pass

    def calcularFranquia(self):
        pass

    def __str__(self):
        pass


