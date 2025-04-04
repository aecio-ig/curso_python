while True: 
    try:
        numero1= input('Digite um numero: ')
        try:
            numero1 = float(numero1)
        except:
            raise Exception('Informe um numero valido pingoludo')

        numero2= input('Digite um numero: ')
        try:
            numero2 = float(numero2)
        except:
            raise Exception('Informe um numero valido candango')

        operador = input('Infome um operador (+ - / * **): ')
        if operador not in ['+', '-', '/' , '*' , '**']:
            raise Exception('Ta de brincation cara?')
        
        resultado = None
        match(operador):
            case('+'):
                resultado = numero1 + numero2
            case('-'):
                resultado = numero1 - numero2
            case('/'):
                resultado = numero1 / numero2
            case('*'):
                resultado = numero1 * numero2
            case('**'):
                resultado = numero1 ** numero2

        print(f'Resultado é: {resultado}')
    except Exception as e:  
        print(e)
        break
    