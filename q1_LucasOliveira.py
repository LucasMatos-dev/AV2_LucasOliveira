import random

transacao_com_dinheiro = lambda fundos_usuario: (
    print("Recebendo dinheiro"),
    (lambda quantia_adicionada: (
        print(f"\nEmitindo Comprovante de Pagamento: {(fundos_usuario + quantia_adicionada):.2f}"),
        "Transação concluída"
    ))(float(input("Informe o valor desejado: ")))[1]
)[1]

processar_transacao = lambda fundos_usuario, nome_usuario, tipo_transacao: (
    print(f"Detalhes da {tipo_transacao}: \nUsuário: {nome_usuario} // Créditos: {fundos_usuario:.2f}"),
    (lambda escolha: "Transação concluída" if escolha == "Confirmar" else "Transação encerrada")(
        input("Confirme ou cancele o tipo de transação ('Confirmar' ou 'Cancelar'): ")
    )
)[1]

criar_transacao = lambda fundos_usuario, nome_usuario: (
    (lambda tipo_transacao: 
         transacao_com_dinheiro(fundos_usuario) if tipo_transacao == "Cash" else (
         processar_transacao(fundos_usuario, nome_usuario, tipo_transacao) if tipo_transacao in ["Fund Transfer", "Credit"] else (
         "Tipo de Transação Não existe - Transação cancelada"
    )))(input("Digite o tipo de transação (Cash, Fund Transfer, Credit): "))
)

print("Criando transação...!\n")

nome_usuario = input("Por favor, digite seu nome de usuário: ")
senha_usuario = input("Por favor, digite sua senha: ")

autenticar_usuario = lambda username, password: username == "admin" and password == "admin123"
fundos_usuario = round(random.uniform(1, 2000), 2) 

resultado = criar_transacao(fundos_usuario, nome_usuario)
print(resultado)
