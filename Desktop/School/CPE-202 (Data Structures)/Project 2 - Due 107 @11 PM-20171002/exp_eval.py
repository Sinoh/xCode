# Jeffery Ho
# CPE 202

from Stacks import StackArray


# A infix_to_postfix is a string
# A infixexpr is a string
# a string containing an infix expression where tokens are space separated is
# the single input parameter and returns a string containing a postfix expression
# where tokens are space separated''
# self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
# self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
# self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 - 2 +")
# self.assertEqual(infix_to_postfix("6 ^ 3 ^ 2"), "6 3 2 ^ ^")
# self.assertEqual(infix_to_postfix("6 * ( 3 + 2 )"), "6 3 2 + *")
# def infix_to_postfix(infixexpr):
#       op_Order ={}
#       op_Stack = StackArray(30)
#       postfixList = []
#       tokenList = infixexpr.split()
#       for token in tokenList:
#           ...
#       return ' '.join(postfixList)
def infix_to_postfix(infixexpr):
    '''Converts an infix expression to an equivalent postfix expression '''

    '''Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated'''


    op_Order = {}
    op_Order['^'] = 4
    op_Order['*'] = 3
    op_Order['/'] = 3
    op_Order['+'] = 2
    op_Order['-'] = 2
    op_Order['('] = 1

    op_Stack = StackArray(30)
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token.isdigit():
            postfixList.append(token)
        elif token == '(':
            op_Stack.push(token)
        elif token == ')':
            top = op_Stack.pop()
            while top != '(':
                postfixList.append(top)
                top = op_Stack.pop()
        else:
            while  op_Stack.is_empty() == False and op_Order[op_Stack.peek()] >= op_Order[token]:
                if op_Order[op_Stack.peek()] == op_Order[token] == 4:
                    break
                else:
                    postfixList.append(op_Stack.pop())
            op_Stack.push(token)

    while not op_Stack.is_empty():
        postfixList.append(op_Stack.pop())

    return ' '.join(postfixList)


# A postfix_eval is a number
# A postfixExpr is a string
# Take in postfixExpr as a string containing a postfix expression and
# evaluates the expression in a postfix operation and returns the result
# self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
# self.assertAlmostEqual(postfix_eval("3 5 -"), -2)
# self.assertAlmostEqual(postfix_eval("3 5 *"), 15)
# self.assertAlmostEqual(postfix_eval("5 5 /"), 1)
# self.assertAlmostEqual(postfix_eval("3 2 ^"), 9)
# def postfix_eval(postfixExpr):
#     op_Stack = StackArray(30)
#     tokenList = postfixExpr.split()
#     for token in tokenList:
#         ...
#     return op_Stack.pop()
def postfix_eval(postfixExpr):
    '''Evaluates the postfix expression and returns the value '''
    op_Stack = StackArray(30)

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token.isdigit():
            op_Stack.push(int(token))
        else:
            operand2 = op_Stack.pop()
            operand1 = op_Stack.pop()
            if operand2 == 0 and token == '/':
                raise ValueError
            result = doMath(token, operand1, operand2)
            op_Stack.push(result)

    return op_Stack.pop()

# A doMath is a number
# a op is an operand
# a op1 is a number
# a op2 is a number
# Takes three parameters, all strings as an operand and two numbers and
# operates on the two numbers based on the operand
# self.assertAlmostEqual(postfix_eval(+, 3, 5), 8)
# self.assertAlmostEqual(postfix_eval(-, 3, 5), -2)
# self.assertAlmostEqual(postfix_eval(*, 3, 5), 15)
# self.assertAlmostEqual(postfix_eval(/, 5, 5), 1)
# self.assertAlmostEqual(postfix_eval(^, 3, 2), 9)
# def doMath(op, op1, op2):
#     if op == '^':
#         ...
#     if op == '*':
#         ...
#     if op == '/':
#         ...
#     if op == '+':
#         ...
#     if op == '-':
#         ...
def doMath(op, op1, op2):
    '''Operates on the two operands based on the operator and returns the result '''
    if op == '^':
        return op1 ** op2
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2

# A postfix_valid is a boolean
# a postfixexpr is a string
# Takes in an parameter as a string and checks if it is a valid postfix expression
# self.assertFalse(postfix_valid(""))
# self.assertFalse(postfix_valid("2 3"))
# self.assertTrue(postfix_valid("2 3 +"))
# self.assertTrue(postfix_valid("2 3 -"))
# self.assertTrue(postfix_valid("2 3 *"))
# self.assertTrue(postfix_valid("2 3 /"))
# def postfix_valid(postfixexpr):
#     ops = '+-/*^'
#     for token in ops:
#         ...
def postfix_valid(postfixexpr):
    '''Checks to if the postfix expression is a valid postfix expression '''
    ops = '+-/*^'
    num = False
    op = False
    for token in ops:
        if token in postfixexpr:
            op = True
    for token in postfixexpr:
        if token.isdigit():
            num = True

    return num and op

