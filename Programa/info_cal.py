import datetime
class info_cal:
    def __init__(self, id, certificado, data_cal, validade_cal, id_equipamento):
        self.id = id
        self.certificado = certificado
        self.data_cal = data_cal
        self.validade_cal = validade_cal
        self.id_equipamento = id_equipamento

    @staticmethod
    def cadastrar_info_equip(bancoDados, id_equipamento, id_, certificado, data_cal, validade_cal):
        mycursor = bancoDados.dbConnection.cursor()

        if not info_cal.validar_id_equipamento(bancoDados, id_equipamento):
            raise ValueError("Equipamento não encontrado. Operação cancelada.")

        if info_cal.certificado_id_equipamento(bancoDados, id_equipamento):
            info_cal.update_info_equip(bancoDados, id_equipamento, certificado, data_cal, validade_cal)
            return

        else:
            if info_cal.validar_id_controle(bancoDados, id_):
                raise ValueError("O ID da instrução já existe. Tente novamente.")

            sql = "INSERT INTO controle (id, id_equipamento, certificado, validade_cal, data_cal) VALUES (%s, %s, %s, %s, %s)"
            values = (id_, id_equipamento, certificado, data_cal, validade_cal)

            try:
                mycursor.execute(sql, values)
                bancoDados.dbConnection.commit()
            except Exception as e:
                bancoDados.dbConnection.rollback()
                raise ValueError("Erro ao cadastrar informações: " + str(e))

        mycursor.close()

    @staticmethod
    def update_info_equip(bancoDados, id_equipamento, certificado, data_cal, validade_cal):
        mycursor = bancoDados.dbConnection.cursor()

        sql = "UPDATE controle SET certificado = %s, data_cal = %s, validade_cal = %s WHERE id_equipamento = %s"
        values = (certificado, data_cal, validade_cal, id_equipamento)

        try:
            mycursor.execute(sql, values)
            bancoDados.dbConnection.commit()
        except Exception as e:
            bancoDados.dbConnection.rollback()
            raise ValueError("Erro ao atualizar informações: " + str(e))

        mycursor.close()        

    @staticmethod
    def validar_id_controle(bancoDados, id):
        mycursor = bancoDados.dbConnection.cursor()

        sql = "SELECT id FROM controle WHERE id = %s"
        values = (id,)

        mycursor.execute(sql, values)
        result = mycursor.fetchone()

        return result is not None
    
    @staticmethod
    def validar_id_equipamento(bancoDados, id_equipamento):
        mycursor = bancoDados.dbConnection.cursor()

        sql = "SELECT id FROM equipamentos WHERE id = %s"
        values = (id_equipamento,)

        mycursor.execute(sql, values)
        result = mycursor.fetchone()

        return result is not None
    
    @staticmethod
    def certificado_id_equipamento(bancoDados, id_equipamento):
        mycursor = bancoDados.dbConnection.cursor()

        sql = "SELECT id FROM controle WHERE id_equipamento = %s"
        values = (id_equipamento,)

        mycursor.execute(sql, values)
        result = mycursor.fetchone()

        return result is not None
    

    @staticmethod
    def apagar_controle(bancoDados, criteria, value):
        mycursor = bancoDados.dbConnection.cursor()

        column_mapping = {
            "ID": "id",
            "Certificado": "certificado"
        }

        column_name = column_mapping.get(criteria)
        if not column_name:
            return False, f"Critério desconhecido: {criteria}"

        sql = f"SELECT * FROM controle WHERE {column_name} = %s"
        value_tuple = (value,)

        try:
            mycursor.execute(sql, value_tuple)
            results = mycursor.fetchall()

            if not results:
                return False, f"Nenhum registro de Controle encontrado com esse {criteria}: {value}"
            return True, "Registro encontrado e pronto para ser apagado."

        except Exception as e:
            return False, f"Erro ao tentar buscar registro com {criteria} = {value}: {str(e)}"

        finally:
            mycursor.close()

    @staticmethod
    def confirm_and_delete(bancoDados, criteria, value):
        mycursor = bancoDados.dbConnection.cursor()

        column_mapping = {
            "ID": "id",
            "Certificado": "certificado"
        }

        column_name = column_mapping.get(criteria)

        delete_sql = f"DELETE FROM controle WHERE {column_name} = %s"
        value_tuple = (value,)

        try:
            mycursor.execute(delete_sql, value_tuple)
            bancoDados.dbConnection.commit()
        except Exception as e:
            bancoDados.dbConnection.rollback()
            raise Exception(f"Erro ao tentar apagar registro com {criteria} = {value}: {str(e)}")
        finally:
            mycursor.close()

    @staticmethod
    def pesquisar_por_certificado(bancoDados, certificado):
        mycursor = bancoDados.dbConnection.cursor()
        mycursor.execute("SELECT * FROM controle WHERE certificado = %s", (certificado,))
        results = mycursor.fetchall()
        mycursor.close()
        return results

    @staticmethod
    def equipamentos_vencidos(bancoDados):
        mycursor = bancoDados.dbConnection.cursor()
        data_atual = datetime.date.today().strftime("%Y-%m-%d")
        mycursor.execute("SELECT * FROM controle WHERE validade_cal < %s", (data_atual,))
        results = mycursor.fetchall()
        mycursor.close()
        return results

    @staticmethod
    def equipamentos_a_vencer(bancoDados, data):
        mycursor = bancoDados.dbConnection.cursor()
        data_str = data.strftime("%Y-%m-%d")
        mycursor.execute("SELECT * FROM controle WHERE validade_cal <= %s", (data_str,))
        results = mycursor.fetchall()
        mycursor.close()
        return results

    @staticmethod
    def equipamentos_vencendo_em_um_mes(bancoDados):
        mycursor = bancoDados.dbConnection.cursor()
        data_atual = datetime.date.today()
        um_mes_a_partir_de_hoje = data_atual + datetime.timedelta(days=30)
        mycursor.execute("SELECT * FROM controle WHERE validade_cal > %s AND validade_cal <= %s", (data_atual, um_mes_a_partir_de_hoje))
        results = mycursor.fetchall()
        mycursor.close()
        return results


"""
    @staticmethod
    def pesquisar_controle(bancoDados):
        mycursor = bancoDados.dbConnection.cursor()

        while True:
            print("Escolha uma opção:")
            print("1. Pesquisar por Certificado")
            print("2. Pesquisar por Validade de Calibração")
            print("0. Sair")

            opcao = int(input())

            if opcao == 0:
                break

            elif opcao == 1:
                # Solicita ao usuário o número do certificado
                certificado = input("Digite o número do certificado: ")

                # Executa a consulta SQL
                mycursor.execute("SELECT * FROM controle WHERE certificado = %s", (certificado,))

                # Recupera os resultados da consulta
                results = mycursor.fetchall()

                # Exibe os resultados
                if results:
                    print("Registros de Controle encontrados:")
                    for result in results:
                        print(result)
                else:
                    print("Nenhum registro de Controle encontrado.")

            elif opcao == 2:
                # Obtém a data atual
                data_atual = datetime.date.today()
                data_atual_str = data_atual.strftime("%Y-%m-%d")

                print("Escolha uma opção:")
                print("1. Equipamentos Vencidos")
                print("2. Equipamentos a Vencer")
                print("3. Equipamentos que vão vencer dentro de um mês")
                sub_opcao = int(input())

                if sub_opcao == 1:
                    # Exibe os equipamentos com data de calibração vencida
                    mycursor.execute("SELECT * FROM controle WHERE validade_cal < %s", (data_atual_str,))
                    results = mycursor.fetchall()

                    if results:
                        print("Equipamentos Vencidos:")
                        for result in results:
                            print(result)
                    else:
                        print("Nenhum equipamento vencido encontrado.")

                elif sub_opcao == 2:
                    # Solicita a data ao usuário
                    data_informada = input("Insira a data (no formato YYYY-MM-DD) até a qual você deseja verificar os equipamentos a vencer: ")

                    try:
                        # Verifica se a data informada é válida
                        data_informada = datetime.datetime.strptime(data_informada, "%Y-%m-%d").date()

                        # Exibe os equipamentos com data de calibração a vencer até a data informada
                        mycursor.execute("SELECT * FROM controle WHERE validade_cal <= %s", (data_informada,))
                        results = mycursor.fetchall()

                        if results:
                            print("Equipamentos a Vencer até", data_informada, ":")
                            for result in results:
                                print(result)
                        else:
                            print("Nenhum equipamento a vencer até", data_informada, "encontrado.")
                    except ValueError:
                        print("Data informada é inválida. Certifique-se de usar o formato YYYY-MM-DD.")

                elif sub_opcao == 3:
                    # Calcula a data daqui a um mês
                    um_mes_a_partir_de_hoje = data_atual + datetime.timedelta(days=30)
                    um_mes_a_partir_de_hoje_str = um_mes_a_partir_de_hoje.strftime("%Y-%m-%d")

                    # Exibe os equipamentos que vão vencer dentro de um mês
                    mycursor.execute("SELECT * FROM controle WHERE validade_cal > %s AND validade_cal <= %s", (data_atual_str, um_mes_a_partir_de_hoje_str))
                    results = mycursor.fetchall()

                    if results:
                        print("Equipamentos que vão vencer dentro de um mês:")
                        for result in results:
                            print(result)
                    else:
                        print("Nenhum equipamento que vai vencer dentro de um mês encontrado.")

                else:
                    print("Opção inválida.")

        mycursor.close()

"""
