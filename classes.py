
class Formula:
    def __init__(self, expression, value):
        self.expression = expression
        self.value = value

    def __str__(self):
        return f"{self.expression} = {self.value}"

    def __and__(self, other):
        if isinstance(other, Formula):
            return Formula(f"({self.expression} & {other.expression})", self.value and other.value)
        raise ValueError("La operación solo es válida con otra instancia de Formula")

    def __or__(self, other):
        if isinstance(other, Formula):
            return Formula(f"({self.expression} | {other.expression})", self.value or other.value)
        raise ValueError("La operación solo es válida con otra instancia de Formula")

    def __invert__(self):
        if self.expression[0] == "~":
            return Formula(f"{self.expression[1:]}", not self.value)
        return Formula(f"~{self.expression}", not self.value)

    def __eq__(self, other):
        if isinstance(other, Formula):
            return self.value == other.value
        return False

    def __rshift__(self, other):
        if isinstance(other, Formula):
            return Formula(f"({self.expression} >> {other.expression})", (not self.value) or other.value)
        raise ValueError("La operación solo es válida con otra instancia de Formula")


#a = Formula("A", True)
#b = Formula("B", False)
#c = Formula("C", True)
#
#f1 = a & b
#f2 = a | b
#f3 = ~a
#f4 = a >> b
#f5 = a & b | c
#f6 = f5 & a
#f7 = f5 | b
#f8 = ~f5
#f9 = f5 >> a
#f10 = ~f8
#
#print("f1 ",f1)  # (A & B) = False
#print("f2 ",f2)  # (A | B) = True
#print("f3 ",f3)  # ~A = False
#print("f4 ",f4)  # (A >> B) = False
#print("f5 ",f5)  # (A & (B | C)) = True
#print("f6 ",f6)  # ((A & (B | C)) & A) = True
#print("f7 ",f7)  # ((A & (B | C)) | B) = True
#print("f8 ",f8)  # ~(A & (B | C)) = False
#print("f9 ",f9)  # ((A & (B | C)) >> A) = True
#print("f10 ",f10) # ~~(A & (B | C)) = True




