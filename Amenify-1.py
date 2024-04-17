
'''
Q1: 
     Write a function ‘produce’ that takes in the object of ‘D’ and ‘n’ and returns the L-systems string ‘S’.

'''
class D:
    def __init__(self, variables, axiom, rules):
        self.variables = variables
        self.axiom = axiom
        self.rules = rules
    
    def rule_application(self, axiom, n):
        result = list(axiom)  
        for _ in range(n):
            res = []
            for char in result:
                res.extend(self.rules.get(char, char))  
            result = res
        return ''.join(result)
    
    
    def produce(self, n):

        return self.rule_application(self.axiom, n)


variables = {'A', 'B'}

axiom = 'A'

rules = {'A': 'AB', 'B': 'A'}

lsystem = D(variables, axiom, rules)
n = 5
result = lsystem.produce(n)
print(f" n = {n} : S={result}")

# ANS:-  n = 5 : S=ABAABABAABAAB


