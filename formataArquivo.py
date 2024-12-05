def converter_colunas(arquivo_entrada, arquivo_saida):

    with open(arquivo_entrada,'r') as arq_entrada, \
        open(arquivo_saida,'w') as arq_saida:

        for linha in arq_entrada:
            elementos = linha.strip().split()
            for elemento in elementos:
                arq_saida.write(elemento + '\n')

arquivo_entrada = 'C:\\Users\edson.p\Documents\RFID\RFID em produção 051224.txt'
arquivo_saida = 'C:\\Users\edson.p\Documents\RFID\RFID em produção 051224Convertido.txt'
converter_colunas(arquivo_entrada, arquivo_saida)
print("Processo concluido!")