
from colorama import Fore, Style, init

init (autoreset = True)

nivel = 5
lista_de_cores = [Fore.WHITE, 
                  Fore.RED,     
                  Fore.YELLOW, 
                  Fore.GREEN, 
                  Fore.CYAN, 
                  Fore.BLUE]

lista_de_texto = ["Sem texto", 
                  "Nível do reservatório de água está muito baixo",
                  "Nível do reservatório de água está Baixo", 
                  "Nível do reservatório de água está médio" , 
                  "Nível do reservatório de água está alto", 
                  "Nível do reservatório de água está muito alto"]

def definir_cor(cor):
    cor_definida = lista_de_cores[cor]
    return cor_definida

cor_do_texto = definir_cor(nivel)

print(cor_do_texto + lista_de_texto[nivel])

print(Style.RESET_ALL)