from playwright.sync_api import sync_playwright
from openai import OpenAI
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =========================
# CONFIG
# =========================
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMAIL_REMETENTE = os.getenv("EMAIL_ADDRESS")
EMAIL_SENHA = os.getenv("EMAIL_PASSWORD")
EMAIL_DESTINO = os.getenv("DESTINATARIOS")


# =========================
# EXTRAI NOTÍCIAS
# =========================
def extrair_noticias():
    noticias_extraidas = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://fiis.com.br/noticias/", timeout=60000)
        page.wait_for_selector("div.higlith__grid__box")

        noticias = page.locator("div.higlith__grid__box")

        print(f"\nTotal de notícias encontradas: {noticias.count()}")

        for i in range(noticias.count()):
            noticia = noticias.nth(i)

            titulo = noticia.locator("h3").inner_text()
            url = noticia.locator("a").first.get_attribute("href")
            horario = noticia.locator("span").inner_text()

            # Abre a notícia
            page.goto(url, timeout=60000)
            page.wait_for_selector("p")

            paragrafos = page.locator("p").all_inner_texts()
            texto_completo = "\n".join(paragrafos)

            noticias_extraidas.append({
                "titulo": titulo,
                "horario": horario,
                "url": url,
                "texto": texto_completo
            })

            # Volta para lista
            page.go_back()

        browser.close()

    return noticias_extraidas


# =========================
# RESUMIR COM OPENAI
# =========================
def resumir_noticia(texto):
    prompt = f"""
    Você é um analista financeiro.
    Resuma a notícia abaixo destacando os principais pontos.

    NOTÍCIA:
    {texto}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Você resume notícias financeiras."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


# =========================
# ENVIAR EMAIL
# =========================
def enviar_email(conteudo):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_DESTINO
    msg["Subject"] = "📰 Resumo diário de notícias FIIs"

    msg.attach(MIMEText(conteudo, "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_REMETENTE, EMAIL_SENHA)
        server.send_message(msg)

    print("📧 Email enviado com sucesso!")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    print("🔎 Coletando notícias...")
    noticias = extrair_noticias()

    print("\n🧠 Resumindo notícias...")
    resumo_final = ""

    for noticia in noticias:
        resumo = resumir_noticia(noticia["texto"])
        resumo_final += f"""
📌 {noticia['titulo']}
🕒 {noticia['horario']}
🔗 {noticia['url']}

{resumo}

----------------------------------
"""

    enviar_email(resumo_final)
