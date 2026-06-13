from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CodeAlpha DevOps Internship</h1>
    <h2>Task 1 - Azure CI/CD Pipeline</h2>
    <p>Successfully deployed using Azure DevOps, Docker, Azure Container Registry, and Azure App Service.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
