# Script para publicar o projeto no GitHub
# Execute: .\publicar-github.ps1

Write-Host "🚀 Publicando projeto no GitHub..." -ForegroundColor Cyan
Write-Host ""

# Solicitar informações do usuário
$usuario = Read-Host "Digite seu usuário do GitHub"
$repositorio = Read-Host "Digite o nome do repositório (ex: newsletter-fiis)"

if ([string]::IsNullOrWhiteSpace($usuario) -or [string]::IsNullOrWhiteSpace($repositorio)) {
    Write-Host "❌ Erro: Usuário e nome do repositório são obrigatórios!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "📝 Configurando repositório remoto..." -ForegroundColor Yellow

# Verificar se já existe um remote
$remoteExists = git remote get-url origin 2>$null
if ($remoteExists) {
    Write-Host "⚠️  Remote 'origin' já existe. Removendo..." -ForegroundColor Yellow
    git remote remove origin
}

# Adicionar remote
$url = "https://github.com/$usuario/$repositorio.git"
git remote add origin $url

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Remote adicionado: $url" -ForegroundColor Green
} else {
    Write-Host "❌ Erro ao adicionar remote" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "📤 Enviando código para o GitHub..." -ForegroundColor Yellow
Write-Host "💡 Se solicitado, use seu Personal Access Token como senha" -ForegroundColor Cyan
Write-Host ""

# Fazer push
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Projeto publicado com sucesso!" -ForegroundColor Green
    Write-Host "🔗 Acesse: https://github.com/$usuario/$repositorio" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "❌ Erro ao fazer push. Verifique:" -ForegroundColor Red
    Write-Host "   1. O repositório foi criado no GitHub?" -ForegroundColor Yellow
    Write-Host "   2. Você tem permissão para acessar o repositório?" -ForegroundColor Yellow
    Write-Host "   3. Você usou um Personal Access Token como senha?" -ForegroundColor Yellow
}

