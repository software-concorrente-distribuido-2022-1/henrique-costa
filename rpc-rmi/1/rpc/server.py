from xmlrpc.server import SimpleXMLRPCServer

def calculate_salary(role, salary):
    newSalary = 0
    
    # calculcar novo salário baseado no cargo
    if role == 'p':
        newSalary = salary + (salary * 0.18)
    elif role == 'o':
        newSalary = salary + (salary * 0.20)

    print('Calculado novo salário')

    return 'Novo salário: R$ ' + str(newSalary) # retornar novo salário

host = '127.0.0.1'
port = 4000
server = SimpleXMLRPCServer((host, port))
print(f'Escutando na porta {port}...')

server.register_function(calculate_salary, 'calculate_salary')

server.serve_forever()