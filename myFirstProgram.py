print('Hello World')

# Meu primeiro programa em python...
# Praticando: definição de função, try/except e condicional simples...
# A primeira linha precisa ser Hello World se não dá azar.
def sumOfTwoNumbers():
    try:
        num1 = float(input('Input your first number: '))
        num2 = float(input('Input your second number: '))
    except:
        num1 = 'invalid'
        num2 = 'invalid'

    result = num1 + num2
            
    try:
        if type(result) != float:
            print('Error! Try to use valid numbers.')
        else:
            print(result)
    except:
        print('#')    

sumOfTwoNumbers()
