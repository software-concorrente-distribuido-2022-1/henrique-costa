from xmlrpc.server import SimpleXMLRPCServer

def is_adult(name, sex, age):
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

host = '127.0.0.1'
port = 4000
server = SimpleXMLRPCServer((host, port))
print(f'Escutando na porta {port}...')

server.register_function(is_adult, 'is_adult')

server.serve_forever()