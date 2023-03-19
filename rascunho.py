"""
arquivo para testar possibilidades
"""
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

senha_valida = False
while senha_valida == False:    # senha da conta do cliente e verificando se a senha está de acordo com as regras 
    tem_numero = False
    tem_simbolo = False

    input_senha = input('Crie sua senha: ')
    if len(input_senha) >= 7:
                                       
        for numero_digitado in input_senha: # verificando numeros na senha
            if numero_digitado in numeros:
                tem_numero = True
                break                    
            else:
                tem_numero = False
                  
            for simbolo_digitado in input_senha: #  verificando simbolos na senha
                if simbolo_digitado in simbolos:
                    tem_simbolo = True                                                     
                    break                                   
                else:
                    tem_simbolo = False

        if tem_numero and tem_simbolo == True: # caso a condição for verdadeira, a senha está válida                  
            print('tudo ok')
            senha_valida = True
        else:
            if tem_numero == False:
                print('Não há números na sua senha')
                continue
            if tem_simbolo == False:
                print('Não há símbolos na sua senha')
                continue
                                        
                

















"""
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

senha_valida = False
while senha_valida == False:    # senha da conta do cliente e verificando se a senha está de acordo com as regras 
            input_senha = input('Crie sua senha: ')
            
            tem_numero = False
            tem_simbolo = False
            if len(input_senha) >= 7:
                print('Quantidade de caracteres ok')
                    
                    
                for numero_digitado in input_senha: # verificando numeros na senha
                    if numero_digitado in numeros:
                        tem_numero = True
                        print('numero ok')
                        break                    
                    else:
                         tem_numero = False

                    
                for simbolo_digitado in input_senha: #  verificando simbolos na senha
                    if simbolo_digitado in simbolos:
                        tem_simbulo = True
                        print('simbolo ok')                                  
                        break
                                    
                    else:
                     tem_simbolo = False
                                    
                
                    
                    
"""