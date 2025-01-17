# Pesquisa de Satisfação NPS

Uma aplicação simples para coletar a opinião dos seus clientes sobre a sua empresa, utilizando a métrica NPS. A ideia aqui é que os clientes dão uma nota de 0 a 10 e, se for abaixo de 10, podem deixar um feedback. As respostas são enviadas diretamente para um e-mail configurado no código.

## Como funciona?

### Interface para o cliente:

* O cliente vê uma escala de 0 a 10 e clica na nota que deseja dar.
* Se a nota for abaixo de 10, um campo aparece para que ele deixe um feedback.
* Se for 10, a avaliação é enviada imediatamente sem a necessidade de um comentário.

### Back-end:

* Um servidor Flask recebe os dados enviados pelo cliente.
* Dependendo da nota, o sistema envia um e-mail com a nota e o feedback (se houver).

### E-mail:

* Os dados são enviados para um destinatário configurado no código por meio de SMTP do Gmail.

## Configurações

### Requisitos:

* Python
* Flask

### Instalando dependências:
```
pip install flask
```
## Configurações:

### Edite o arquivo nps.py:

* Remetente: Substitua email pela conta de e-mail que irá enviar as mensagens.
* Senha: Coloque a senha do app do Gmail (não use a senha principal da sua conta).
* Destinatário: Altere o campo destinatario para o e-mail que receberá as respostas.

### Ative a autenticação em dois fatores na sua conta do Gmail e gere uma senha de app.

## Rodando o projeto:

### No terminal, execute:
```
python nps.py
```
### Acesse pelo navegador

## Melhorias possíveis:

* Adicionar um banco de dados para salvar as respostas e ter um histórico.
* Melhorar a segurança do envio dos e-mails.
* Melhorar o Design.
