def solution(expression):
    input_str = expression
    num = ''
    numbers = []
    operators = []
    for i in input_str:
        if i in ["*","+","-"]:
            numbers.append(int(num))
            num = ''
            operators.append(i)
        else:
            num += i
    numbers.append(int(num))

    def calculate(numbers,operators,priority):
        for op in priority:
            while op in operators:
                idx = operators.index(op)
                result = eval(f"{numbers[idx]}{op}{numbers[idx+1]}")
                numbers[idx] = result
                del numbers[idx+1]
                del operators[idx]
        return abs(numbers[0])

    priorities = [["*","+","-"],["*","-","+"],["+","*","-"],["+","-","*"],["-","+","*"],["-","*","+"]]

    answer = 0
    for priority in priorities:
        answer = max(answer,calculate(numbers[:],operators[:],priority))

    return answer

print(solution("100-200*300-500+20"))