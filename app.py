from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mon App</title>
        <style>
            body {
                background-color: #1e1e2f;
                color: white;
                text-align: center;
                font-family: Arial, sans-serif;
            }
            h1 {
                color: #00ffcc;
                font-size: 50px;
                margin-top: 100px;
            }
            p {
                color: #ffcc00;
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Mon Application DevOps</h1>
        <p>Bienvenue dans mon projet CI/CD avec Jenkins</p><br>
        <p>nassima tkkkkk</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)