import contas
import pessoa

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoa.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    def _checa_agencia(self, conta: contas.Conta) -> bool:
        return conta.agencia in self.agencias
        
    def _checa_cliente(self, cliente: pessoa.Pessoa) -> bool:
        return cliente in self.clientes
        
    def _checa_conta(self, conta: contas.Conta) -> bool:
        return conta in self.contas

    def _checa_conta_cliente(self, cliente: pessoa.Cliente, conta: contas.Conta) -> bool:
        return conta is cliente.conta

    def autenticar(self, cliente: pessoa.Cliente, conta: contas.Conta) -> bool:
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_conta_cliente(cliente, conta)

if __name__ == '__main__':
    c1 = pessoa.Cliente('Aecio', 30)
    cc1 = contas.ContaCorrente(11,22,0,0)
    c1.conta = cc1

    c2 = pessoa.Cliente('Maria', 18)
    cp2 = contas.ContaPupanca(12,23,100)
    c2.conta = cp2

    banco = Banco()
    banco.clientes.extend([c1,c2])
    banco.contas.extend([cc1,cp2])
    banco.agencias.extend([11,12])
    print(banco.__dict__)

