def sum(a, b):
    return float(a) + float(b)

def sub(a, b):
    return float(a) - float(b)

def mult(a, b):
    return float(a) * float(b)

def div(a, b):
    return float(a) / float(b)

def exp(a, b):
    return float(a) ** float(b)


def __main__():
    print("This is a Simple Calculator™")
    while(1):
        n1 = input("First number\n")
        symbol = input("Enter symbol (+ , - , *, /, ^)\n")
        n2 = input("Second number\n")
        if (symbol == '+'):
            result = sum(n1, n2)
        if (symbol == '-'):
            result = sub(n1, n2)
        if (symbol == '*'):
            result = mult(n1, n2)
        if (symbol == '/'):
            result = div(n1, n2)
        if (symbol == '^'):
            result = exp(n1, n2)
        else:
            print("invalid input")
            return
        print(result)
        return
        
__main__(); 