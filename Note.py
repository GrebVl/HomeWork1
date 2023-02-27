import datetime
from datetime import *

class Note:

    def __init__(self, titl, msg):
        self.titl = titl
        self.dat = datetime.today().strftime("%d/%m/%Y - %H.%M.%S")
        self.msg = msg

    def set_titl(self, titl):
        self.titl = titl
        self.dat = datetime.today().strftime("%d/%m/%Y - %H.%M.%S")

    def get_titl(self):
        return self.titl

    def set_dat(self, dat):
        self.dat = dat

    def get_dat(self):
        return self.dat

    def set_msg(self, msg):
        self.msg = msg
        self.dat = datetime.today().strftime("%d/%m/%Y - %H.%M.%S")

    def get_msg(self):
        return self.msg

    def display_info(self):
        print(f"date: {self.dat}\nName: {self.titl}\nmsg: {self.msg}\n")

    def titl_info(self):
        return f"date: {self.dat}\n  Name: {self.titl}"
