numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

senha_valida = False
while senha_valida == False:    # senha da conta do cliente e verificando se a senha está de acordo com as regras 
    input_senha = input('Crie sua senha: ')
    if len(input_senha) >= 7:
        print('Quantidade de caracteres ok')

        tem_numero = ''      
        for numero_digitado in input_senha:
            if numero_digitado in numeros:
                print('numero ok')
                break
            else:
                tem_numero = 'Sua senha não tem números'
        print(tem_numero)
        continue
                  
                       
                    
                          
                            
                                
                    
                    
                    
    else:
                print('Quantidade de caracteres insuficiente' )
                continue