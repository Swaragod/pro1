
def get_employees(name, employees_list):

    if name in employees_list:
        answer = 'ok'
    else:
        answer = 'warning'

    return answer

employees = ['Ivan', 'Alexey', 'Maria', 'Anna', 'Igor','Oleg', 'Olga']

