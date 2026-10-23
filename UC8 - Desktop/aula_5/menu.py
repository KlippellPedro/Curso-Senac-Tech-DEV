from picole import Picole
class Menu:
    def __init__(self):
        self.opcoes = [
            Picole(1, "Fruki", 2.00),
            Picole(2, "Sukita", 3.00),
            Picole(3, "Fanta Uva", 4.00),
            Picole(4, "Monster Branco", 5.00),
            Picole(5, "Maromba", 6.00)
        ]
    def exibir_menu(self):
        print("=== Bem-vindo a Sorveteria TabajaraCorp ===")
        print("--- Menu de opções ---")
        for picole in self.opcoes:
            print(f"{picole.codigo} - Picolé de {picole.nome} - R${picole.preco:.2f}")
        
    def obter_picole_por_codigo(self, codigo):
        for picole in self.opcoes:
            if picole.codigo == codigo:
                return picole
        return None
    