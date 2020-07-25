# Jupyter and Google Colab Live Coding
Educational tool for displaying code from Jupyter (under development) and Google Colab environments in almost real time.

## Google Colab Instructions

1. Fork this repository
2. (Optional) Add a `credentials.py` with a `get_credentials()` functions that returns your Google Colab username and password. The `credentials.py` is already being ignored by `.gitignore`. As a suggestion, use keyring for storing your password:
```
"""
# Template of credentials.py file
Firstly, install keyring: 
$ pip install keyring

Next, store your password in your system using:
>>> import keyring
>>> keyring.set_password("system", "username@gmail.com", "password")

Make sure to replace username with your colab email address. Finally, the password can be accessed using:
>>> keyring.get_password("system", "username")
"""
my_username = "username@gmail.com"
def get_credentials():
    pwd = keyring.get_password("system", my_username)
    return my_username, pwd
```
3. Run the `colab.py` file:
```
$ python colab.py
```
4. You will be asked to open the ipynb file that you would like to live share. **Is case the 'credentials.py' file is not present, you will also be asked to login manually on google colab**. Check the source code for further info. 

5. The live code will be pushed to the output folder in this repository every 10 seconds with the name pattern: YEAR-MONTH-DAY.py
