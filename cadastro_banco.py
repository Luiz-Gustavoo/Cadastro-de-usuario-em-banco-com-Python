print('          BEM VINDO AO BANCO PyCASH          ')
print('-' * 50)

print('')

print('sim = criar conta')
print('não = não criar conta')
print('')

input_criar_conta_valido = False

while input_criar_conta_valido == False:

    input_criar_conta = input('Você deseja criar uma conta no nosso banco? escolha de acordo com as opções acima: ')
    if input_criar_conta == 'sim':
        print('Ótimo! vamos começar o seu cadastro!')
        input_criar_conta_valido = True
        print('-'* 50)
        print('Vamos precisar de algumas informações suas')

        nome_valido = False
        while nome_valido == False:
            nome = input('Digite o seu nome: ')

            print('')

            if nome.isalpha():
                nome_valido = True
                print('Olá {}!. Vamos para a próxima parte.'.format(nome))
            else:
                print('Digite apenas letras')
                continue

        print('')
        print('-' * 50)
        print('Lembre-se que é preciso ser maior de idade para abrir conta :)')

        idade_valida = False
        while idade_valida == False:
            
            idade = input('Digite a sua idade: ')
            if idade.isnumeric():
                idade_int = int(idade)
                
                if type(idade_int) == int:
                    print('ok')
                
                if idade_int >= 18:
                    print('Você é maior de idade e pode se cadastrar! ')
                    print('Agora só falta um passo! ')
                    ano_nascimento_valida = True
                else:
                    print('Não é possível se cadastrar sendo menor de idade :(')
                    break
            else:
                print('Digite apenas números')    
                continue
            

           


    elif input_criar_conta == 'não':
        print('Que pena :( ... estaremos aqui caso mude de ideia')
        iinput_criar_conta_valido = True
        print('Criação de conta cancelada')
        break

    else:
        input_criar_conta_valido = False
        print('Digite apenas de acordo com as opções acima')
