import hashlib
"""Importa a biblioteca hashlib para realizar operações de hash, que são usadas para proteger senhas e outros dados sensíveis."""
class Usuario:
    def __init__(self, id_usuario: str, nome: str, login: str, senha_plana: str, papel: str):
        self.id_usuario = id_usuario
        self.nome = nome
        self.login = login
        self.senha_hash = self._hash_senha(senha_plana)
        self.papel=papel # Define o papel do usuário, que pode ser 'administrador' ou 'caixa', determinando seu nível de acesso no sistema.
    
    def _criptografar_senha(self, senha_plana: str) -> str:
        """Gera um hash SHA-256 da senha fornecida para armazenamento seguro."""
        return hashlib.sha256(senha_plana.encode()).hexdigest()
    """Converte a senha em uma representação hexadecimal do hash SHA-256, garantindo que a senha não seja armazenada em texto plano."""
    
    def verificar_senha(self, senha_digitada: str) -> bool:
        """Verifica se a senha digitada corresponde ao hash armazenado."""
        hash_digitado = self._criptografar_senha(senha_digitada)
        return self.senha_hash == hash_digitado # Retorna True se forem iguais

    def e_admin(self) -> bool:
        """Verifica se o usuário tem papel de administrador."""
        return self.papel.lower == 'administrador'
    """Retorna True se o papel do usuário for 'administrador', ignorando diferenças de maiúsculas e minúsculas."""
    
    def to_dict(self) -> dict:
        """Converte o objeto Usuario em um dicionário para facilitar a serialização em JSON."""
        return {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "login": self.login,
            "senha_hash": self.senha_hash,
            "papel": self.papel
        }
    
    @classmethod
    def from_dict(cls, dados: dict):
        """Cria uma instância de Usuario a partir de um dicionário, útil para desserialização de JSON."""
        usuario= cls(
            id_usuario=dados["id_usuario"],
            nome=dados["nome"],
            login=dados["login"],
            senha_plana=dados["senha_hash"],  # Aqui você pode querer ajustar dependendo de como você armazena a senha
            papel=dados["papel"]
        )
        usuario.senha_hash = dados["senha_hash"]
        return usuario