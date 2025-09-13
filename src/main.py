from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from webbrowser import open

# ---------------------------------------------------
# funcoes

# funcao para calcular o imc e indicar o peso ideal
def calcular():
    lbl_ideal.place(x=20, y=120)
    lbl_tabela.place(x=20, y=50)
    lbl_res.place(x=20, y=20)
    try:
        nomec = str(ent_nome.get())
        pesoc = float(ent_peso.get())
        alturac = float(ent_altura.get())
    except:
        messagebox.showerror('ERRO', 'Preencha Peso e Altura!!\nUse PONTO no Peso ou Altura!\nEx:  Peso: 60.45    Altura: 1.75')
    else:
        imc = pesoc / alturac ** 2
        pmin = 18.7 * (alturac ** 2)
        pmax = 24.9 * (alturac ** 2)
        if nomec == '':
            nomec = '<desconhecido>'
        resultado.set(f'{nomec}, o seu IMC é {imc:.1f} kg/m²')
        if imc <= 16.99:
            tabela.set(f'Você está muito abaixo do peso.\nDe acordo com sua altura o seu\npeso deveria ser no mínimo {pmin:.1f} kg.')
        elif 17 <= imc <= 18.59:
            tabela.set(f'Você está abaixo do peso.\nDe acordo com sua altura o seu\npeso deveria ser no mínimo {pmin:.1f} kg.')
        elif 18.6 <= imc <= 24.99:
            tabela.set('Parabéns! você está no peso ideal.\n')
        elif 25 <= imc <= 29.99:
            tabela.set(f'Você está levemente acima do peso e \ndeveria emagrecer no minimo {pesoc - pmax:.1f} kg.')
        elif 30 <= imc <= 34.99:
            tabela.set(f'Você está com obsidade grau I e \ndeveria emagrecer no minimo {pesoc - pmax:.1f} kg.')
        elif 35 <= imc <= 39.99:
            tabela.set(f'Você está com obsidade grau II e \ndeveria emagrecer no minimo {pesoc - pmax:.1f} kg. \n')
        else:
            tabela.set(f'Você está com obsidade grau III e \ndeveria emagrecer no minimo {pesoc - pmax:.1f} kg.')
        ideal.set(f'Seu peso ideal pode variar \nentre {pmin:.1f} kg e {pmax:.1f} kg.')


# funcao para limpar os campos de calculo
def limpar():
    ent_nome.delete(0, END)
    ent_peso.delete(0, END)
    ent_altura.delete(0, END)
    ent_nome.focus()
    lbl_res.place(x=999)
    lbl_ideal.place(x=999)
    lbl_tabela.place(x=999)


# funcao para abrir outra janela com a tabela imc
def mostrartabela():
    mtabela = Toplevel()
    mtabela.geometry('515x380+340+100')
    mtabela.title('TABELA IMC')
    mtabela.resizable(0, 0)
    mtabela['bg'] = '#80aaff'
    tbl_lbl = Label(mtabela, image=tabelaimc)
    tbl_lbl.place(x=0, y=10)

    def sairtbl():
        mtabela.destroy()

    btn_sair = ttk.Button(mtabela, text='Sair', command=sairtbl).place(x=230, y=354)



# funcao para abrir outra tela com as informacoes do imc
def oque():
    txtq = 'O índice de massa corporal (IMC) é um cálculo feito\nde acordo com o peso e a altura de uma pessoa.\nO mesmo tem como objetivo avaliar se o peso de um\nindivíduo está acima do proposto para sua altura.\nAtravés do IMC também pode ser medida a magreza,\nentretanto, seu maior foco é avaliar a obesidade.'
    que = Toplevel()
    que.title('IMC - O Que É:')
    que['bg'] = '#80aaff'
    que.geometry('440x200+380+150')
    lblq = Label(que, text=txtq, font=fontepad, justify=LEFT, bg='#80aaff')
    lblq.place(x=5, y=20)

    def sairq():
        que.destroy()
    btn_sairq = ttk.Button(que, text='Sair', command=sairq).place(x=210, y=170)
    btn_saiba = ttk.Button(que, text='Saiba mais', command=lambda: open('https://www.tuasaude.com/imc/')).place(x=130, y=170)


# funcao para abrir outra tela com as informacoes de como calcular o imc
def comocalcular():
    txtcalc = '''O cálculo do IMC é feito da seguinte forma: 
divide-se o peso pela altura ao quadrado.
Exemplo: Se o seu peso é 80 kg e sua altura é 1,80m, 
a fórmula para calcular o IMC ficará:
IMC = 80/ 1,80²
IMC = 80/ 3,24
IMC = 24,69
De acordo com a tabela do IMC, você está no peso ideal.'''
    como = Toplevel()
    como.title('IMC - Como Calcular:')
    como['bg'] = '#80aaff'
    como.geometry('465x210+360+150')
    lblc = Label(como, text=txtcalc, font=fontepad, justify=LEFT, bg='#80aaff')
    lblc.place(x=5, y=15)

    def sairc():
        como.destroy()
    btn_sairc = ttk.Button(como, text='Sair', command=sairc).place(x=230, y=180)
    btn_saiba = ttk.Button(como, text='Saiba mais', command=lambda: open('https://siteantigo.portaleducacao.com.br/conteudo/artigos/educacao-fisica/calculo-de-massa-corporal-como-funciona/48547')).place(x=120, y=180)


# funcao para sair do programa principal
def sair():
    root.destroy()


# ---------------------------------------------------
# GUI
root = Tk()
root.title('Calculadora IMC - by[Pedro Barreto]')
root.geometry('350x350+430+100')
root.resizable(0, 0)
root.iconbitmap(default='_img/cal.ico')
resultado = StringVar()
tabela = StringVar()
ideal = StringVar()
corfundo = '#80aaff'
fontepad = ('Century Gothic'), 12, 'bold'
tabelaimc = PhotoImage(file='_img/tabela.png')
btncalc = PhotoImage('_img/calc.png')
# ---------------------------------------------------
# Menu
abas = Menu(root)

tab = Menu(abas, tearoff=0)
tab.add_command(label='Tabela IMC', command=mostrartabela)
tab.add_command(label='O que é', command=oque)
tab.add_command(label='Como calcular', command=comocalcular)
abas.add_cascade(label='Informações', menu=tab)
abas.add_command(label='Sair', command=sair)

# ---------------------------------------------------
# widgets
frame_sup = Frame(root, bg=corfundo, width=350, height=150, relief='raised')
frame_sup.pack()
frame_inf = Frame(root, bg=corfundo, width=350, height=200, relief='raised', highlightthickness=1)
frame_inf.pack()

lbl_nome = Label(frame_sup, text='Nome:', bg=corfundo, font=fontepad)
lbl_nome.place(x=40, y=40)

lbl_peso = Label(frame_sup, text='Peso:', bg=corfundo, font=fontepad)
lbl_peso.place(x=40, y=65)

lbl_altura = Label(frame_sup, text='Altura:', bg=corfundo, font=fontepad)
lbl_altura.place(x=40, y=90)


ent_nome = ttk.Entry(frame_sup, width=15)
ent_nome.place(x=130, y=44)
ent_nome.focus()

ent_peso = ttk.Entry(frame_sup, width=10)
ent_peso.place(x=130, y=68)

ent_altura = ttk.Entry(frame_sup, width=10)
ent_altura.place(x=130, y=94)

btn_calc = ttk.Button(frame_sup, text='Calcular', command=calcular, width=8)
btn_calc.place(x=170, y=125)

btn_limpa = ttk.Button(frame_sup, text='Limpar', command=limpar, width=8, cursor='exchange')
btn_limpa.place(x=90, y=125)

lbl_res = Label(frame_inf, textvariable=resultado, bg=corfundo, font=fontepad, justify=LEFT)
lbl_res.place(x=20, y=20)

lbl_tabela = Label(frame_inf, textvariable=tabela, bg=corfundo, font=fontepad, justify=LEFT)
lbl_tabela.place(x=20, y=50)

lbl_ideal = Label(frame_inf, textvariable=ideal, bg=corfundo, font=fontepad, justify=LEFT)
lbl_ideal.place(x=20, y=120)

# ---------------------------------------------------
root.configure(menu=abas)
root.mainloop()
