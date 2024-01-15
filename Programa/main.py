import datetime
import sys
from info_cal import info_cal
from empresas import Empresa
from equipamentos import EmpresaNotFoundError, Equipamento, EquipamentoIDExistsError
sys.path.append(r'C:\Users\Tulio Volpato\Desktop\Pasta do estudante\Fetin\Fetin 2023\Projeto\Projeto_M12\BD\Banco de Dados')
from database import BancoDeDados
import menu, re
import tkinter as tk
from tkinter import messagebox, Entry, StringVar

bancoDados = BancoDeDados("127.0.0.1", "root", "gastar01", "cadastro_labcal")

def main_screen():
    # Limpa todos os widgets da tela
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Sistema de Calibração")
    label.pack(pady=20)

    button1 = tk.Button(window, text="Empresas", command=empresa_screen)
    button1.pack(fill=tk.X)

    button2 = tk.Button(window, text="Equipamentos", command=equipamento_screen)
    button2.pack(fill=tk.X, pady=10)

    button_exit = tk.Button(window, text="Sair", command=window.quit)
    button_exit.pack(fill=tk.X, pady=10)

def empresa_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Empresas:")
    label.pack(pady=20)

    button1 = tk.Button(window, text="Cadastrar empresa", command=cadastrar_empresa_screen)
    button1.pack(fill=tk.X, pady=10)

    button2 = tk.Button(window, text="Apagar empresa", command= apagar_empresa_screen)
    button2.pack(fill=tk.X, pady=10)

    button3 = tk.Button(window, text="Pesquisar empresa", command=pesquisar_empresa_screen)
    button3.pack(fill=tk.X, pady=10)

    button_exit = tk.Button(window, text="Voltar", command=main_screen)
    button_exit.pack(fill=tk.X, pady=10)

def validate_only_numbers(char):
    return char.isdigit()

def cadastrar_empresa_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Cadastrar Empresa")
    label.pack(pady=20)

    validate_command = window.register(validate_only_numbers)
    label_id = tk.Label(window, text="ID da empresa")
    label_id.pack(pady=5)
    entry_id = tk.Entry(window, validate="key", validatecommand=(validate_command, '%S'))
    entry_id.pack(fill=tk.X, pady=5)
    
    label_nome = tk.Label(window, text="Nome da empresa")
    label_nome.pack(pady=5)
    entry_nome = tk.Entry(window)
    entry_nome.pack(fill=tk.X, pady=5)

    label_telefone = tk.Label(window, text="Telefone da empresa")
    label_telefone.pack(pady=5)
    entry_telefone = tk.Entry(window)
    entry_telefone.pack(fill=tk.X, pady=5)

    label_endereco = tk.Label(window, text="Endereço")
    label_endereco.pack(pady=5)
    entry_endereco = tk.Entry(window)
    entry_endereco.pack(fill=tk.X, pady=5)

    label_email = tk.Label(window, text="E-mail")
    label_email.pack(pady=5)
    entry_email = tk.Entry(window)
    entry_email.pack(fill=tk.X, pady=5)

    validate_cep_command = window.register(validate_only_numbers)
    label_cep = tk.Label(window, text="CEP")
    label_cep.pack(pady=5)
    entry_cep = tk.Entry(window, validate="key", validatecommand=(validate_cep_command, '%S'))
    entry_cep.pack(fill=tk.X, pady=5)

    label_responsavel = tk.Label(window, text="Responsável")
    label_responsavel.pack(pady=5)
    entry_responsavel = tk.Entry(window)
    entry_responsavel.pack(fill=tk.X, pady=5)

    def cadastrar():
        try:
            id_empresa = int(entry_id.get().strip())
        except ValueError:
            messagebox.showwarning("Erro", "O ID deve ser um número inteiro.")
            return
        
        nome = entry_nome.get().strip()
        telefone = entry_telefone.get().strip()
        endereco = entry_endereco.get().strip()
        email = entry_email.get().strip()
        cep = entry_cep.get().strip()
        responsavel = entry_responsavel.get().strip()

        if not (id_empresa and nome and telefone and endereco and email and cep and responsavel):
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
            return

        if Empresa.validar_id_empresa(bancoDados, id_empresa):
            messagebox.showwarning("Erro", "O ID da empresa já existe. Tente novamente.")
            return

        success = Empresa.cadastrar(bancoDados, id_empresa, nome, telefone, endereco, email, cep, responsavel)
        
        if success:
            messagebox.showinfo("Sucesso", "Empresa cadastrada com sucesso!")
            empresa_screen()
        else:
            messagebox.showwarning("Erro", "Falha ao cadastrar a empresa!")

    button_submit = tk.Button(window, text="Cadastrar", command=cadastrar)
    button_submit.pack(pady=20)

    button_exit = tk.Button(window, text="Voltar", command=empresa_screen)
    button_exit.pack(fill=tk.X, pady=10)

def confirm_delete(empresa_info):
    confirm = tk.Toplevel(window)
    confirm.title("Confirmação")
    confirm.geometry("300x250")  # Ajuste essas dimensões conforme sua necessidade
    
    details = f"ID: {empresa_info['id']}\n" \
              f"Nome: {empresa_info['nome']}\n" \
              f"Telefone: {empresa_info['telefone']}\n" \
              f"Endereço: {empresa_info['endereco']}\n" \
              f"Email: {empresa_info['email']}\n" \
              f"CEP: {empresa_info['CEP']}\n" \
              f"Responsável: {empresa_info['responsavel']}\n"
    label_details = tk.Label(confirm, text=details)
    label_details.grid(row=0, column=0, columnspan=2, pady=10)

    label = tk.Label(confirm, text="Tem certeza de que deseja apagar essa empresa?")
    label.grid(row=1, column=0, columnspan=2, pady=10, padx=20)

    def on_yes():
        confirm.result = True
        confirm.destroy()

    def on_no():
        confirm.result = False
        confirm.destroy()

    yes_button = tk.Button(confirm, text="Sim", command=on_yes)
    yes_button.grid(row=2, column=0, padx=2)  # Reduzi o padx

    no_button = tk.Button(confirm, text="Não", command=on_no)
    no_button.grid(row=2, column=1, padx=2)  # Reduzi o padx

    window.wait_window(confirm)
    return getattr(confirm, 'result', False)

def apagar_empresa_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Apagar Empresa")
    label.pack(pady=20)

    criteria = tk.StringVar()  # Armazenará o critério selecionado pelo usuário
    criteria.set("ID")  # Define o padrão como "ID"

    criteria_list = ["ID", "Nome", "Telefone", "Endereço", "Email", "CEP"]

    drop = tk.OptionMenu(window, criteria, *criteria_list)
    drop.pack(pady=20)

    label_input = tk.Label(window, text="Digite o valor correspondente ao critério selecionado:")
    label_input.pack(pady=5)
    entry_input = tk.Entry(window)
    entry_input.pack(fill=tk.X, pady=5)

    def apagar():
        selected_criteria = criteria.get()
        value = entry_input.get().strip()

        if not value:
            messagebox.showwarning("Erro", "O campo de valor deve ser fornecido!")
            return
        
        success, results = Empresa._apagar(bancoDados, selected_criteria, value)

        if success:
            if not confirm_delete(results[0]):  # Considerando que haverá apenas um resultado. Ajuste conforme necessário.
                messagebox.showinfo("Operação Cancelada", "Operação de exclusão cancelada")
                return

            # Apagando a empresa após a confirmação
            success_delete = Empresa.confirm_and_delete(bancoDados, selected_criteria, value)

            if success_delete:
                messagebox.showinfo("Sucesso", "Empresa apagada com sucesso!")
            else:
                messagebox.showwarning("Erro", "Falha ao apagar a empresa!")
        else:
            messagebox.showwarning("Erro", "Nenhuma empresa encontrada!")

        if not confirm_delete():
            messagebox.showinfo("Operação Cancelada", "Operação de exclusão cancelada")
            return

        if selected_criteria == "ID":
            try:
                value = int(value)
                success = Empresa.apagar_por_id(bancoDados, value)
            except ValueError:
                messagebox.showwarning("Erro", "O ID da empresa deve ser um número!")
                return
        elif selected_criteria == "Nome":
            success = Empresa.apagar_por_nome(bancoDados, value)
        elif selected_criteria == "Telefone":
            success = Empresa.apagar_por_telefone(bancoDados, value)
        elif selected_criteria == "Endereço":
            success = Empresa.apagar_por_endereco(bancoDados, value)
        elif selected_criteria == "Email":
            success = Empresa.apagar_por_email(bancoDados, value)
        elif selected_criteria == "CEP":
            success = Empresa.apagar_por_cep(bancoDados, value)

        if success:
            messagebox.showinfo("Sucesso", "Empresa apagada com sucesso!")
        else:
            messagebox.showwarning("Erro", "Falha ao apagar a empresa!")

    button_apagar = tk.Button(window, text="Apagar", command=apagar)
    button_apagar.pack(pady=20)

    button_exit = tk.Button(window, text="Voltar", command=empresa_screen)
    button_exit.pack(fill=tk.X, pady=10)

def exibir_todas_empresas():
    for widget in window.winfo_children():
        widget.destroy()

    # Suponhamos que a classe Empresa tenha um método chamado pesquisar_todas_empresas()
    todas_empresas = Empresa.pesquisar_todas_empresas(bancoDados)

    label = tk.Label(window, text="Todas as Empresas")
    label.pack(pady=20)

    # Criando um frame para conter o Text widget e a Scrollbar
    frame = tk.Frame(window)
    frame.pack(pady=10)

    # Criando o Scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Criando um Text widget com a Scrollbar
    equip_text = tk.Text(frame, wrap=tk.WORD, height=50, width=110, yscrollcommand=scrollbar.set)
    equip_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Conectando a Scrollbar ao Text widget
    scrollbar.config(command=equip_text.yview)

    if todas_empresas:
        for empresa in todas_empresas:
            info = f"ID: {empresa['id']}\n" \
                f"Nome: {empresa['nome']}\n" \
                f"Endereço: {empresa['endereco']}\n" \
                f"Telefone: {empresa['telefone']}\n" \
                f"Email: {empresa['email']}\n" \
                f"Responsável: {empresa['responsavel']}\n\n"
            equip_text.insert(tk.END, info)
    else:
        equip_text.insert(tk.END, "Nenhuma empresa cadastrada!")

    # Desabilitando o Text widget para impedir a edição do usuário
    equip_text.config(state=tk.DISABLED)

    button_exit = tk.Button(window, text="Voltar", command=pesquisar_empresa_screen)
    button_exit.pack(pady=20)

def pesquisar_empresa_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Pesquisar Empresa")
    label.pack(pady=20)

    criteria = tk.StringVar()  
    criteria.set("ID")  

    criteria_list = ["ID", "Nome", "Telefone", "Endereco", "Email", "CEP", "Responsavel"]
    drop = tk.OptionMenu(window, criteria, *criteria_list)
    drop.pack(pady=20)

    label_input = tk.Label(window, text="Digite o valor correspondente ao critério selecionado:")
    label_input.pack(pady=5)
    entry_input = tk.Entry(window)
    entry_input.pack(fill=tk.X, pady=5)

    info_label = tk.Label(window, text="") 
    info_label.pack(pady=20)

    criteria_to_method = {
        "ID": Empresa.pesquisar_por_id,
        "Nome": Empresa.pesquisar_por_nome,
        "Telefone": Empresa.pesquisar_por_telefone,
        "Endereco": Empresa.pesquisar_por_endereco,
        "Email": Empresa.pesquisar_por_email,
        "CEP": Empresa.pesquisar_por_cep,
        "Responsavel": Empresa.pesquisar_por_responsavel
    }

    def pesquisar():
        selected_criteria = criteria.get()
        value = entry_input.get().strip()

        if not value:
            messagebox.showwarning("Erro", "O campo de valor deve ser fornecido!")
            return

        if selected_criteria == "ID":
            try:
                value = int(value)
            except ValueError:
                messagebox.showwarning("Erro", "O ID da empresa deve ser um número!")
                return

        empresa = criteria_to_method[selected_criteria](bancoDados, value)

        if empresa:
            info = f"ID: {empresa[0]['id']}\n" \
                   f"Nome: {empresa[0]['nome']}\n" \
                   f"Endereço: {empresa[0]['endereco']}\n" \
                   f"Telefone: {empresa[0]['telefone']}\n" \
                   f"Email: {empresa[0]['email']}\n" \
                   f"Responsável: {empresa[0]['responsavel']}"
            info_label.config(text=info)
        else:
            messagebox.showwarning("Erro", "Empresa não encontrada!")

    def ver_equipamentos():
        value = entry_input.get().strip()
        empresa = criteria_to_method[criteria.get()](bancoDados, value)

        if empresa:
            ver_equipamentos_relacionados_screen(empresa[0]['id'])
        else:
            messagebox.showwarning("Erro", "Não foi possível encontrar a empresa para buscar os equipamentos.")


    button_frame = tk.Frame(window)
    button_frame.pack(pady=20)

    button_pesquisar = tk.Button(button_frame, text="Pesquisar", command=pesquisar)
    button_pesquisar.pack(side=tk.LEFT, padx=5)

    button_mostrar_todas = tk.Button(button_frame, text="Mostrar Todas as Empresas", command=exibir_todas_empresas)
    button_mostrar_todas.pack(side=tk.LEFT, padx=5)

    button_ver_equipamentos = tk.Button(window, text="Ver equipamentos relacionados", command=ver_equipamentos)
    button_ver_equipamentos.pack(pady=10)

    button_exit = tk.Button(window, text="Voltar", command=empresa_screen)
    button_exit.pack(fill=tk.X, pady=10)

def ver_equipamentos_relacionados_screen(empresa_id):
    # Primeiro, limpar todos os widgets da tela anterior
    for widget in window.winfo_children():
        widget.destroy()

    # Título da tela
    label = tk.Label(window, text="Equipamentos Relacionados")
    label.pack(pady=20)

    # Criando um frame para conter o Text widget e a Scrollbar
    frame = tk.Frame(window)
    frame.pack(pady=10)

    # Criando o Scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Widget Text para exibir os detalhes dos equipamentos
    equip_text = tk.Text(frame, wrap=tk.WORD, height=50, width=110, yscrollcommand=scrollbar.set)
    equip_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Conectando a Scrollbar ao Text widget
    scrollbar.config(command=equip_text.yview)

    equipamentos = Empresa.pesquisar_equip_empresa(bancoDados, empresa_id)

    if equipamentos:
        for equip in equipamentos:
            equip_text.insert(tk.END, f"ID: {equip['id']}\n")
            equip_text.insert(tk.END, f"Nome: {equip['nome']}\n")
            equip_text.insert(tk.END, f"Modelo: {equip['modelo']}\n")
            equip_text.insert(tk.END, f"Fabricante: {equip['fabricante']}\n")
            equip_text.insert(tk.END, f"Num. de Série: {equip['numero_serie']}\n")
            equip_text.insert(tk.END, f"Setor: {equip['setor']}\n")
            equip_text.insert(tk.END, f"É um equipamento padrão? {equip['padrao']}\n")
            equip_text.insert(tk.END, f"Calibração: {equip['calibracao']}\n")
            # Adicione aqui mais detalhes conforme necessário, similar ao exemplo acima

            equip_text.insert(tk.END, "-"*50 + "\n")  # Separador entre equipamentos

        # Evite que o usuário edite os detalhes no widget Text
        equip_text.config(state=tk.DISABLED)
    else:
        messagebox.showwarning("Atenção", "Nenhum equipamento encontrado para esta empresa.")

    # Botão para voltar para a tela de pesquisa de empresas
    button_back = tk.Button(window, text="Voltar", command=pesquisar_empresa_screen)
    button_back.pack(pady=20)

def equipamento_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Equipamentos:")
    label.pack(pady=20)

    button1 = tk.Button(window, text="Cadastrar equipamento", command=cadastrar_equipamento_screen)
    button1.pack(fill=tk.X, pady=10)

    button2 = tk.Button(window, text="Apagar equipamento", command=apagar_equipamento_screen)
    button2.pack(fill=tk.X, pady=10)

    button3 = tk.Button(window, text="Pesquisar equipamento", command=pesquisar_equipamento_screen)
    button3.pack(fill=tk.X, pady=10)

    button4 = tk.Button(window, text="Status de Calibração", command=status_equipamento_screen)
    button4.pack(fill=tk.X, pady=10)

    button_exit = tk.Button(window, text="Voltar", command=main_screen)
    button_exit.pack(fill=tk.X, pady=10)

def cadastrar_equipamento_screen():

    def clear_window():
        for widget in window.winfo_children():
            widget.destroy()

    def toggle_padrao_fields(*args):
        if padrao_var.get() == "S":
            pass  # Se você tiver outros campos associados ao estado "Sim", coloque aqui.
        else:
            pass  # Se você tiver outros campos associados ao estado "Não", coloque aqui.

    def cadastrar():
        try:
            id_equipamento = int(entry_id.get())
            id_empresa = int(entry_empresa.get())
            nome = entry_nome.get()
            modelo = entry_modelo.get()
            fabricante = entry_fabricante.get()
            numero_serie = entry_numero_serie.get()
            setor = entry_setor.get()
            padrao = padrao_var.get() == "S"
            calibracao = calibracao_var.get() == "S"

            success = Equipamento.cadastrar(
                bancoDados, id_equipamento, id_empresa, nome, modelo, 
                fabricante, numero_serie, setor, padrao, calibracao
            )

            if success:
                messagebox.showinfo("Sucesso", "Equipamento cadastrado com sucesso!")
            else:
                messagebox.showwarning("Erro", "Falha ao cadastrar o equipamento!")
        except ValueError:
            messagebox.showwarning("Erro", "IDs devem ser números!")
        except EmpresaNotFoundError:  # Supondo que esta seja a exceção levantada quando o ID da empresa não é encontrado.
            messagebox.showwarning("Erro", "ID da empresa não encontrado.")
        except EquipamentoIDExistsError:  # Supondo que esta exceção seja lançada quando o ID do equipamento já existe.
            messagebox.showwarning("Erro", "ID do equipamento já existe.")
        except Exception as e:
            messagebox.showwarning("Erro", f"Erro desconhecido: {e}")

    clear_window()

    label = tk.Label(window, text="Cadastrar Equipamento")
    label.pack(pady=20)

    # Widgets setup except for the Radiobuttons
    labels_texts = [
        "ID do Equipamento:", "ID da Empresa:", "Nome do Equipamento:", 
        "Modelo do Equipamento:", "Fabricante do Equipamento:", "Número de Série:", "Setor do Equipamento na Empresa:"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(window, text=text)
        label.pack(pady=5)
        entry = tk.Entry(window)
        entry.pack(fill=tk.X, pady=5)
        entries.append(entry)

    # Radiobutton for "O equipamento é um padrão?"
    padrao_var = tk.StringVar(value="N")  # Default to 'No'
    label_padrao = tk.Label(window, text="O equipamento é um padrão?")
    label_padrao.pack(pady=5)
    radio_padrao_S = tk.Radiobutton(window, text="Sim", variable=padrao_var, value="S", command=toggle_padrao_fields)
    radio_padrao_S.pack(anchor=tk.W)
    radio_padrao_N = tk.Radiobutton(window, text="Não", variable=padrao_var, value="N", command=toggle_padrao_fields)
    radio_padrao_N.pack(anchor=tk.W)

    # Radiobutton for "O equipamento precisa de calibração?"
    calibracao_var = tk.StringVar(value="N")  # Default to 'No'
    label_calibracao = tk.Label(window, text="O equipamento precisa de calibração?")
    label_calibracao.pack(pady=5)
    radio_calibracao_S = tk.Radiobutton(window, text="Sim", variable=calibracao_var, value="S")
    radio_calibracao_S.pack(anchor=tk.W)
    radio_calibracao_N = tk.Radiobutton(window, text="Não", variable=calibracao_var, value="N")
    radio_calibracao_N.pack(anchor=tk.W)

    # Defining the Entries
    entry_id, entry_empresa, entry_nome, entry_modelo, entry_fabricante, entry_numero_serie, entry_setor = entries

    # Defining the Buttons
    button_cadastrar = tk.Button(window, text="Cadastrar", command=cadastrar)
    button_cadastrar.pack(pady=20)

    button_exit = tk.Button(window, text="Voltar", command=equipamento_screen)  # Assuming you have an 'equipamento_screen' function
    button_exit.pack(fill=tk.X, pady=10)

    # Initially hide padrao fields
    toggle_padrao_fields()

def confirm_delete_equipamentos(equipamento_info):
    confirm = tk.Toplevel(window)
    confirm.title("Confirmação")
    confirm.geometry("310x310")  # Ajuste essas dimensões conforme sua necessidade
    
    details = f"ID: {equipamento_info['id']}\n" \
              f"Nome: {equipamento_info['nome']}\n" \
              f"Modelo: {equipamento_info['modelo']}\n" \
              f"Fabricante: {equipamento_info['fabricante']}\n" \
              f"Número de Série: {equipamento_info['numero_serie']}\n"

    label_details = tk.Label(confirm, text=details)
    label_details.grid(row=0, column=0, columnspan=2, pady=10)

    label = tk.Label(confirm, text="Tem certeza de que deseja apagar este equipamento?")
    label.grid(row=1, column=0, columnspan=2, pady=10, padx=20)

    def on_yes():
        confirm.result = True
        confirm.destroy()

    def on_no():
        confirm.result = False
        confirm.destroy()

    yes_button = tk.Button(confirm, text="Sim", command=on_yes)
    yes_button.grid(row=2, column=0, padx=2)

    no_button = tk.Button(confirm, text="Não", command=on_no)
    no_button.grid(row=2, column=1, padx=2)

    window.wait_window(confirm)
    return getattr(confirm, 'result', False)

def apagar_equipamento_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Apagar Equipamento")
    label.pack(pady=20)

    criteria = tk.StringVar()
    criteria.set("ID")

    criteria_list = ["ID", "Nome", "Modelo", "Fabricante", "Número de Série"]

    drop = tk.OptionMenu(window, criteria, *criteria_list)
    drop.pack(pady=20)

    label_input = tk.Label(window, text="Digite o valor correspondente ao critério selecionado:")
    label_input.pack(pady=5)
    entry_input = tk.Entry(window)
    entry_input.pack(fill=tk.X, pady=5)

    def apagar():
        selected_criteria = criteria.get()
        value = entry_input.get().strip()

        if not value:
            messagebox.showwarning("Erro", "O campo de valor deve ser fornecido!")
            return
            
        success, results = Equipamento._apagar(bancoDados, selected_criteria, value)

        if success:
            if not confirm_delete_equipamentos(results[0]):
                messagebox.showinfo("Operação Cancelada", "Operação de exclusão cancelada")
                return

            success_delete = Equipamento.confirm_and_delete(bancoDados, selected_criteria, value)

            if success_delete:
                messagebox.showinfo("Sucesso", "Equipamento apagado com sucesso!")
            else:
                messagebox.showwarning("Erro", "Falha ao apagar o equipamento!")
        else:
            messagebox.showwarning("Erro", "Nenhum equipamento encontrado!")


    button_apagar = tk.Button(window, text="Apagar", command=apagar)
    button_apagar.pack(pady=20)

    button_exit = tk.Button(window, text="Voltar", command=equipamento_screen)
    button_exit.pack(fill=tk.X, pady=10)

def exibir_todos_equipamentos():
    for widget in window.winfo_children():
        widget.destroy()

    # Suponhamos que a classe Equipamento tenha um método chamado pesquisar_todos_equipamentos()
    todos_equipamentos = Equipamento.pesquisar_todos_equipamentos(bancoDados)

    label = tk.Label(window, text="Todos os Equipamentos")
    label.pack(pady=20)

    # Criando um frame para conter o Text widget e a Scrollbar
    frame = tk.Frame(window)
    frame.pack(pady=10)

    # Criando o Scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Criando um Text widget com a Scrollbar
    equip_text = tk.Text(frame, wrap=tk.WORD, height=50, width=110, yscrollcommand=scrollbar.set)
    equip_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Conectando a Scrollbar ao Text widget
    scrollbar.config(command=equip_text.yview)

    if todos_equipamentos:
        for equipamento in todos_equipamentos:
            info = f"ID: {equipamento['id']}\n" \
                   f"Nome: {equipamento['nome']}\n" \
                   f"Modelo: {equipamento['modelo']}\n" \
                   f"Fabricante: {equipamento['fabricante']}\n" \
                   f"Número de Série: {equipamento['numero_serie']}\n" \
                   f"Setor: {equipamento['setor']}\n" \
                   f"Padrão: {equipamento['padrao']}\n" \
                   f"Calibração: {equipamento['calibracao']}\n\n"
            equip_text.insert(tk.END, info)
    else:
        equip_text.insert(tk.END, "Nenhum equipamento cadastrado!")

    # Desabilitando o Text widget para impedir a edição do usuário
    equip_text.config(state=tk.DISABLED)

    button_exit = tk.Button(window, text="Voltar", command=pesquisar_equipamento_screen)
    button_exit.pack(pady=20)

def pesquisar_equipamento_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Pesquisar Equipamento")
    label.pack(pady=20)

    criteria = tk.StringVar()
    criteria.set("ID")

    criteria_list = ["ID", "Nome", "Modelo", "Fabricante", "Número de Série", "Setor", "Padrão", "Calibração"]
    drop = tk.OptionMenu(window, criteria, *criteria_list)
    drop.pack(pady=20)

    label_input = tk.Label(window, text="Digite o valor correspondente ao critério selecionado:")
    label_input.pack(pady=5)
    entry_input = tk.Entry(window)
    entry_input.pack(fill=tk.X, pady=5)

    # Crie um frame para conter o Text widget e a scrollbar
    frame = tk.Frame(window)
    frame.pack(pady=20)

    # Crie o Text widget dentro do frame (sem configurar a scrollbar ainda)
    equip_text = tk.Text(frame, wrap=tk.WORD, height=30, width=110)
    equip_text.pack(side=tk.LEFT)

    # Crie a scrollbar e associe-a ao Text widget
    scrollbar = tk.Scrollbar(frame, command=equip_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Agora, associe a scrollbar ao Text widget
    equip_text.config(yscrollcommand=scrollbar.set)


    criteria_mapping = {
            "ID": Equipamento.pesquisar_por_id,
            "Nome": Equipamento.pesquisar_por_nome,
            "Modelo": Equipamento.pesquisar_por_modelo,
            "Fabricante": Equipamento.pesquisar_por_fabricante,
            "Número de Série": Equipamento.pesquisar_por_numero_serie,
            "Setor": Equipamento.pesquisar_por_setor,
            "Padrão": Equipamento.pesquisar_por_padrao,
            "Calibração": Equipamento.pesquisar_por_calibracao
        }

    def pesquisar():
        selected_criteria = criteria.get()
        value = entry_input.get().strip()

        if not value:
            messagebox.showwarning("Atenção", "Por favor, insira um valor para a pesquisa.")
            return

        if selected_criteria == "ID":
            try:
                value = int(value)
            except ValueError:
                messagebox.showwarning("Atenção", "ID deve ser um número inteiro.")
                return

        equipamentos = criteria_mapping[selected_criteria](bancoDados, value)

        if equipamentos:
            equip_text.config(state=tk.NORMAL)  # Habilita o widget Text para edição
            equip_text.delete(1.0, tk.END)      # Limpa o widget Text
            for equipamento in equipamentos:
                info = f"ID: {equipamento['id']}\n" \
                    f"Nome: {equipamento['nome']}\n" \
                    f"Modelo: {equipamento['modelo']}\n" \
                    f"Fabricante: {equipamento['fabricante']}\n" \
                    f"Número de Série: {equipamento['numero_serie']}\n" \
                    f"Setor: {equipamento['setor']}\n" \
                    f"Padrão: {equipamento['padrao']}\n" \
                    f"Calibração: {equipamento['calibracao']}\n\n"
                equip_text.insert(tk.END, info)
            equip_text.config(state=tk.DISABLED)  # Desabilita o widget Text após inserir as informações
        else:
            messagebox.showwarning("Erro", "Equipamento não encontrado!")


    button_frame = tk.Frame(window)
    button_frame.pack(pady=20)

    button_pesquisar = tk.Button(button_frame, text="Pesquisar", command=pesquisar)
    button_pesquisar.pack(side=tk.TOP, padx=5, pady=15)  

    button_mostrar_todos = tk.Button(button_frame, text="Mostrar Todos os Equipamentos", command=exibir_todos_equipamentos)
    button_mostrar_todos.pack(side=tk.TOP, padx=5, pady=5)

    button_exit = tk.Button(window, text="Voltar", command=equipamento_screen)
    button_exit.pack(fill=tk.X, pady=10)

def status_equipamento_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Status de Calibração")
    label.pack(pady=20)

    button1 = tk.Button(window, text="Inserir informações", command=inserir_info_equipamento_screen)
    button1.pack(fill=tk.X, pady=10)

    button2 = tk.Button(window, text="Apagar informações", command= apagar_info_equipamento_screen)
    button2.pack(fill=tk.X, pady=10)

    button3 = tk.Button(window, text="Pesquisar informações", command=pesquisar_info_equipamento_screen)
    button3.pack(fill=tk.X, pady=10)

    button_exit = tk.Button(window, text="Voltar", command=equipamento_screen)
    button_exit.pack(fill=tk.X, pady=10)

def inserir_info_equipamento_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Inserir informações")
    label.pack(pady=20)

    label_id_equipamento = tk.Label(window, text="ID do equipamento:")
    label_id_equipamento.pack(pady=5)
    id_equipamento_entry = tk.Entry(window)
    id_equipamento_entry.pack(fill=tk.X, pady=5)
    
    label_id = tk.Label(window, text="ID da instrução:")
    label_id.pack(pady=5)
    id_entry = tk.Entry(window)
    id_entry.pack(fill=tk.X, pady=5)

    label_certificado = tk.Label(window, text="Numero do certificado:")
    label_certificado.pack(pady=5)
    certificado_entry = tk.Entry(window)
    certificado_entry.pack(fill=tk.X, pady=5)

    label_data_cal = tk.Label(window, text="Data da calibração:")
    label_data_cal.pack(pady=5)
    data_cal_entry = tk.Entry(window)
    data_cal_entry.pack(fill=tk.X, pady=5)

    label_validade_cal = tk.Label(window, text="Validade da calibração:")
    label_validade_cal.pack(pady=5)
    validade_cal_entry = tk.Entry(window)
    validade_cal_entry.pack(fill=tk.X, pady=5)

    def cadastrar_info():
        id_equipamento = id_equipamento_entry.get().strip()
        id_ = id_entry.get().strip()
        certificado = certificado_entry.get().strip()
        data_cal = data_cal_entry.get().strip()
        validade_cal = validade_cal_entry.get().strip()

        if not (id_equipamento and id_ and certificado and data_cal and validade_cal):
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            id_equipamento = int(id_equipamento)
            id_ = int(id_)

            if info_cal.certificado_id_equipamento(bancoDados, id_equipamento):
                
                update = messagebox.askyesno("Atualizar", "O id_equipamento já possui certificado. Deseja atualizar os dados?")
                if update:
                    info_cal.update_info_equip(bancoDados, id_equipamento, certificado, data_cal, validade_cal)
                    messagebox.showinfo("Sucesso", "Informações atualizadas com sucesso!")
                    return
                else:
                    messagebox.showinfo("Info", "Operação cancelada.")
                    return

            info_cal.cadastrar_info_equip(bancoDados, id_equipamento, id_, certificado, data_cal, validade_cal)
            messagebox.showinfo("Sucesso", "Informações cadastrada com sucesso!")
        except ValueError as ve:
            messagebox.showwarning("Aviso", str(ve))
        except Exception as e:
            messagebox.showwarning("Erro", "Um erro inexperado ocorreu. Detalhes: " + str(e))
            
    button_save = tk.Button(window, text="Salvar", command=cadastrar_info)
    button_save.pack(pady=20)

    button_exit = tk.Button(window, text="Voltar", command=status_equipamento_screen)
    button_exit.pack(fill=tk.X, pady=10)


def apagar_info_equipamento_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Apagar informações do Equipamento")
    label.pack(pady=20)

    criteria = tk.StringVar()
    criteria.set("ID")
    criteria_list = ["ID", "Certificado"]
    drop = tk.OptionMenu(window, criteria, *criteria_list)
    drop.pack(pady=20)

    label_input = tk.Label(window, text="Digite o valor correspondente ao critério selecionado:")
    label_input.pack(pady=5)
    entry_input = tk.Entry(window)
    entry_input.pack(fill=tk.X, pady=5)

    def apagar():
        selected_criteria = criteria.get()
        value = entry_input.get().strip()

        if not value:
            messagebox.showwarning("Erro", "O campo de valor deve ser fornecido!")
            return

        success, message = info_cal.apagar_controle(bancoDados, selected_criteria, value)

        if success:
            confirmacao = messagebox.askyesno("Confirmação", "Tem certeza de que deseja apagar esse registro?")
            if confirmacao:
                try:
                    info_cal.confirm_and_delete(bancoDados, selected_criteria, value)
                    messagebox.showinfo("Sucesso", "Registro apagado com sucesso!")
                except Exception as e:
                    messagebox.showwarning("Erro", str(e))
            else:
                messagebox.showinfo("Cancelado", "Ação de apagar cancelada pelo usuário.")
        else:
            messagebox.showwarning("Erro", message)

    button_apagar = tk.Button(window, text="Apagar", command=apagar)
    button_apagar.pack(pady=20)

    button_exit = tk.Button(window, text="Voltar", command=status_equipamento_screen)
    button_exit.pack(fill=tk.X, pady=10)

def pesquisar_info_equipamento_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Pesquisar informações")
    label.pack(pady=20)

    criteria = tk.StringVar()
    criteria.set("Certificado")

    criteria_list = ["Certificado", "Equipamentos Vencidos", "Equipamentos a Vencer", "Vencendo em um mês"]
    drop = tk.OptionMenu(window, criteria, *criteria_list)
    drop.pack(pady=20)

    entry_input = tk.Entry(window)
    entry_input.pack(fill=tk.X, pady=5)

    button_search = tk.Button(window, text="Pesquisar", command=lambda: pesquisar_controle(criteria.get(), entry_input.get().strip()))
    button_search.pack(pady=20)

    frame = tk.Frame(window)
    frame.pack(pady=10)

    # Criando o Scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Criando um Text widget com a Scrollbar
    equip_text = tk.Text(frame, wrap=tk.WORD, height=20, width=70, yscrollcommand=scrollbar.set)
    equip_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Conectando a Scrollbar ao Text widget
    scrollbar.config(command=equip_text.yview)

    results_frame = tk.Frame(window)
    results_frame.pack(pady=20)

    def format_result(result):
        # Mapeia as chaves do dicionário para rótulos específicos
        labels_mapping = {
            'id': 'ID:',
            'id_equipamento': 'ID do equipamento:',
            'certificado': 'Certificado:',
            'data_cal': 'Data da Calibração:',
            'validade_cal': 'Validade da Calibração:'
        }
        
        # Formata o resultado para exibir os rótulos e valores
        formatted_str = ""
        for key, label in labels_mapping.items():
            value = result.get(key, "Informação não disponível")  # Se a chave não estiver presente no resultado, use uma mensagem padrão
            formatted_str += f"{label} {value}\n"
        return formatted_str

    def display_results(results):
        equip_text.config(state=tk.NORMAL)  # Habilita o widget Text para edição
        equip_text.delete(1.0, tk.END)  # Limpa o widget Text

        if results:
            for result in results:
                formatted_result = format_result(result)
                equip_text.insert(tk.END, formatted_result + "\n")
        else:
            equip_text.insert(tk.END, "Nenhum resultado encontrado.")

        equip_text.config(state=tk.DISABLED)


    def pesquisar_controle(criteria, value):
        if criteria == "Certificado" and not value:
            messagebox.showwarning("Atenção", "Por favor, insira um valor no campo de Certificado.")
            return

        results = []

        if criteria == "Certificado":
            results = info_cal.pesquisar_por_certificado(bancoDados, value)

        elif criteria == "Equipamentos Vencidos":
            results = info_cal.equipamentos_vencidos(bancoDados)

        elif criteria == "Equipamentos a Vencer":
            try:
                data = datetime.datetime.strptime(value, "%Y-%m-%d").date()
                results = info_cal.equipamentos_a_vencer(bancoDados, data)
            except ValueError:
                messagebox.showwarning("Atenção", "Por favor, insira uma data válida no formato YYYY-MM-DD.")
                return

        elif criteria == "Vencendo em um mês":
            results = info_cal.equipamentos_vencendo_em_um_mes(bancoDados)

        display_results(results)


    button_exit = tk.Button(window, text="Voltar", command=status_equipamento_screen)
    button_exit.pack(fill=tk.X, pady=10)

window = tk.Tk()
window.title("Sistema de Gerenciamento")
window.geometry("350x450")
main_screen()
window.mainloop()