
'''
Q2: 
     Test your code using the following L-system (Cantor fractal) where n=3 and tell the answer:
variables : A B
constants : none
start  : A
rules  : (A → ABA), (B → BBB)

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

rules = {'A': 'ABA', 'B': 'BBB'}

lsystem = D(variables, axiom, rules)
n = 3
result = lsystem.produce(n)
print(f" n = {n} : S={result}")

# ANS :- n = 3 : S=ABABBBABABBBBBBBBBABABBBABA


