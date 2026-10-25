from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevPortfolio | CCA 2</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #f8fafc;
                line-height: 1.6;
            }

            header {
                padding: 24px 10%;
                background: #111c32;
                border-bottom: 1px solid #334155;
            }

            header h2 {
                color: #38bdf8;
            }

            main {
                max-width: 900px;
                margin: 80px auto;
                padding: 30px;
                text-align: center;
            }

            .tag {
                display: inline-block;
                color: #38bdf8;
                border: 1px solid #38bdf8;
                border-radius: 20px;
                padding: 6px 16px;
                margin-bottom: 20px;
            }

            h1 {
                font-size: 3rem;
                margin-bottom: 16px;
            }

            h1 span {
                color: #38bdf8;
            }

            .intro {
                color: #cbd5e1;
                font-size: 1.1rem;
                margin: 0 auto 30px;
                max-width: 650px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-top: 45px;
            }

            .card {
                background: #1e293b;
                padding: 25px;
                border-radius: 12px;
                border: 1px solid #334155;
            }

            .card h3 {
                color: #38bdf8;
                margin-bottom: 10px;
            }

            footer {
                text-align: center;
                padding: 25px;
                color: #94a3b8;
                border-top: 1px solid #334155;
            }

            @media (max-width: 600px) {
                h1 {
                    font-size: 2.2rem;
                }

                main {
                    margin: 35px auto;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <h2>DevPortfolio</h2>
        </header>

        <main>
            <div class="tag">Computer Science Student</div>

            <h1>Hello, I'm <span>Kushagra</span></h1>

            <p class="intro">
                An aspiring software developer exploring Python, web development,
                cloud computing, and DevOps. This portfolio is deployed through
                an automated CI/CD pipeline using Jenkins, Docker, and Kubernetes.
            </p>

            <div class="cards">
                <div class="card">
                    <h3>Python</h3>
                    <p>Building applications and solving problems.</p>
                </div>

                <div class="card">
                    <h3>Web Development</h3>
                    <p>Creating simple and responsive web experiences.</p>
                </div>

                <div class="card">
                    <h3>Cloud & DevOps</h3>
                    <p>Learning automated builds and container deployment.</p>
                </div>
            </div>
        </main>

        <footer>
            CCA 2 Project | Flask + Jenkins + Docker + Kubernetes
        </footer>
    </body>
    </html>
    """

@app.route("/health")

# Updated for the second CI/CD pipeline execution.
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
