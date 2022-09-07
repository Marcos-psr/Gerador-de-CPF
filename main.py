from tkinter import *
from validate_docbr import CPF, CNPJ

root = Tk()
cpf = CPF()
cnpj = CNPJ()

STEEL_BLUE = "#4682B4"


class Aplicattion:
    def __init__(self):
        self.root = root
        self.screen()
        self.entry()
        self.button()
        self.cpf = cpf
        self.cnpj = cnpj
        root.mainloop()

    def screen(self):
        self.root.configure(background=STEEL_BLUE)
        self.root.geometry("800x400")
        self.root.resizable(False, False)
        self.root.title("Gerador de Cadastros")

    def entry(self):
        self.label = Label(self.root, text="GERADOR DE CPF/CNPJ", background=STEEL_BLUE, font=("courier", 18, "bold"))
        self.label.place(relwidth=0.4, relx=0.3, rely=0.25)

        self.entrada = Entry(self.root, font=("arial", 18, "bold"), justify="center")
        self.entrada.place(relwidth=0.4, relheight=0.1, relx=0.3, rely=0.4)

    def button(self):
        self.button_cpf = Button(self.root, text="GERAR CPF", font=("verdana", 10, "bold"), command=self.generate_cpf)
        self.button_cpf.place(relwidth=0.15, relheight=0.08, relx=0.3, rely=0.6)

        self.button_cnpj = Button(self.root, text="GERAR CNPJ", font=("verdana", 10, "bold"),
                                  command=self.generate_cnpj)
        self.button_cnpj.place(relwidth=0.15, relheight=0.08, relx=0.55, rely=0.6)

    def generate_cpf(self):
        self.entrada.delete(0, END)
        self.entrada.insert(0, self.cpf.generate(True))

    def generate_cnpj(self):
        self.entrada.delete(0, END)
        self.entrada.insert(0, self.cnpj.generate(True))


if __name__ == "__main__":
    Aplicattion()