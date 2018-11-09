class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def conv2postfix(expression):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    #因为碰到了括号就需要压入堆栈，因此可以认为优先级最低
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = expression.split()
    operatorList = ["*", "/", "+", "-", "(", ")"]
    print(tokenList)

    for token in tokenList:
        #如果是操作数，直接追加到list中
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token.isdigit():
            postfixList.append(token)

        #if token not in operatorList:
        #    postfixList.append(token)

        #左括号，优先级低，直接压入堆栈
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            #如果碰到了右括号，需要将堆栈中的操作符弹出，追加到list中，直接碰到右括号
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            #对于其他操作符，如果堆栈不空，需要判断和堆栈中元素的优先级，
            #如果堆栈中的优先级大于当前扫描的操作符优先级，则弹出并追加到队列中
            #将当前扫描的操作符，压入堆栈
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    #将堆栈中的操作符全部弹出，追加到list中
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postEva(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token.isdigit():
            #将操作数压入堆栈
            operandStack.push(int(token))
        else:
            #对于运算符，弹出栈顶的两个元素，进行计算
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

if __name__ == '__main__':
    expression =  "A * B + C * D"
    expression = "( A + B ) * ( C + D )"
    expression = "10 + 3 * 5 / ( 16 - 4 )"
    postfix = conv2postfix(expression)
    print(postfix)
    res = postEva("70 8 + 3 2 + /")
    print(res)
