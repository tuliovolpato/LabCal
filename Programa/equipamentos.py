from info_cal import info_cal
from empresas import Empresa

def cadastrar_info_equip(bancoDados):
    info_cal.cadastrar_info_equip(bancoDados)   

class EmpresaNotFoundError(Exception):
    pass

class EquipamentoIDExistsError(Exception):
    pass

class Equipamento:

    @staticmethod
    def validar_id_equipamento(bancoDados, id_equipamento):
        mycursor = bancoDados.dbConnection.cursor()
        sql = "SELECT id FROM equipamentos WHERE id = %s"
        values = (id_equipamento,)
        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        mycursor.close()
        if result:
            raise EquipamentoIDExistsError
        return False

    @staticmethod
    def validar_id_empresa(bancoDados, id_empresa):
        mycursor = bancoDados.dbConnection.cursor()
        sql = "SELECT id FROM empresas WHERE id = %s"
        values = (id_empresa,)
        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        mycursor.close()
        if not result:
            raise EmpresaNotFoundError
        return True

    @staticmethod
    def validar_status_cal(bancoDados, calibracao): 
        if calibracao == 1:
            resposta = input("Deseja inserir as informações do certificado de calibração agora? (S/N): ").strip().lower()
            if resposta == 's':
                cadastrar_info_equip(bancoDados)

    @staticmethod
    def cadastrar(bancoDados, id_equipamento, id_empresa, nome, modelo, fabricante, numero_serie, setor, padrao, calibracao):
        mycursor = bancoDados.dbConnection.cursor()

        try:
            Equipamento.validar_id_equipamento(bancoDados, id_equipamento)
            Equipamento.validar_id_empresa(bancoDados, id_empresa)
            
            sql = """INSERT INTO equipamentos (id, id_empresa, nome, modelo, fabricante, numero_serie, setor, padrao, calibracao) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (id_equipamento, id_empresa, nome, modelo, fabricante, numero_serie, setor, padrao, calibracao)

            mycursor.execute(sql, values)
            bancoDados.dbConnection.commit()
            return True
        except (EmpresaNotFoundError, EquipamentoIDExistsError):
            raise  # Re-lance a exceção para ser tratada em outra parte do código
        except Exception as e:
            bancoDados.dbConnection.rollback()
            return False
        finally:
            mycursor.close()


    @staticmethod
    def apagar_por_id(bancoDados, id_equipamento):
        return Equipamento._apagar(bancoDados, "ID", id_equipamento)

    @staticmethod
    def apagar_por_nome(bancoDados, nome_equipamento):
        return Equipamento._apagar(bancoDados, "nome", nome_equipamento)

    @staticmethod
    def apagar_por_modelo(bancoDados, modelo_equipamento):
        return Equipamento._apagar(bancoDados, "modelo", modelo_equipamento)

    @staticmethod
    def apagar_por_fabricante(bancoDados, fabricante_equipamento):
        return Equipamento._apagar(bancoDados, "fabricante", fabricante_equipamento)

    @staticmethod
    def apagar_por_numero_serie(bancoDados, ns_equipamento):
        return Equipamento._apagar(bancoDados, "numero_serie", ns_equipamento)


    @staticmethod
    def exibir_resultados(results):
        print("Equipamento encontrado:")
        for result in results:
            print(result)

    @staticmethod
    def _apagar(bancoDados, criteria, value):
        mycursor = bancoDados.dbConnection.cursor()

        column_mapping = {
            "ID": "id",
            "Nome": "nome",
            "Modelo": "modelo",
            "Fabricante": "fabricante",
            "Número de Série": "numero_serie"
        }

        column_name = column_mapping.get(criteria)

        if not column_name:
            return (False, f"Critério desconhecido: {criteria}")  # Retornando False com uma lista vazia se o critério não for reconhecido

        sql = f"SELECT * FROM equipamentos WHERE {column_name} = %s"
        value_tuple = (value,)

        try:
            mycursor.execute(sql, value_tuple)
            results = mycursor.fetchall()

            if not results:
                return (False, f"Nenhuma equipamento encontrada com esse {criteria}.") # Retornando False com uma lista vazia se nenhum equipamento for encontrado
            return (True, results)

        except Exception as e:
            return (False, f"Erro ao tentar buscar equipamento com {criteria} = {value}: {str(e)}")  # Retornando False com uma lista vazia se ocorrer um erro
        finally:
            mycursor.close()


    @staticmethod
    def confirm_and_delete(bancoDados, column_name, value):
        delete_sql = f"DELETE FROM equipamentos WHERE {column_name} = %s"
        value_tuple = (value,)

        mycursor = bancoDados.dbConnection.cursor()

        try:
            mycursor.execute(delete_sql, value_tuple)
            
            if mycursor.rowcount > 0:
                bancoDados.dbConnection.commit()
                return True
            else:
                return "Nenhum equipamento corresponde a esse critério. No entanto, nenhum erro ocorreu na operação."
        except Exception as e:
            return f"Erro ao tentar apagar equipamento com {column_name} = {value}: {str(e)}"
        finally:
            mycursor.close()


    @staticmethod
    def pesquisar_por_id(bancoDados, id_equipamento):
        return Equipamento._pesquisar(bancoDados, "id", id_equipamento)

    @staticmethod
    def pesquisar_por_nome(bancoDados, nome_equipamento):
        return Equipamento._pesquisar(bancoDados, "nome", nome_equipamento)

    @staticmethod
    def pesquisar_por_modelo(bancoDados, modelo_equipamento):
        return Equipamento._pesquisar(bancoDados, "modelo", modelo_equipamento)

    @staticmethod
    def pesquisar_por_fabricante(bancoDados, fabricante_equipamento):
        return Equipamento._pesquisar(bancoDados, "fabricante", fabricante_equipamento)

    @staticmethod
    def pesquisar_por_numero_serie(bancoDados, ns_equipamento):
        return Equipamento._pesquisar(bancoDados, "numero_serie", ns_equipamento)

    @staticmethod
    def pesquisar_por_setor(bancoDados, setor):
        return Equipamento._pesquisar(bancoDados, "setor", setor)

    @staticmethod
    def pesquisar_por_padrao(bancoDados, padrao):
        return Equipamento._pesquisar(bancoDados, "padrao", padrao)

    @staticmethod
    def pesquisar_por_calibracao(bancoDados, calibracao):
        return Equipamento._pesquisar(bancoDados, "calibracao", calibracao)

    @staticmethod
    def pesquisar_todos_equipamentos(bancoDados):
        return Equipamento._pesquisar(bancoDados, "Todos os equipamentos", None)


    @staticmethod
    def _pesquisar(bancoDados, coluna, valor=None):
        mycursor = bancoDados.dbConnection.cursor()
        
        sql = ""
        value = None

        if coluna == "Todos os equipamentos":
            sql = "SELECT * FROM equipamentos"
        else:
            if coluna in ["id", "padrao", "calibracao"]:
                sql = f"SELECT * FROM equipamentos WHERE {coluna} = %s"
                value = (int(valor),) if coluna == "id" else (valor,)
            else:
                sql = f"SELECT * FROM equipamentos WHERE {coluna} LIKE %s"
                value = ("%" + str(valor) + "%",)

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


    def pesquisar_equip_empresa(id_empresa, bancoDados):
        mycursor = bancoDados.dbConnection.cursor()
        # Executa a consulta SQL
        mycursor.execute("SELECT * FROM equipamentos WHERE id_empresa = %s", (id_empresa,))

        # Recupera os resultados da consulta
        results = mycursor.fetchall()

        # Exibe os resultados
        if results:
            print("Equipamentos encontrados:")
            for result in results:
                 print(result)
        else:
            print("Operação falhou:")




