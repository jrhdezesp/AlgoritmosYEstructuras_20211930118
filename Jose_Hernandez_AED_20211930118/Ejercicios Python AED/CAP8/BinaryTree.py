class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if self.value is None:
            return ''
        if self.left is None and self.right is None:
            return str(self.value)
        left_str = str(self.left) if self.left else ''
        right_str = str(self.right) if self.right else ''
        return f'({left_str} {self.value} {right_str})'


def build_expression_tree(postfix_expression):
    operand_stack = []
    for token in postfix_expression.split():
        if token.isnumeric():
            operand_stack.append(BinaryTree(int(token)))
        else:
            right = operand_stack.pop()
            left = operand_stack.pop()
            operand_stack.append(BinaryTree(token, left, right))
    if len(operand_stack) != 1:
        raise ValueError('Invalid postfix expression')
    return operand_stack.pop()


postfix_expression_list = [
    '91 95 + 15 + 19 + 4 *',
    'B B * A C 4 * * -',
    '42',
    'A 57 ',
    '+ /',
]

for postfix_expression in postfix_expression_list:
    try:
        expression_tree = build_expression_tree(postfix_expression)
        print(postfix_expression, '->', expression_tree)
    except Exception as e:
        print(postfix_expression, '->', "Invalido" )
