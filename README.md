# 📰 Newsletter de Notícias FIIs

Sistema automatizado que coleta notícias sobre Fundos Imobiliários (FIIs) do site [fiis.com.br](https://fiis.com.br/noticias/), resume-as utilizando inteligência artificial (OpenAI GPT-4.1-mini) e envia um resumo diário por email.

## 🎯 Funcionalidades

- **Web Scraping**: Extração automática de notícias do site fiis.com.br usando Playwright
- **Resumo com IA**: Utiliza OpenAI GPT-4.1-mini para criar resumos inteligentes das notícias
- **Envio por Email**: Envia newsletter formatada com todas as notícias resumidas

## 📋 Pré-requisitos

- Python 3.13 ou superior
- Conta OpenAI com API Key
- Conta Gmail (ou outro serviço SMTP) para envio de emails
- Playwright instalado e configurado

## 🚀 Instalação

1. Clone o repositório ou baixe os arquivos do projeto

2. Instale as dependências usando `uv` (recomendado) ou `pip`:
   ```bash
   # Com uv
   uv sync
   
   # Ou com pip
   pip install -r requirements.txt
   ```

3. Instale os navegadores do Playwright:
   ```bash
   playwright install chromium
   ```

4. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```env
   OPENAI_API_KEY=sua_chave_api_openai
   EMAIL_ADDRESS=seu_email@gmail.com
   EMAIL_PASSWORD=sua_senha_app_gmail
   DESTINATARIOS=destinatario1@email.com,destinatario2@email.com
   ```

### 🔐 Configuração do Gmail

Para usar o Gmail como servidor SMTP, você precisará criar uma **Senha de App**:

1. Acesse sua [Conta do Google](https://myaccount.google.com/)
2. Vá em **Segurança** → **Verificação em duas etapas** (deve estar ativada)
3. Role até **Senhas de app**
4. Selecione **Email** e **Outro (personalizado)** → digite "Newsletter FIIs"
5. Copie a senha gerada e use no arquivo `.env`

## 📖 Uso

Execute o script principal:

```bash
python newsletter_fiis.py
```

O script irá:
1. 🔎 Coletar todas as notícias do site fiis.com.br/noticias/
2. 🧠 Resumir cada notícia usando IA
3. 📧 Enviar um email com todos os resumos formatados

## 📁 Estrutura do Projeto

```
noticias/
├── newsletter_fiis.py  # Script principal com todas as funcionalidades
├── pyproject.toml      # Configuração do projeto e dependências
├── uv.lock            # Lock file das dependências
├── .env               # Variáveis de ambiente (não versionado)
└── README.md          # Este arquivo
```

## 🔧 Dependências

- **playwright**: Automação de navegador para web scraping
- **openai**: Cliente Python para API da OpenAI
- **python-dotenv**: Carregamento de variáveis de ambiente

## ⚙️ Configuração Avançada

### Personalizar o modelo de IA

No arquivo `newsletter_fiis.py`, linha 80, você pode alterar o modelo:
```python
model="gpt-4.1-mini"  # Altere para gpt-4, gpt-3.5-turbo, etc.
```

### Ajustar o prompt de resumo

Modifique a função `resumir_noticia()` para personalizar como as notícias são resumidas.

### Usar outro servidor SMTP

Altere as configurações na função `enviar_email()` (linha 102) para usar outro servidor SMTP:
```python
with smtplib.SMTP("smtp.seuservidor.com", 587) as server:
```

## 🤖 Automação

Para executar diariamente, você pode usar:

- **Windows**: Agendador de Tarefas
- **Linux/Mac**: Cron jobs
- **Cloud**: GitHub Actions, AWS Lambda, etc.

Exemplo de cron job (executa diariamente às 9h):
```bash
0 9 * * * cd /caminho/do/projeto && python newsletter_fiis.py
```

## ⚠️ Avisos

- O web scraping pode ser afetado por mudanças na estrutura do site fiis.com.br
- O uso da API da OpenAI gera custos (consulte a [tabela de preços](https://openai.com/pricing))
- Certifique-se de ter permissão para fazer scraping do site antes de usar


## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

Desenvolvido com ❤️ para facilitar o acompanhamento de notícias sobre FIIs
