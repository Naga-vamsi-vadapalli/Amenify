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

The time complexity of the provided implementation is O(n * m * k), where:
n is the number of iterations specified by the produce method,
m is the length of the axiom string, and
k is the average number of rules applied to each character.

The space complexity of the provided rule_application method is O(m), where m is the length of the resulting string after applying the rules.
Despite the nested loop structure and iterative nature of the algorithm, the space complexity remains linear with respect to the size of the input axiom string.
The space complexity is not multiplied by the number of iterations (n) since only one intermediate list (res) is maintained in memory at any given time, and memory is reused throughout the function execution.
Therefore, the space complexity for this implementation is O(m), where m is the length of the resulting string after applying the rules
'''



class D:
    def __init__(self, variables, axiom, rules):
        self.variables = variables
        self.axiom = axiom
        self.rules = rules
    
    def rule_application(self, axiom, n):
        result = axiom

        for _ in range(n):
            next_state = []

            for char in result:

                next_state.append(self.rules.get(char, char))
            result = ''.join(next_state)
        return result
    
    def produce(self, n):
        return self.rule_application(self.axiom, n)


variables = {'A', 'B'}

axiom = 'A'

rules = {'A': 'ABA', 'B': 'BBB'}

lsystem = D(variables, axiom, rules)
n = 3
result = lsystem.produce(n)
print(f" n = {n} : S={result}")


# n = 3 : S=ABABBBABABBBBBBBBBABABBBABA
'''
The space complexity of the provided rule_application method is O(m), where m is the length of the resulting string after applying the rules.
Despite the nested loop structure and iterative nature of the algorithm, the space complexity remains linear with respect to the size of the input axiom string.
The space complexity is not multiplied by the number of iterations (n) since only one intermediate list (res) is maintained in memory at any given time, and memory is reused throughout the function execution.

The time complexity of the modified implementation is O(n * m), where:
n is the number of iterations specified by the produce method, and
m is the length of the axiom string.

'''