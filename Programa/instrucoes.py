class Instrucao:
    def __init__(self, id, valor, unidade, incerteza, k, grau_de_liberdade, multiplicador):
        self.id = id
        self.valor = valor
        self.unidade = unidade
        self.incerteza = incerteza
        self.k = k
        self.grau_de_liberdade = grau_de_liberdade
        self.multiplicador = multiplicador

    @staticmethod
    def cadastrar(bancoDados, instrucao):
        mycursor = bancoDados.dbConnection.cursor()

        sql = """
            INSERT INTO instrucoes (
                id, valor, unidade, incerteza, k, grau_de_liberdade, multiplicador
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        data = (
            instrucao.id,
            instrucao.valor,
            instrucao.unidade,
            instrucao.incerteza,
            instrucao.k,
            instrucao.grau_de_liberdade,
            instrucao.multiplicador
        )

        try:
            mycursor.execute(sql, data)
            bancoDados.dbConnection.commit()
            return True
        except Exception as e:
            print("Erro ao cadastrar instrução:", e)
            bancoDados.dbConnection.rollback()
            return False

    @staticmethod
    def apagar(bancoDados, id):
        try:
            sql = "DELETE FROM instrucoes WHERE id = %s"
            mycursor = bancoDados.dbConnection.cursor()
            mycursor.execute(sql, (id,))
            bancoDados.dbConnection.commit()
            return True
        except Exception as e:
            bancoDados.dbConnection.rollback()
            print("Erro ao apagar instrução:", e)
            return False

    @staticmethod
    def pesquisar(bancoDados, id):
        mycursor = bancoDados.dbConnection.cursor()

        sql = "SELECT * FROM instrucoes WHERE id = %s"
        
        try:
            mycursor.execute(sql, (id,))
            results = mycursor.fetchall()
            return results
        except Exception as e:
            print("Erro ao pesquisar instrução:", e)
            return []

