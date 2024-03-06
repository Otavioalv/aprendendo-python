# Importar a bibliote
from flask import Flask;

# Configurar o flask
app = Flask(__name__);


#  iniciar o flask
if __name__ == "__main__":
    app.run(debug=True);
