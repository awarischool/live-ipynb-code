from driverutils import ChromeBot
from getpass import getpass
from time import sleep
import datetime

BLACKBOARD_PATH = '/Volumes/GoogleDrive/My Drive/Awari DS - Turma Mai 20/_Live Code'
USE_CREDENTIALS_FILE = True
CREDENTIALS_TOKEN = 'abc'

# Colocando dentro de funcao para que variavel pwd nao fique salva no resto do programa
def google_login(c, use_credentials_file=False):

    if not use_credentials_file:
        email = input('Email: ')
        pwd = getpass('Senha: ')
    else:
        try:
            from credentials import get_credentials
            email, pwd = get_credentials(CREDENTIALS_TOKEN)
        except:
            print("Failure when retrieving credentials")

    # Escrever usuario e clicar em next
    c.send_keys('//*[@id="identifierId"]', email)
    c.click('//*[@id="identifierNext"]/div/button/div[2]')

    sleep(3)
    # Escrever senha e next
    c.send_keys('//*[@id="password"]/div[1]/div/div[1]/input', pwd)
    c.click('//*[@id="passwordNext"]/div/button/div[2]')

    # Verificar se há algum passo adicional
    input('Open notebook for class and press enter to continue')


def pegar_codigo(chrome):
    # Pegar blocos de códigos
    codeblocks = chrome.driver.find_elements_by_class_name('editor')

    # Converter todos os blocos para texto
    code = '\n\n'.join([cd.text for cd in codeblocks])

    return code

def colab_signin():
    c = ChromeBot()
    c.driver.implicitly_wait(10)
    c.driver.get('https://colab.research.google.com')
    # Clicar em sign in
    c.click('//*[@id="gb"]/div/div[1]/a')
    google_login(c, USE_CREDENTIALS_FILE)
    return c

def write_code(code, fpath='test.py'):
    with open(fpath, mode='w') as f:
        f.write(code)

if __name__ == '__main__':
    # Pegar data local
    now = datetime.datetime.now()
    fname = now.strftime("%Y-%m-%d.py")

    # Iniciar sessão e logar no colab
    chrome = colab_signin()

    # Loop para vigiar e exportar código
    try:
        print('Iniciando loop para vigiar e exportar código')
        while True:
            code = pegar_codigo(chrome)
            write_code(code, fpath=BLACKBOARD_PATH+'/'+fname)
            sleep(10)
    except:
        print("Execution has been interrupted")

    answer = input('Quit? (y/n)')
    if answer=='y':
        chrome.driver.quit()



