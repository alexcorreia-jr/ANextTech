from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="ANextTech",
    description="Plataforma de tecnologia, software e SaaS",
    version="0.1.0",
)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


@app.get("/", response_class=HTMLResponse)
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="theme-color" content="#080b16">
        <title>ANextTech | Build What's Next</title>
        <style>
            * { box-sizing: border-box; }

            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 24px;
                color: #f4f7ff;
                background:
                    radial-gradient(ellipse at 50% 35%, #18213d 0%, #080b16 65%);
                font-family: Inter, system-ui, sans-serif;
                text-align: center;
            }

            main { width: 100%; max-width: 760px; }

            .logo {
                display: block;
                width: 100%;
                max-width: 650px;
                height: auto;
                margin: 0 auto 24px;
                filter: drop-shadow(0 0 28px #572cff35);
            }

            h1 {
                font-size: clamp(2rem, 6vw, 3.5rem);
                margin: 12px 0;
                letter-spacing: -1.5px;
            }

            h1 span {
                color: #72dcff;
            }

            p {
                color: #aab5d0;
                line-height: 1.8;
                font-size: 1.05rem;
            }

            .status {
                display: inline-flex;
                align-items: center;
                gap: 9px;
                padding: 10px 16px;
                margin-top: 20px;
                border: 1px solid #263c52;
                border-radius: 999px;
                color: #baf8df;
                background: #10251f;
                font-size: 0.9rem;
            }

            .dot {
                width: 8px;
                height: 8px;
                background: #42e6a4;
                border-radius: 50%;
            }

            footer {
                margin-top: 48px;
                color: #64708b;
                font-size: 0.8rem;
            }
        </style>
    </head>
    <body>
        <main>
            <img class="logo"
                 src="/static/images/logo.png"
                 alt="Logo ANextTech">

            <h1>O futuro começa <span>agora.</span></h1>

            <p>
                Tecnologia, software e soluções SaaS para transformar
                ideias em experiências digitais.
            </p>

            <div class="status">
                <span class="dot"></span>
                ANextTech API iniciada
            </div>

            <footer>ANextTech · Build What's Next.</footer>
        </main>
    </body>
    </html>
    """


@app.get("/health")
def verificar_saude():
    return {
        "status": "healthy",
        "servico": "ANextTech API",
        "horario": datetime.now(timezone.utc).isoformat(),
    }
