import shutil # pacote para copiar e mover arquivos

# Cria arquivo ou sobreescreve caso ja exista - parametro 'w' (Parametro 'a', atualiza o arquivo mas não recria)

#############################################
## Exercicio 1

# arquivo = open('teste.txt', 'a')
#
# arquivo.write('Minha primeira escrita')
# arquivo.write('\nMinha Segunda escrita')
# arquivo.write('\nMinha Terceira escrita')
# arquivo.close()

#############################################
## Exercicio 2

# def escrever_arquivo(texto):
#
#     #diretorio = 'C:/projetos/teste/arquivo.txt'
#     #arquivo = open(diretorio, 'w')
#
#     arquivo = open('teste.txt', 'w')
#     arquivo.write(texto)
#     arquivo.close()
#
# def atualizar_arquivo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()
#
# def ler_arquivo(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r')
#     texto = arquivo.read()
#     print(texto)
#
# if __name__ == '__main__':
#
#     #escrever_arquivo('Primeira Linha.\n')
#     #atualizar_arquivo('Segunda Linha.\n')
#     ler_arquivo('teste.txt')


#############################################
## Exercicio 3

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/facci/Downloads')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/facci/Downloads')

##########################################################
if __name__ == '__main__':

    # escrever_arquivo('Primeira Linha.\n')
    # atualizar_arquivo('Segunda Linha.\n')
    # ler_arquivo('teste.txt')

    #aluno = 'Rafael, 10,10,5,5'
    #atualizar_arquivo('notas.txt',aluno)

    ##lista_media = media_notas('notas.txt')
    ##print(lista_media)

    #copia_arquivo('notas.txt')
    #move_arquivo('notas.txt')