from process_data import read_file
import random 

#Este algoritmo es una 2-approximation del problema de 3-CNF-SAT
def k_approximation(cnf):
    pos_c = 0
    neg_c = 0

    for clause in cnf:
        count = 0
        for l in clause.split():
            if count > 0:
                if l[0]!='!': count+=1
                else: break
            elif count < 0 :
                if l[0] =='!': count-=1
                else: break
            else: #count = 0 
                if l[0] == '!': count -=1
                else: count +=1
        if abs(count) == len(clause.split()) and count > 0: pos_c +=1
        if abs(count) == len(clause.split()) and count < 0: neg_c +=1
    return pos_c, neg_c


if __name__ == '__main__':
    filename = "sample1.txt"
    cnf, _ = read_file(filename)
    output_file = f"output_{filename}"
    
    positive_clauses, negative_clauses = k_approximation(cnf)
    print(f"\nAll literals in True has: {len(cnf) - negative_clauses} clauses in True")
    print("---------------------------------------")
    print(f"All literals in False has: {len(cnf) - positive_clauses} clauses in True")
    print("---------------------------------------")
    print(f"Total de clausulas: {len(cnf)}\n")


#Este algoritmo es una 2-approximation del problema de 3-CNF-SAT
def k_approximation(cnf):
    pos_c = 0
    neg_c = 0

    for clause in cnf:
        count = 0
        for l in clause.split():
            if count > 0:
                if l[0]!='!': count+=1
                else: break
            elif count < 0 :
                if l[0] =='!': count-=1
                else: break
            else: #count = 0 
                if l[0] == '!': count -=1
                else: count +=1
        if abs(count) == len(clause.split()) and count > 0: pos_c +=1
        if abs(count) == len(clause.split()) and count < 0: neg_c +=1
    return pos_c, neg_c


if __name__ == '__main__':
    filename = "sample1.txt"
    cnf, _ = read_file(filename)
    output_file = f"output_{filename}"
    
    positive_clauses, negative_clauses = k_approximation(cnf)
    print(f"\nAll literals in True has: {len(cnf) - negative_clauses} clauses in True")
    print("---------------------------------------")
    print(f"All literals in False has: {len(cnf) - positive_clauses} clauses in True")
    print("---------------------------------------")
    print(f"Total de clausulas: {len(cnf)}\n")


# LEFT: clausulas que qudan por hacer true
# LIT: literales que me quedan por esoger
# SUB: Clausulas que se han hecho true
# TRUE: Literales que se han hecho true

# Buscar el literal que está en la mayor cantidad de clausulas
# Quitarlo de la lista de LIT a el y a su opuesto

class Lit:
    def __init__(self,id):
        self.id = id
        self.count = 0
        self.gen = 0

    def __hash__(self) -> int:
        return self.id
    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id
    def __repr__(self) -> str:
        return str(self.id)

def other_approx(clauses:list[list[Lit]]):
    current_gen = 0
    any_left = True
    # get lits
    left_lits = set()
    for clause in clauses:
        for lit in clause:
            left_lits.add(lit)
    left_lits: list[Lit] = list(left_lits)
    current_clauses = clauses
    true_clauses = []
    true_lits = []
    while any_left:
        # count clause with lit
        for clause in current_clauses:
            for lit in clause:
                if lit.gen == current_gen:
                    lit.count += 1
                else:
                    lit.count = 1
                    lit.gen = current_gen
        # get literal in most clauses
        max = 0
        max_lit = None
        for lit in left_lits:
            if current_gen == lit.gen:
                if lit.count > max:
                    max_lit = lit
                    max = lit.count
        true_lits.append(max_lit)
        # get left clauses
        left_clauses = []
        for clause in current_clauses:
            have_max_lit = False
            for lit in clause:
                if lit == max_lit:
                    true_clauses += [clause]
                    have_max_lit = True
                    break
            if not have_max_lit:
                left_clauses += [clause]
        current_clauses = left_clauses
        # removing lit and !lit
        left_lits.remove(max_lit)
        try:
            left_clauses.remove(Lit(max_lit.id*-1))
        except Exception:
            pass
        # check any left
        any_left = False
        for clause in current_clauses:
            for lit in clause:
                if lit in left_lits:
                    any_left = True
                    break
            if any_left:
                break

        current_gen += 1

    return true_clauses, true_lits





lits = []
for i in range(1,11):
    lits.append(Lit(i))
    lits.append(Lit(i*-1))

clauses = []
for _ in range(3):
    clauses += [random.choices(lits,k = 3)]
print(clauses)

true_clasuse, true_lits = other_approx(clauses=clauses)
print('true clauses')
print(true_clasuse)
print('true lits')
print(true_lits)

