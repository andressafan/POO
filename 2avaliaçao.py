''' Alunos: Andressa Felix e Caio Nikolas '''

class Seguro:
    def __init__(self, num_apolice: int, proprietario):
        self._num_apolice = num_apolice
        self._proprietario = proprietario

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

    @property
    def idade(self):
        return self.__idade


class SeguroVida(Seguro):
    def __init__(self, nome_beneficiario: str, num_apolice: int, proprietario):
        super().__init__(num_apolice, proprietario)
        self.__nome_beneficiario = nome_beneficiario

    @property
    def nome_beneficiario(self):
        return self.__nome_beneficiario

    def calcularValor(self):
        if self._proprietario.idade <= 30:
            return 800.00
        elif 31 <= self._proprietario.idade <= 50:
            return 1300.00
        else:
            return 1600.00

    def calcularPremio(self):
        if self._proprietario.idade <= 30:
            return 50000.00
        elif 31 <= self._proprietario.idade <= 50:
            return 30000.00
        else:
            return 20000.00

    def __str__(self):
        return f'''
        {'-' * 10 + ' S E G U R O  D E  V I D A ' + '-' * 10}
        Número da Apólice:   {self._num_apolice}
        Segurado:            {self._proprietario.nome}
        Valor:               {self.calcularValor()}
        Prêmio:              {self.calcularPremio()}
        '''


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
        return 0.03 * self.__valor_automovel

    def calcularPremio(self):
        return 0.8 * self.__valor_automovel

    def calcularFranquia(self):
        return 0.4 * self.calcularValor()

    def __str__(self):
        return f'''
        {'-' * 10 + ' S E G U R O  A U T O M O V E L ' + '-' * 10}
        Número da Apólice:   {self._num_apolice}
        Segurado:            {self._proprietario.nome}
        Valor:               {self.calcularValor()}
        Prêmio:              {self.calcularPremio()}
        '''


class ControleDeSeguros:
    def __init__(self):
        self.__seguros = []

    def cadastrarSeguro(self, seguro: Seguro):
        self.__seguros.append(seguro)

    def imprimirRelatorio(self):
        segvida = segauto = valor_total = premio_total = 0
        for seguro in self.__seguros:
            print(seguro)
            valor_total += seguro.calcularValor()
            premio_total += seguro.calcularPremio()
            if isinstance(seguro, SeguroVida):
                segvida += 1
            elif isinstance(seguro, SeguroAutomovel):
                segauto += 1
        print(f''' 
        {'-' * 10 + ' R E L A T O R I O ' + '-' * 10}
        Seguros de vida:        {segvida}
        Seguros de Automóveis:  {segauto}
        Valor total:            {valor_total}
        Prêmio Total:           {premio_total}''')


if __name__ == '__main__':
    cliente1 = Cliente("08272891823", "Andressa", 21)
    cliente2 = Cliente("19283754312", "Nikolas", 32)
    cliente3 = Cliente("92838302928", "Caio", 15)
    cliente4 = Cliente("76767788899", "Allyson", 31)
    cliente5 = Cliente("00099988764", "Lucas", 32)
    cliente6 = Cliente("12123423411", "Guilherme", 50)
    cliente7 = Cliente("12123423333", "Julia", 19)

    controle = ControleDeSeguros()
    controle.cadastrarSeguro(SeguroAutomovel(42424, "Toyota Camry", 2022, 10000.0, 2626, cliente1))
    controle.cadastrarSeguro(SeguroAutomovel(2222, "Nissan Altima", 2021, 15000.0, 312, cliente2))
    controle.cadastrarSeguro(SeguroVida(cliente6.nome, 190128, cliente6))
    controle.cadastrarSeguro(SeguroVida(cliente2.nome, 11112, cliente2))
    controle.cadastrarSeguro(SeguroAutomovel(323443, "Jeep Wrangler", 2023, 20000.0, 566, cliente3))
    controle.cadastrarSeguro(SeguroAutomovel(4455, "Volkswagen Golf", 2020, 18000.0, 101112, cliente5))
    controle.cadastrarSeguro(SeguroVida(cliente3.nome, 7, cliente3))
    controle.cadastrarSeguro(SeguroVida(cliente5.nome, 8, cliente5))
    controle.cadastrarSeguro(SeguroAutomovel(22, "Honda Civic", 2022, 25000.0, 131415, cliente4))
    controle.cadastrarSeguro(SeguroAutomovel(9, "Tesla Model S", 2023, 22000.0, 161718, cliente6))
    controle.imprimirRelatorio()

