from driverutils import ChromeBot
from getpass import getpass
from time import sleep
import datetime
import os

GDRIVE_PATH = '/Volumes/GoogleDrive/My Drive/'
USE_CREDENTIALS_FILE = False
EXPORT_GDRIVE = False
EXPORT_GITHUB = True

# XPATHS
SIGNIN_XP = '//*[@id="gb"]/div/div[1]/a'
USERNAME_XP = '//*[@id="identifierId"]'
USER_NEXT = '//*[@id="identifierNext"]/div/button/div[2]'
PWD_XP = '//*[@id="password"]/div[1]/div/div[1]/input'
PWD_NEXT = '//*[@id="passwordNext"]/div/button/div[2]'

def google_login(c, use_credentials_file=False):
    if not use_credentials_file:
        email = input('Email: ')
        pwd = getpass('Senha: ')
    else:
        try:
            from credentials import get_credentials
            email, pwd = get_credentials()
        except:
            print("Failure when retrieving credentials")

    # Escrever usuario e clicar em next
    c.send_keys(USERNAME_XP, email)
    c.click(USER_NEXT)
    sleep(3)

    # Escrever senha e next
    c.send_keys(PWD_XP, pwd)
    c.click(PWD_NEXT)


def get_colab_code(chrome):
    # Get all codeblocks
    codeblocks = chrome.driver.find_elements_by_class_name('editor')

    # Convert codeblocks to text
    code = """\n\n""".join([cd.text for cd in codeblocks])

    return code

def colab_signin():
    c = ChromeBot()
    c.driver.implicitly_wait(10)
    c.driver.get('https://colab.research.google.com')

    c.click(SIGNIN_XP)
    sleep(3)
    google_login(c, USE_CREDENTIALS_FILE)

    # Wait for opening notebook material
    colab_url = input("Open notebook manually or input its url here. Then, press enter to continue: ")
    if colab_url!='':
        c.driver.get(colab_url)

    return c

def write_code(code, fpath='test.py'):
    with open(fpath, mode='w') as f:
        f.writelines(code)
        #f.write(code)

def export_github(code, fpath):
    write_code(code, fpath)
    os.system('git add output')
    os.system('git commit -m "update live code"')
    os.system('git push')


if __name__ == '__main__':
    # Get current date time as filename
    now = datetime.datetime.now()
    fname = now.strftime("%Y-%m-%d.py")

    # Start session and sign in to colab
    chrome = colab_signin()

    # Watch and export code
    try:
        print('Watching and exporting code...')
        while True:
            code = get_colab_code(chrome)
            if EXPORT_GDRIVE:
                write_code(code, fpath=GDRIVE_PATH+'/'+fname)

            if EXPORT_GITHUB:
                export_github(code, fpath= './output/'+fname)
            sleep(10)
    except:
        print("Execution has been interrupted")

    answer = input('Quit? (y/n)')
    if answer=='y':
        chrome.driver.quit()



