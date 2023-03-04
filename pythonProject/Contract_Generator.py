def gera_contrato(nome_Contratante, nome_Contratado, Endereco, CPF_CNPJ, Razao_Social, vlr_Contrato, objeto):
    contrato = f"""
Contrato de Prestação de Serviços

Entre:
{nome_Contratante}, Mominado "Contratante"
e
{nome_Contratado}, Nominado "Contratado"

Objeto:
O presente contrato tem como objeto a prestação de serviços de {objeto} pelo Contratado ao Contratante.

Cláusulas e Obrigações legais do Contrato:
Cláusula 1: O Contratado se compromete a prestar  serviços de {objeto} de forma satisfatória e dentro do prazo estabelecido.
Cláusula 2: O Contratante se compromete a pagar ao Contratado o valor correspondente aos serviços prestados.
Cláusula 3: O contrato tem estabelecido, um  total de {objeto} até sua conclusão
Cláusula 4: O contrato contará com a disponibilidade de {objeto}. caso sejam necessárias
Cláusula 5: O contrato terá um valor fixo de {objeto}

E por assim estarem justos e contratados, assinam o presente contrato em duas vias de igual teor e forma.

{nome_Contratante}
{nome_Contratado}
{Endereco}
{CPF_CNPJ}
{Razao_Social}
{vlr_Contrato}
    """
    return contrato.format(nome_Contratante=nome_Contratante, nome_Contratado=nome_Contratado, Endereco=Endereco, CPF_CNPJ=CPF_CNPJ, Razao_Social=Razao_Social, vlr_Contrato=vlr_Contrato, objeto=objeto)

print(gera_contrato("Cleverson Santos", "Drika", "Rua da Paz 414", "23.416.612/0001-20", "We Are Testers", "R$ 45.500", "Automação de testes"))
