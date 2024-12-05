def comparar_listas(arquivo1, arquivo2, arquivo_saida):
    """
    Compara duas listas de códigos RFID em arquivos .txt e gera um novo arquivo 
    contendo os elementos da primeira lista que não estão na segunda lista.

    Args:
        arquivo1 (str): Caminho para o arquivo da primeira lista.
        arquivo2 (str): Caminho para o arquivo da segunda lista.
        arquivo_saida (str): Caminho para o arquivo de saída.
    """
    try:
        # Lê os arquivos e cria conjuntos com os códigos RFID
        with open(arquivo1, 'r') as f1, open(arquivo2, 'r') as f2:
            set1 = set(f1.read().splitlines())
            set2 = set(f2.read().splitlines())

        # Encontra os elementos e cria conjuntos com os códigos RFID
        elementos_exclusivos = set1 - set2

        # Escreve os elementos exclusivos no arquivo de saída
        with open(arquivo_saida, 'w') as f_out:
            for elemento in elementos_exclusivos:
                f_out.write(elemento + '\n')

        print(f"Comparação concluída. Arquivo de saída gerado em: {arquivo_saida}")
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. verifique os caminhos fornecidos.")
    except Exception as e:
        print(f"Erro ao comparar listas: {e}")

arquivo1 = 'Lista_1.txt'
arquivo2 = 'Lista_2.txt'
arquivo_saida = 'Lista_1_exclusivos.txt'

comparar_listas(arquivo1, arquivo2, arquivo_saida)