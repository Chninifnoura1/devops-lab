from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    #return "Version 1 - CI/CD avec Jenkins"
    #return "Version 4 - Déployée automatiquement"
    #return "VChninif noura - Déployée automatiquement"
    return "nassima tk fffffff- Déployée automatiquement master il groupe 1"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
