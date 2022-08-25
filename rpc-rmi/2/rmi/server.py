import Pyro4

# lembrar de rodar "python -m Pyro4.naming" para subir o servidor de nomes

@Pyro4.expose
class AdultChecker(object):
    def is_adult(self, name, sex, age):
        adult = False
        
        # verificar se é adulto(a)
        if sex == 'm' and age >= 18:
            adult = True
        elif sex == 'f' and age >= 21:
            adult = True

        print('Calculado maioridade')

        if (adult):
            return name + ' atingiu a maioridade.'
        else:
            return name + ' não atingiu a maioridade.'


daemon = Pyro4.Daemon() # fazer o deamon do Pyro
ns = Pyro4.locateNS() # obter o nome do servidor
uri = daemon.register(AdultChecker) # registrar AdultChecker como um objeto do Pyro
ns.register('scp.adult-checker', str(uri)) # registrar o objeto com um nome no servidor/serviço de nomes (equivalente a registry)

print('Ativo. Pronto para escutar.')

daemon.requestLoop() # iniciar o loop do servidor e esperar por chamadas