import sys
import Pyro4

salaryCalculator = Pyro4.Proxy('PYRONAME:scp.salary-calculator')

role = None
salary = None

roleInput = input('Cargo (o/operador ou p/programador): ').lower()
if roleInput == 'p' or roleInput == 'programador':
    role = 'p'
elif roleInput == 'o' or roleInput == 'operador':
    role = 'o'
else:
    print('Cargo inválido')
    sys.exit()

salaryInput = input('Salário: ')
try:
    salary = float(salaryInput)
    if salary <= 0:
        salary = None
        print('Salário inválido')
        sys.exit()
except ValueError:
    print('Salário inválido')
    sys.exit()

if role and salary:
    new_salary = salaryCalculator.calculate_salary(role, salary)
    print(new_salary)