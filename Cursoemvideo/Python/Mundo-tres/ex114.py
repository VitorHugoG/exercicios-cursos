import urllib
import urllib.request

# tenta acessar a url usando o metodo urlopen da biblioteca urllib
try:
    site=urllib.request.urlopen('http://www.pudim.com.br/')
#um exceção padrão é o URLError 
except urllib.request.URLError:
    print('\033[033mO site pudim não está disponível no momento\033[m')
# se não tiver nenhuma exceção ele 
else:
    print('\033[34mO site pudim  está disponível no momento\033[m')