from playwright.sync_api import sync_playwright
from openai import OpenAI
from dotenv import load_dotenv
import os
# =========================
# CONFIG
# =========================
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extrair_noticias():
    with sync_playwright() as p:
        # Abre o navegador
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Acessa o site
        page.goto(
            "https://fiis.com.br/noticias/",
            wait_until="domcontentloaded",
            timeout=60000
        )

        # Espera o grid de notícias existir
        page.wait_for_selector("div.higlith__grid__box")

        # Seleciona todas as notícias
        noticias = page.locator("div.higlith__grid__box")

        print(f"\nTotal de notícias encontradas: {noticias.count()}\n")

        noticias_extraidas = []
        # Loop pelas notícias
        for i in range(noticias.count()):
            noticia = noticias.nth(i)

            titulo = noticia.locator(
                "h3.higlith__grid__box__title"
            ).inner_text()

            url = noticia.locator("a").first.get_attribute("href")

            horario = noticia.locator("span").inner_text()

            

            paragrafos = page.locator("p").all_inner_texts()

            

            noticias_extraidas.append({
                "url": url,
                "titulo": titulo,
                "horario": horario,
                "paragrafos": paragrafos
            })


        

        context.close()
        browser.close()
        return noticias_extraidas


# =========================
# FUNÇÃO: RESUMIR COM OPENAI
# =========================
def resumir_noticia(texto):
    prompt = f"""
    Você é um analista financeiro.
    Leia a notícia abaixo e gere um resumo com os principais pontos,
    em linguagem clara e objetiva.

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
# MAIN
# =========================
if __name__ == "__main__":
    print("🔎 Coletando notícia...")
    noticias_extraidas = extrair_noticias()

    print("\n🧠 Resumindo com IA...")
    resumo = resumir_noticia(noticias_extraidas)

    print("\n📌 RESUMO FINAL:\n")
    print(resumo)



