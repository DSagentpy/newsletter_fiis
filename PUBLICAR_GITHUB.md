# 📤 Como Publicar no GitHub

## Passo a Passo

### 1. Criar o repositório no GitHub
1. Acesse: https://github.com/new
2. Escolha um nome (ex: `newsletter-fiis`)
3. **NÃO** marque "Add a README file" (já temos um)
4. **NÃO** adicione .gitignore (já temos um)
5. Clique em **"Create repository"**

### 2. Conectar e enviar o código

Após criar o repositório, execute os comandos abaixo no PowerShell (substitua `SEU_USUARIO` e `NOME_DO_REPOSITORIO`):

```powershell
cd "C:\Users\W-10\OneDrive\PROJETO PYTHON\noticias"

# Adicionar o repositório remoto (substitua SEU_USUARIO e NOME_DO_REPOSITORIO)
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git

# Enviar o código
git push -u origin main
```

### 3. Autenticação

Se solicitado, você precisará:
- **Usuário**: Seu username do GitHub
- **Senha**: Use um **Personal Access Token** (não sua senha normal)

#### Como criar um Personal Access Token:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Dê um nome (ex: "noticias-project")
4. Marque `repo` (acesso completo aos repositórios)
5. Generate token
6. **Copie o token** (você só verá uma vez!)
7. Use este token como senha quando solicitado

### 4. Verificar

Acesse seu repositório no GitHub e verifique se todos os arquivos foram enviados!

---

**Dica**: Se preferir usar SSH em vez de HTTPS, você precisará configurar uma chave SSH primeiro.

