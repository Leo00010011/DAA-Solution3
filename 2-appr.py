from process_data import read_file

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