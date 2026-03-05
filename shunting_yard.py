class ExpressionError(Exception): 
    pass
# Erreur liée a une expression mathématique mal formulée

def tokenize(expression):  
    # Transforme expression en liste de tokens
    tokens = []
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch == " ": 
            i += 1 
            continue

        if ch == "(" or ch == ")": 
            tokens.append(ch) 
            i += 1
            continue
        if ch in "+-*/": 
            if ch == "-" and (i == 0 or (len(tokens) > 0 and (tokens[-1] in "+-*/(")))  :
                # Lire des nombres négatifs
                i += 1 # on saute le "-"

                if i >= len(expression) : 
                    raise ExpressionError("Expression invalide : '-' tout seul")
                #  Après le "-" on doit avoir un chiffre ou un point 
                if not (expression[i].isdigit() or expression[i] == "."): 
                    raise ExpressionError("Expression invalide :") 
            tokens.append(ch)
            i += 1 
            continue 

        # Lecture des nombres (et caractères)
        if ch.isdigit() or ch == "." : 
            start = i
            dot_count = 0  
            
            while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                if expression[i] == ".": 
                    dot_count += 1 
                if dot_count > 1: 
                    raise ExpressionError("Nombre mal formé : ")
                i += 1 

            nombre = expression[start:i]
            tokens.append(nombre)
            continue

        # opérateur invalide
        raise ExpressionError("Caractère invalide : " + ch)
            
    return tokens 


            
print(tokenize("-3.14+2"))
print(tokenize("2*-4"))
print(tokenize("7-2"))
print(tokenize("(-5+1)"))           
print(tokenize("3+4")) # Doit afficher les nombres 3 et 4 séparés   

def infix_to_postfix(tokens):
        output = []
        stack =[] 

        precedence = {
             "+" : 1,
             "-" : 1,
             "*" : 2,
             "/" : 2, 
        }
        for token in tokens: 
             if token not in "+-*/()": 
                  output.append(token)

             elif token in "+-*/":
                  while stack and stack[-1] in "+-*/" and precedence[stack[-1]] >= precedence[token]: 
                       output.append(stack.pop())

                       stack.append(token)
                    
             elif token == "()" :
                  stack.append(token)

             elif token == ")":
                  
                  while stack and stack[-1] != "(": 
                       output.append(stack.pop())
                       if not stack:
                            raise ExpressionError("Parentheses mal équilibrées : ")
                       
                       stack.pop()
                    
                  while stack:
                    if stack[-1] in "()":
                        raise ExpressionError("Parenthèses non appariées")
                    output.append(stack.pop())
        return output

tokens = tokenize("3+4*2")
print(infix_to_postfix(tokens))          
                  

    # Transforme une expression infix to postfix (shunting_yard)

def evaluate_postfix(tokens):
    stack = []

    for token in tokens:

        if token not in "+-*/":
            # token transform/ en string en float
            try:
                value = float(token)
            except ValueError:
                raise ExpressionError("Nombre invalide: " + token)

            stack.append(value)
            continue

        # token est un opérateur
        if len(stack) < 2:
            raise ExpressionError("Expression invalide: pas assez d'opérandes")

        b = stack.pop()
        a = stack.pop()

        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        elif token == "*":
            stack.append(a * b)
        elif token == "/":
            if b == 0:
                raise ExpressionError("Division par zéro")
            stack.append(a / b)

    if len(stack) != 1:
        raise ExpressionError("Expression invalide")

    return stack[0]

expr = "3+4*2/(1-5)"
t = tokenize(expr)
p = infix_to_postfix(t)
print("TOKENS:", t)
print("POSTFIX:", p)
print("RESULT:", evaluate_postfix(p))


