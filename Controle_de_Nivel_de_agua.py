
# Fore: define a cor da fonte | Style: permite resetar tudo | init: liga as cores no Windows
# colorama = biblioteca para altera cores no terminal
from colorama import Fore, Style, init

# No Windows, init() liga o "tradutor" de cores
init () # sem essa linha a menssagem não fica colorida

nivel = 2 # Níveis aceitos: de 1 a 5

""" Lista de cores correspondentes a cada nível, foi colocada uma cor aleatória no indice 0 
    apenas para que os outros indices coincidicem com o número do nível"""""
lista_de_cores = [Fore.WHITE, 
                  Fore.RED,     
                  Fore.YELLOW, 
                  Fore.GREEN, 
                  Fore.CYAN, 
                  Fore.BLUE]

# Lista de mensagens de status para cada nível
lista_de_texto = ["Reservatório em manutenção", 
                  "Nível do reservatório de água está muito baixo",
                  "Nível do reservatório de água está Baixo", 
                  "Nível do reservatório de água está médio" , 
                  "Nível do reservatório de água está alto", 
                  "Nível do reservatório de água está muito alto"]

# Função que recebe o nível e retorna a cor configurada na lista.
# Foi criada essa função pois é um pré requisito da atividade
def definir_cor(cor):
    cor_definida = lista_de_cores[cor]
    return cor_definida

# Chama a função para obter a cor baseada na variável 'nivel'
cor_do_texto = definir_cor(nivel)

# Exibe a mensagem colorida no terminal
print(cor_do_texto + lista_de_texto[nivel])

print(Style.RESET_ALL) # Reseta as cores do terminal