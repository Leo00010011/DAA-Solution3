OPEN_PAR = (0,'(')
CLOSE_PAR = (1,')')
IMPL = (2,'=>')
SSI = (3,'<=>')
OR = (4,'||')
AND = (5,'&&')
NOT = (6,'!')
VAR = 7
END = (8,'END')


def rec_fixed_token(s:str, start_index, token:str):
    if (start_index + len(token) - 1) >= len(s):
        raise Exception(f'Unfinished expression expected Token "{token}" ')
    if s[(start_index + 1):start_index + len(token)] == token[1:]:
        return  start_index + len(token)
    else:
        raise Exception(f'Wrong token at {start_index} "{s[start_index:start_index + len(token)]}" expected Token "{token}"')
    
def rec_open_par(s:str, start_index):
    return OPEN_PAR, start_index + 1

def rec_close_par(s:str, start_index):
    return CLOSE_PAR, start_index + 1

def rec_not(s:str, start_index):
    return NOT, start_index + 1

def rec_impl(s:str, start_index):
    return IMPL, rec_fixed_token(s,start_index,'=>')

def rec_ssi(s:str, start_index):
    return SSI, rec_fixed_token(s,start_index, '<=>')

def rec_or(s:str, start_index):
    return OR, rec_fixed_token(s,start_index, '||')
    

def rec_and(s:str, start_index):
    return AND, rec_fixed_token(s,start_index, '&&')

def rec_var(s:str, start_index):
    if not s[start_index].isalnum():
        raise Exception(f'Invalid character "{s[start_index]}" at {start_index}')
    current_index = start_index
    while(current_index < len(s) and s[current_index].isalnum()):
        current_index += 1
    return (VAR,s[start_index: current_index]), current_index

rec_dict = {
    '(': rec_open_par,
    ')': rec_close_par,
    '=': rec_impl,
    '<': rec_ssi,
    '|': rec_or,
    '!': rec_not,
    '&': rec_and
}


s = '((x1 =>x2) || !((!x1 <=> x3) || x4) &&  !x2)'
s2 = 'x1 && x2 && x3'

def jump_spaces(s, index):
    while(s[index] == ' '):
        index +=1
    return index

def tokenize(s):
    current_index = 0
    result = []
    token = None
    while(current_index < len(s)):
        current_index = jump_spaces(s,current_index)
        rec = rec_dict.get(s[current_index])
        if rec:
            token,current_index = rec(s,current_index)
        else:
            token, current_index = rec_var(s,current_index)
        result.append(token)
    result.append(END)
    return result


class Not_Node:
    def __init__(self,node):
        self.node = node

class Lit_Node:
    def __init__(self,name):
        self.name = name

class Or_Node:
    def __init__(self,left, right):
        self.left = left
        self.right = right

class And_Node:
    def __init__(self,left,right):
        self.left = left
        self.right = right

class Impl_Node:
    def __init__(self,left,right):
        self.left = left
        self.right = right

class Ssi_Node:
    def __init__(self,left,right):
        self.left = left
        self.right = right

def E(tokens, start_index):
    t_node, index = T(tokens,start_index)
    e_node, index = X(tokens,index,t_node)
    return e_node, index
    

def T(tokens,start_index):
    if tokens[start_index][0] == VAR:
        return Lit_Node(tokens[start_index][1]), start_index + 1
    if tokens[start_index][0] == NOT[0]:
        t_node, index = T(tokens,start_index + 1)
        return Not_Node(t_node), index
    if tokens[start_index][0] == OPEN_PAR[0]:
        e_node, index = E(tokens,start_index + 1)
        if tokens[index][0] == CLOSE_PAR[0]:
            return e_node, index + 1
        else:
            raise Exception(f'Unexpected token "{tokens[index][1]}", expected "{CLOSE_PAR[1]}"')
    else:
        raise Exception(f'Unexpected token {tokens[start_index]}')

def X(tokens,start_index, her):
    if tokens[start_index][0] == OR[0]:
        e_node, index = E(tokens,start_index + 1)
        return Or_Node(her,e_node), index
    if tokens[start_index][0] == AND[0]:
        e_node, index = E(tokens,start_index + 1)
        return And_Node(her,e_node), index
    if tokens[start_index][0] == IMPL[0]:
        e_node, index = E(tokens,start_index + 1)
        return Impl_Node(her,e_node), index
    if tokens[start_index][0] == SSI[0]:
        e_node, index = E(tokens,start_index + 1)
        return Ssi_Node(her,e_node), index
    if tokens[start_index][0] in [CLOSE_PAR[0], END[0]]:
        return her, start_index

def get_parse_tree(tokens):
    root, index = E(tokens,0)
    if tokens[index][0] == END[0]:
        return root
    else:
        Exception('Unbalanced Parenthesis')

tokens = tokenize(s)
root = get_parse_tree(tokens)
root