import sys
import os

''' Adiciona o diretório raiz do projeto ao sys.path para que 
as importações de controller e models funcionem corretamente 
a partir do gui.py'''
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from gui import AppGUI

if __name__ == "__main__":
    try:
        app = AppGUI()
        app.mainloop()

    except ImportError as e:
        print("\n=== Erro de importação crítico ===")
        print("Certifique-se de que sua estrutura de pastas está correta:")
        print(" - controllers/sistema.py")
        print(" - models/carrinho.py, models/pagamento.py")
        print(" - Todas as subpastas ('controllers' e 'models') devem " \
        "ter um arquivo vazio '__init__.py'")
        print(f"Detalhe do erro: {e}")
        sys.exit(1)

    print("Obrigado por usar o sistema do mercado!")        