import re #importa o modulo regex

informacoes = 'O telefone do ususário é 98127-3909.' #frase que estamos procurando

                        #padrao             #onde procurar
resultado  = re.search(r'[0-9]+.[0-9]+', informacoes)

##se nao encontrarmos o padrao o resultado é none
if(resultado is not None):
    print(resultado.group(0))