from flask import Flask, render_template, request, jsonify
import smtplib
import email.message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            data = request.get_json()
            nota = data.get("nota")
            comentario = data.get("feedback", "")


            print(f"Nota recebida: {nota}, Comentário: {comentario}")

            if nota is not None:
                if nota < 10 and comentario.strip():
                    enviar_email(nota, comentario)
                    return jsonify({"message": "Feedback enviado com sucesso!"}), 200
                elif nota == 10:
                    enviar_email(nota, "")
                    return jsonify({"message": "Avaliação enviada com sucesso!"}), 200
                else:
                    return jsonify({"message": "Aguardando feedback do cliente."}), 200
            else:
                return jsonify({"error": "Nota não fornecida!"}), 400
        except Exception as e:
            print(f"Erro no POST: {e}")
            return jsonify({"error": str(e)}), 500

    return render_template("index.html")

def enviar_email(nota, comentario):
    print("Iniciando envio de e-mail...")

    remetente = "email"
    senha = "senha_aplicativo"
    destinatario = "destinatario"

    corpo_email = f"""
    <p>Olá,</p>
    <p>O cliente respondeu com a nota: <strong>{nota}</strong></p>
    """
    if comentario:
        corpo_email += f"<p>Feedback: {comentario}</p>"
    corpo_email += "<p>Atenciosamente,<br>Sistema de Pesquisas</p>"

    msg = email.message.Message()
    msg['Subject'] = "Resposta da Pesquisa de Satisfação"
    msg['From'] = remetente
    msg['To'] = destinatario
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            print("Conectando ao servidor SMTP...")
            server.starttls()
            server.login(remetente, senha)
            print("Autenticação bem-sucedida!")
            server.sendmail(remetente, destinatario, msg.as_string().encode('utf-8'))
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        raise

if __name__ == "__main__":
    app.run(debug=True)
