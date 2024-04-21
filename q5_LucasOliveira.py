import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)
iv = get_random_bytes(16)

encrypted_passwords = []
usernames = []

def senha_criptografada(password, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_password = pad(password.encode(), AES.block_size)
    encrypted_password = cipher.encrypt(padded_password)
    return encrypted_password

def descriptografar_senha(encrypted_password, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_password = cipher.decrypt(encrypted_password)
    unpadded_password = unpad(decrypted_password, AES.block_size)
    return unpadded_password.decode()

def authenticar_usuario(password, key, iv, stored_encrypted_password):
    decrypted_password = descriptografar_senha(stored_encrypted_password, key, iv)
    return password == decrypted_password

def armazenar_senha_criptografada(username, encrypted_password):
    encrypted_passwords.append((username, encrypted_password))

transacao_com_dinheiro = lambda fundos_usuario: print("Recebendo dinheiro") or (
    print(f"\nEmitindo Comprovante de Pagamento: {(fundos_usuario + float(input('Informe o valor desejado: '))):.2f}") or
    "Transação concluída"
)

processar_transacao = lambda fundos_usuario, nome_usuario, tipo_transacao: (
    print(f"Detalhes da {tipo_transacao}: \nUsuário: {nome_usuario} // Créditos: {fundos_usuario:.2f}") or
    ("Transação concluída" if input("Confirme ou cancele o tipo de transação ('Confirmar' ou 'Cancelar'): ") == "Confirmar" else "Transação encerrada")
)

criar_transacao = lambda fundos_usuario, nome_usuario: (
    transacao_com_dinheiro(fundos_usuario) if (tipo_transacao := input("Digite o tipo de transação (Cash, Fund Transfer, Credit): ")) == "Cash" else (
        processar_transacao(fundos_usuario, nome_usuario, tipo_transacao) if tipo_transacao in ["Fund Transfer", "Credit"] else "Tipo de Transação Não existe - Transação cancelada"
    )
)

admin_password_encrypted = senha_criptografada("admin123", key, iv)
armazenar_senha_criptografada("admin", admin_password_encrypted)

nome_usuario = input("Por favor, digite seu nome de usuário: ")
senha_usuario = input("Por favor, digite sua senha: ")

resultado = criar_transacao(1234.56, nome_usuario) if authenticar_usuario(senha_usuario, key, iv, admin_password_encrypted) else "Acesso negado."
print(resultado)
