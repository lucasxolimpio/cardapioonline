from database_client import get_connection
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    with get_connection() as conn:  # Gerenciador de contexto para conexão
        # Use a conexão aqui se necessário
        pass
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)  # Lembre-se de desativar o debug em produção
