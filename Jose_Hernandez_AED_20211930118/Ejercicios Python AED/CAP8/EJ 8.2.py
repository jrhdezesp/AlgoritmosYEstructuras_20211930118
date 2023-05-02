from BinaryTree import *


def build_expression_tree(postfix_expression):
    operand_stack = []
    operators = set('+-*/')
    for token in postfix_expression.split():
        if token.isdigit():
            operand_stack.append(BinaryTree(token))
        elif token in operators:
            right_tree = operand_stack.pop()
            left_tree = operand_stack.pop()
            new_tree = BinaryTree(token, right=operand_stack.pop(), left=operand_stack.pop())

            operand_stack.append(new_tree)
        else:
            raise ValueError('Invalid token: ' + token)
    if len(operand_stack) != 1:
        raise ValueError('Invalid expression')
    return operand_stack[0]

def postorder_traversal(tree):
    if tree is None:
        return ''
    return postorder_traversal(tree.left_child) + postorder_traversal(tree.right_child) + str(tree.key) + ' '

def inorder_traversal(tree):
    if tree is None:
        return ''
    if tree.is_leaf():
        return str(tree.key)
    return '(' + inorder_traversal(tree.left_child) + ' ' + str(tree.key) + ' ' + inorder_traversal(tree.right_child) + ')'

def preorder_traversal(tree):
    if tree is None:
        return ''
    return str(tree.key) + ' ' + preorder_traversal(tree.left_child) + preorder_traversal(tree.right_child)

if __name__ == '__main__':
    postfix_expression = '3 4 + 5 * 6 -'
    expression_tree = build_expression_tree(postfix_expression)

    print('Postorder traversal:', postorder_traversal(expression_tree))
    print('Inorder traversal:', inorder_traversal(expression_tree))
    print('Preorder traversal:', preorder_traversal(expression_tree))

