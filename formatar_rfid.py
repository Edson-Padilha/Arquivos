from PySide6.QtWidgets import (QApplication,  QMainWindow, QVBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QFileDialog,
                               QWidget)
from PySide6.QtCore import Qt 
import sys
import os

class FormatarArquivoRFID(QMainWindow):
    def __init__(self):
        super().__init__()

        # Remover os botões de minimizar e maximizar
        self.setWindowFlags(self.windowFlags() &  ~Qt.WindowMinimizeButtonHint & ~Qt.WindowMaximizeButtonHint)

        self.setWindowTitle("Formatar Arquivo RFID")
        self.setFixedSize(450, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Widgets
        self.label_arquivo = QLabel("Arquivo RFID:")
        self.line_edit_arquivo = QLineEdit()
        self.button_selecionar_arquivo = QPushButton("Selecionar")
        self.button_formatar = QPushButton("Formatar")
        self.label_status = QLabel("...")
        self.label_status.setAlignment(Qt.AlignCenter)

        # Layout
        self.layout.addWidget(self.label_arquivo)
        self.layout.addWidget(self.line_edit_arquivo)
        self.layout.addWidget(self.button_selecionar_arquivo)
        self.layout.addWidget(self.button_formatar)
        self.layout.addWidget(self.label_status)

        # Conectar sinais aos slots
        self.button_selecionar_arquivo.clicked.connect(self.selecionar_arquivo)
        self.button_formatar.clicked.connect(self.formatar_arquivo)

        self.arquivo_entrada = ""
    
    def selecionar_arquivo(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Selecionar Arquivo RFID", "", "Arquivos de Texto (*.txt);;Todos os Arquivos (*)")
        
        if file_path:
            self.line_edit_arquivo.setText(file_path)
            self.arquivo_entrada = file_path
            self.label_status.setText("Arquivo de entrada selecionado.")
        else:
            self.label_status.setText("Nenhum arquivo selecionado.")
            self.arquivo_entrada = ""
            self.line_edit_arquivo.clear() # Limpa o campo de entrada
    
    def formatar_arquivo(self):
        if not self.arquivo_entrada:
            self.label_status.setText("Por favor, selecione um arquivo primeiro.")
            return

        try:
            diretorio, nome_arquivo = os.path.split(self.arquivo_entrada)
            nome_base, extensao = os.path.splitext(nome_arquivo)
            arquivo_saida = os.path.join(diretorio, f"{nome_base}Convertido{extensao}")

            with open(self.arquivo_entrada, 'r') as arq_entrada, \
                open(arquivo_saida, 'w') as arq_saida:
                
                for linha in arq_entrada:
                    elementos = linha.strip().split()
                    
                    for elemento in elementos:
                        arq_saida.write(elemento + '\n')
            self.label_status.setText(f"Arquivo convertido e salvo como: {arquivo_saida}")
            self.line_edit_arquivo.clear() # Limpa o lineEdit após conversão
            self.arquivo_entrada = "" # Reseta o arquivo de entrada

        except Exception as e:
            self.label_status.setText(f"Ocorreu um erro: {e}")

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = FormatarArquivoRFID()
    window.show()
    sys.exit(app.exec())

# Comando para criar executável: pyinstaller --name Formatar_Arquivo --noconsole --onefile --icon=bar-code.ico formatar_rfid.py