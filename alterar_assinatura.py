import pickle
import os
############# Imports do cliente
import getpass
import re
from fuzzywuzzy import fuzz
import shutil
from datetime import datetime
import socket
##########################

class AlterarAssinatura:
    def __init__(self, arquivo):
        self.__arquivo = arquivo

    def decoder(self):
        with open(self.__arquivo, "rb")as arqui:
            arquivo = ""
            for x in pickle.load(arqui):
                arquivo += f"{x}\n"
        return arquivo
    
        

if __name__ == "__main__":
    programa = AlterarAssinatura("code.pickle")
    exec(programa.decoder())
