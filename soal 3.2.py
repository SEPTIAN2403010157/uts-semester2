from typing import List, Union

def evaluatePrefix(expression: List[str]) -> Union[int, str]:
    stack = stack ()
    operators = {"+", "-", "*", "/"}

    try:
        for token in reversed(expression):
            if token not in operators:
                stack.push(int(token))
            else:
                if stack.isEmpty():
                    return "Ekspresi tidak valid"
                a = stack.pop()

                if stack.isEmpty():
                    return "Ekspresi tidak valid"
                b = stack.pop()

                if token == '+':
                    stack.push(a + b)
                elif token == '-':
                    stack.push(a - b)
                elif token == '*':
                    stack.push(a * b)
                elif token == '/':
                    if b == 0:
                        return "Pembagian oleh nol tidak diperbolehkan"
                    stack.push(a // b)

        if stack.isEmpty() or len(stack.items) != 1:
            return "Ekspresi tidak valid"
        return stack.pop()

    except:
        return "Ekspresitidakvalid"
    
    print(evaluatePrefix(["+", "3", "*", "2", "2"]))   # Output: 7
print(evaluatePrefix(["*", "+", "1", "2", "3"]))   # Output: 9
print(evaluatePrefix(["-", "5"]))                  # Output: Ekspresi tidak valid
print(evaluatePrefix(["/", "8", "0"]))             # Output: Pembagian oleh nol tidak diperbolehkan