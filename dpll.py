#import sys
from copy import deepcopy
from classes import Formula

assign_true = []
assign_false = []
n_props, n_iterations = 0, 0


def print_cnf(cnf):
    s = ''
    for i,clause in enumerate(cnf):
        if len(clause) > 0:
            temp = clause
            temp = temp.replace(' ', ' | ')
            temp = temp.replace('!', '~')
            s += '(' + temp + ')'
            if i !=len(cnf) - 1:
                s += ' & '
    if s == '':
        s = '()'
    print(s)
    return s

def write_file(filename, text):
    text = f'{text}\n'
    with open(filename, 'a') as file:
        file.write(text)

def get_units_clauses(cnf):
    units = []
    for u in cnf:
        if len(u) < 3 and u not in units:
            units.append(u)
    return units

def literals_left(cnf):
    literals = []
    for c in cnf:
        for k in c.split():
            l = k
            if len(k) > 1:
                l = k[1]
            if l not in literals:
                literals.append(l)
    return literals
def unit_in(unit, clause):
    for c in clause.split():
        if c == unit:
            return True
    return False

def solve(cnf, literals, output_file):
    text = '\nCNF = '
    print(text)
    text += print_cnf(cnf)
    write_file(output_file, text)
    
    new_true = []
    new_false = []
    global assign_true, assign_false, n_props, n_iterations
    n_iterations += 1
    units = get_units_clauses(cnf) #Para sacar las clausulas de 1 solo literal
    for unit in units:
        new_cnf = []
        n_props += 1
        if unit[0] == "!": #el literal es negativo
            assign_false.append(unit[1])
            new_false.append(unit[1])
        else:
            assign_true.append(unit)
            new_true.append(unit)
        for clause in cnf:
            new_clause = ""
            if not unit_in(unit, clause):
                new_clause = clause #Si el literal no esta en la clausula se mantiene la misma como esta
                if unit[0]!= '!' and unit_in('!'+unit, new_clause):
                    new_clause = new_clause.replace('!'+unit, '').strip()
                    if '  ' in new_clause:
                            new_clause = new_clause.replace('  ', ' ')
                elif  unit[0]== '!' and (unit[1] in new_clause):
                    new_clause = new_clause.replace(unit[1], '').strip()
                new_cnf.append(new_clause)

        cnf = new_cnf

    text = f'Units = {units}\n'
    text += f'CNF after unit propogation = '
    print(text)
    text += print_cnf(cnf)
    write_file(output_file, text)

    # NO clauses left
    if len(cnf) == 0:
        return True
    # Any empty clause
    if sum(len(clause) == 0 for clause in cnf):
        for i in new_true:
            assign_true.remove(i)
        for i in new_false:
            assign_false.remove(i)
        print('Null clause found, backtracking...')
        return False
    
    literals = literals_left(cnf)
    # Choosing a literal
    x = literals[0]
    # First Branch
    if solve(deepcopy(cnf)+[x], deepcopy(literals), output_file): return True
    # Second Branch
    elif solve(deepcopy(cnf)+['!'+x], deepcopy(literals), output_file): return True
    # Going back  
    else:
        for i in new_true:
            assign_true.remove(i)
        for i in new_false:
            assign_false.remove(i)
        return False


def dpll(cnf, literals, output_file):
    global assign_true, assign_false, n_props, n_iterations
    
    if solve(cnf, literals, output_file):
        text = f'\nNumber of iterations = {n_iterations}\n'
        text +=f'Unit Propogations = {n_props}\n'
        text +=f'Result: SATISFIABLE\n'
        text +='Solution:\n'
        for i in assign_true:
            text +=f'\t\t{i} = True\n'
        for i in assign_false:
            text +=f'\t\t{i} = False\n'
    else:
        text = '\nReached starting node!\n'
        text += f'Number of iterations = {n_iterations}\n'# cantidad de iteraciones
        text += f'Unit Propogations = {n_props}\n' 
        text += f'Result: UNSATISFIABLE\n'
    print(text)
    write_file(output_file, text=text)
    print()

if __name__=='__main__':
    filename = "sample1.txt"
    input = open(filename, 'r').read() #open(sys.argv[1], 'r').read()
    literals = [i for i in list(set(input)) if i.isalpha()]
    cnf = input.splitlines()
    output_file = f"output_{filename}"
    
    dpll(cnf,literals, output_file)