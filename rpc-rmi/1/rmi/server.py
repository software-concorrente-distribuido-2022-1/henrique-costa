import Pyro4

# lembrar de rodar "python -m Pyro4.naming" para subir o servidor de nomes

@Pyro4.expose
class SalaryCalculator(object):
    def calculate_salary(self, role, salary):
        newSalary = 0
        
        # calculcar novo salário baseado no cargo
        if role == 'p':
            newSalary = salary + (salary * 0.18)
        elif role == 'o':
            newSalary = salary + (salary * 0.20)

        print('Calculado novo salário')

        return 'Novo salário: R$ ' + str(newSalary) # retornar novo salário


daemon = Pyro4.Daemon() # fazer o deamon do Pyro
ns = Pyro4.locateNS() # obter o nome do servidor
uri = daemon.register(SalaryCalculator) # registrar SalaryCalculator como um objeto do Pyro
ns.register('scp.salary-calculator', str(uri)) # registrar o objeto com um nome no servidor/serviço de nomes (equivalente a registry)

print('Ativo. Pronto para escutar.')

daemon.requestLoop() # iniciar o loop do servidor e esperar por chamadas