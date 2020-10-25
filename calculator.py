def calculator_v1():
    while True:
        number1 = int(input('\ninput a number: '))
        method = input('do you want to multiply [*], divide [/], add [+} or subtract [-]: ')
        number2 = int(input('input a second number: '))

        subtract = f'the output is: {number1 - number2}\n'
        add = f'the output is: {number1 + number2}\n'
        multiply = f'the output is: {number1 * number2}\n'
        divide = f'the output is: {number1 / number2}\n'

        if method == '-':
            print(subtract)
        elif method == '+':
            print(add)
        elif method == '*':
            print(multiply)
        elif method == '/':
            print(divide)
        else:
            print("please input a valid method...")

        while True:
            repeat = input('do you wish to do another calculation [Y] [N]: ')
            repeat_upper = repeat.upper()
            if repeat_upper == 'Y':
                break
            elif repeat_upper == 'N':
                print("see you next time!")
                quit()
            else:
                print("please input a valid answer...")
