class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.head.data
        self.head = self.head.next
        return popped_value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

def precedence(op):
    if op == '^':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0

def is_operator(c):
    return c in {'+', '-', '*', '/', '^'}

def infix_to_postfix(infix_expression):
    stack = Stack()  
    postfix = []  

    for char in infix_expression:
        if char.isalpha():
            postfix.append(char)

        elif char == '(':
            stack.push(char)

        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  

    
        elif is_operator(char):
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(char)):
                postfix.append(stack.pop())
            stack.push(char)


    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)  


if __name__ == "__main__":
    infix_expression = input().strip()
    postfix_expression = infix_to_postfix(infix_expression)
    print(postfix_expression)
