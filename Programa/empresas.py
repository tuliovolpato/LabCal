class Empresa:
    def __init__(self, id, nome, telefone, endereco, email, CEP, responsavel):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.CEP = CEP
        self.responsavel = responsavel

    @staticmethod
    def validar_id_empresa(bancoDados, id_empresa):
        mycursor = bancoDados.dbConnection.cursor()

        sql = "SELECT id FROM empresas WHERE id = %s"
        values = (id_empresa,)

        mycursor.execute(sql, values)
        result = mycursor.fetchone()

        return True if result else False

    @staticmethod
    def cadastrar(bancoDados, id_empresa, nome, telefone, endereco, email, CEP, responsavel):
        mycursor = bancoDados.dbConnection.cursor()

        if Empresa.validar_id_empresa(bancoDados, id_empresa):
            print("O ID da empresa já existe.")
            return False

        sql = "INSERT INTO empresas (id, nome, telefone, endereco, email, CEP, responsavel) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id_empresa, nome, telefone, endereco, email, CEP, responsavel)

        try:
            mycursor.execute(sql, values)
            bancoDados.dbConnection.commit()
            return True
        except Exception as e:
            print("Erro ao cadastrar empresa:", e)
            bancoDados.dbConnection.rollback()
            return False
        finally:
            mycursor.close()

    @staticmethod
    def apagar_por_id(bancoDados, id_empresa):
        return Empresa._apagar(bancoDados, "ID", id_empresa)

    @staticmethod
    def apagar_por_nome(bancoDados, nome_empresa):
        return Empresa._apagar(bancoDados, "Nome", nome_empresa)

    @staticmethod
    def apagar_por_telefone(bancoDados, telefone_empresa):
        return Empresa._apagar(bancoDados, "Telefone", telefone_empresa)

    @staticmethod
    def apagar_por_endereco(bancoDados, endereco_empresa):
        return Empresa._apagar(bancoDados, "Endereço", endereco_empresa)

    @staticmethod
    def apagar_por_email(bancoDados, email_empresa):
        return Empresa._apagar(bancoDados, "Email", email_empresa)

    @staticmethod
    def apagar_por_cep(bancoDados, cep_empresa):
        return Empresa._apagar(bancoDados, "CEP", cep_empresa)

    @staticmethod
    def exibir_resultados(results):
        print("Empresa encontrada:")
        for result in results:
            print(result)

    @staticmethod
    def _apagar(bancoDados, criteria, value):
        mycursor = bancoDados.dbConnection.cursor()

        column_mapping = {
            "ID": "id",
            "Nome": "nome",
            "Telefone": "telefone",
            "Endereço": "endereco",
            "Email": "email",
            "CEP": "cep"
        }

        column_name = column_mapping.get(criteria)
        if not column_name:
            return (False, f"Critério desconhecido: {criteria}")

        sql = f"SELECT * FROM empresas WHERE {column_name} = %s"
        value_tuple = (value,)

        try:
            mycursor.execute(sql, value_tuple)
            results = mycursor.fetchall()

            if not results:
                return (False, f"Nenhuma empresa encontrada com esse {criteria}.")
            return (True, results)
        except Exception as e:
            return (False, f"Erro ao tentar buscar empresa com {criteria} = {value}: {str(e)}")
        finally:
            mycursor.close()

    @staticmethod
    def confirm_and_delete(bancoDados, column_name, value):
        delete_sql = f"DELETE FROM empresas WHERE {column_name} = %s"
        value_tuple = (value,)

        mycursor = bancoDados.dbConnection.cursor()

        try:
            mycursor.execute(delete_sql, value_tuple)
            bancoDados.dbConnection.commit()
            print("As informações foram apagadas.")
            return True
        except Exception as e:
            print(f"Erro ao tentar apagar empresa com {column_name} = {value}:", e)
            bancoDados.dbConnection.rollback()
            return False
        finally:
            mycursor.close()


    @staticmethod
    def pesquisar_por_id(bancoDados, id_empresa):
        return Empresa._pesquisar(bancoDados, "id", id_empresa)

    @staticmethod
    def pesquisar_por_nome(bancoDados, nome_empresa):
        return Empresa._pesquisar(bancoDados, "nome", nome_empresa)

    @staticmethod
    def pesquisar_por_telefone(bancoDados, telefone_empresa):
        return Empresa._pesquisar(bancoDados, "telefone", telefone_empresa)

    @staticmethod
    def pesquisar_por_endereco(bancoDados, endereco_empresa):
        return Empresa._pesquisar(bancoDados, "endereco", endereco_empresa)

    @staticmethod
    def pesquisar_por_email(bancoDados, email_empresa):
        return Empresa._pesquisar(bancoDados, "email", email_empresa)

    @staticmethod
    def pesquisar_por_cep(bancoDados, cep_empresa):
        return Empresa._pesquisar(bancoDados, "CEP", cep_empresa)

    @staticmethod
    def pesquisar_por_responsavel(bancoDados, responsavel_empresa):
        return Empresa._pesquisar(bancoDados, "responsavel", responsavel_empresa)

    @staticmethod
    def pesquisar_todas_empresas(bancoDados):
        return Empresa._pesquisar(bancoDados, "Todas as empresas")
    
    
    @staticmethod
    def _pesquisar(bancoDados, coluna, valor=None):
        mycursor = bancoDados.dbConnection.cursor()

        sql = ""
        value = None

        if coluna == "Todas as empresas":
            sql = "SELECT * FROM empresas"
        else:
            if coluna == "id":
                sql = f"SELECT * FROM empresas WHERE {coluna} = %s"
                value = (valor,)
            else:
                sql = f"SELECT * FROM empresas WHERE {coluna} LIKE %s"
                value = ("%" + valor + "%",)

        try:
            if value:
                mycursor.execute(sql, value)
            else:
                mycursor.execute(sql)

            results = mycursor.fetchall()
            return results if results else None

        except Exception as e:
            print("Erro na pesquisa:", e)
            return None
        finally:
            mycursor.close()

    @staticmethod
    def pesquisar_equip_empresa(bancoDados, id_empresa):
        mycursor = bancoDados.dbConnection.cursor()
        mycursor.execute("SELECT * FROM equipamentos WHERE id_empresa = %s", (id_empresa,))
        results = mycursor.fetchall()
        mycursor.close()

        return results

    @staticmethod
    def obter_todas_empresas(bancoDados):
        mycursor = bancoDados.dbConnection.cursor()

        # A consulta SQL para pegar todas as empresas
        sql = "SELECT * FROM empresas"
        
        try:
            mycursor.execute(sql)
            results = mycursor.fetchall()  # Pega todos os registros
            return results  # Retorna a lista de todos os registros ou uma lista vazia se nenhum registro for encontrado
        except Exception as e:
            print("Erro ao obter todas as empresas:", e)
            return []
        finally:
            mycursor.close()

