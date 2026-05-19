# 💰 FinTrack — Controle de Finanças Pessoais

> Uma aplicação moderna de finanças pessoais para acompanhar receitas, despesas, metas financeiras e comportamento de gastos através de dashboards interativos.

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688)
![React](https://img.shields.io/badge/React-18-61DAFB)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)

---

## 📋 Sumário

* [Visão Geral](#visão-geral)
* [Funcionalidades](#funcionalidades)
* [Stack Tecnológica](#stack-tecnológica)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Primeiros Passos](#primeiros-passos)
* [Documentação da API](#documentação-da-api)
* [Variáveis de Ambiente](#variáveis-de-ambiente)
* [Executando os Testes](#executando-os-testes)
* [Contribuindo](#contribuindo)

---

## Visão Geral

O FinTrack é uma plataforma full-stack de gerenciamento financeiro pessoal que permite aos usuários:

* Registrar e acompanhar **receitas e despesas** com categorias personalizadas
* Visualizar **gráficos financeiros mensais** e resumos de saldo
* Definir e monitorar **metas financeiras pessoais**
* Utilizar **sugestões de categorias com IA** baseadas na descrição das transações
* Exportar relatórios e gerenciar transações recorrentes

---

## Funcionalidades

### MVP (Principal)

* [x] Cadastro de usuários e autenticação JWT
* [x] Criar, editar e excluir transações financeiras (receita/despesa)
* [x] Categorização manual de transações
* [x] Cálculo automático de saldo
* [x] Histórico completo de transações com filtros
* [x] Gráficos financeiros mensais (barra, pizza e linha)
* [x] Metas financeiras pessoais

### Funcionalidades Extras (Roadmap)

* [ ] Sugestão automática de categorias com IA
* [ ] Previsão mensal de gastos baseada no histórico
* [ ] Alertas de limite de gastos
* [ ] Dashboard avançado de análises
* [ ] Metas gamificadas com progresso visual
* [ ] Exportação de relatórios em PDF/Excel
* [ ] Integração bancária simulada
* [ ] Alternância entre modo claro/escuro
* [ ] Filtros por período, categoria e tipo
* [ ] Upload de comprovantes/anexos
* [ ] Suporte a transações recorrentes
* [ ] Notificações em tempo real com WebSocket

---

## Stack Tecnológica

| Camada         | Tecnologia                       |
| -------------- | -------------------------------- |
| Frontend       | React 18, Tailwind CSS, Recharts |
| Backend        | FastAPI, SQLAlchemy, Alembic     |
| Banco de Dados | MySQL 8.0                        |
| Autenticação   | JWT (python-jose)                |
| Containers     | Docker, Docker Compose           |
| CI/CD          | GitHub Actions                   |
| Testes         | Pytest, React Testing Library    |

---

## Estrutura do Projeto

```bash
fintrack/
├── backend/
│   ├── app/
│   │   ├── api/v1/endpoints/    # Manipuladores de rotas
│   │   ├── core/                # Configurações, segurança e JWT
│   │   ├── models/              # Modelos ORM do SQLAlchemy
│   │   ├── schemas/             # Schemas Pydantic
│   │   ├── services/            # Regras de negócio
│   │   └── utils/               # Utilitários
│   ├── tests/                   # Suite de testes com Pytest
│   ├── Dockerfile
│   ├── requirements.txt
│   └── alembic/                 # Migrações do banco
├── frontend/
│   ├── src/
│   │   ├── components/          # Componentes reutilizáveis
│   │   ├── pages/               # Componentes de páginas
│   │   ├── hooks/               # Hooks customizados do React
│   │   ├── store/               # Gerenciamento de estado com Zustand
│   │   ├── services/            # Camada de serviços da API
│   │   └── utils/               # Helpers e formatadores
│   ├── Dockerfile
│   └── package.json
├── docker/
│   └── mysql/init.sql
├── docker-compose.yml
├── docker-compose.prod.yml
└── .github/workflows/           # Pipelines de CI/CD
```

---

## Primeiros Passos

### Pré-requisitos

* [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/)
* [Node.js 20+](https://nodejs.org/) (para desenvolvimento local do frontend)
* [Python 3.11+](https://www.python.org/) (para desenvolvimento local do backend)

### 1. Clone o repositório

```bash
git clone https://github.com/your-username/fintrack.git
cd fintrack
```

### 2. Configure as variáveis de ambiente

```bash
cp .env.example .env
# Edite o arquivo .env com seus valores
```

### 3. Execute com Docker Compose

```bash
docker-compose up --build
```

A aplicação estará disponível em:

* **Frontend**: [http://localhost:3000](http://localhost:3000)
* **Backend API**: [http://localhost:8000](http://localhost:8000)
* **Documentação da API (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Desenvolvimento Local (sem Docker)

**Backend:**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**

```bash
cd frontend
npm install
npm run dev
```

---

## Documentação da API

Após iniciar o backend, acesse a documentação interativa da API:

* **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Principais Endpoints

| Método | Endpoint                    | Descrição                     |
| ------ | --------------------------- | ----------------------------- |
| POST   | `/api/v1/auth/register`     | Registrar novo usuário        |
| POST   | `/api/v1/auth/login`        | Login e obtenção do token JWT |
| GET    | `/api/v1/transactions/`     | Listar transações             |
| POST   | `/api/v1/transactions/`     | Criar transação               |
| PUT    | `/api/v1/transactions/{id}` | Atualizar transação           |
| DELETE | `/api/v1/transactions/{id}` | Excluir transação             |
| GET    | `/api/v1/categories/`       | Listar categorias             |
| POST   | `/api/v1/categories/`       | Criar categoria               |
| GET    | `/api/v1/goals/`            | Listar metas                  |
| POST   | `/api/v1/goals/`            | Criar meta                    |
| GET    | `/api/v1/dashboard/summary` | Resumo do dashboard           |
| GET    | `/api/v1/dashboard/charts`  | Dados dos gráficos            |

---

## Variáveis de Ambiente

```env
# Backend
DATABASE_URL=mysql+pymysql://fintrack:fintrack@db:3306/fintrack
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Frontend
VITE_API_URL=http://localhost:8000/api/v1

# MySQL
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=fintrack
MYSQL_USER=fintrack
MYSQL_PASSWORD=fintrack
```

---

## Executando os Testes

**Backend:**

```bash
cd backend
pytest tests/ -v --cov=app
```

**Frontend:**

```bash
cd frontend
npm run test
```

---

## Contribuindo

1. Faça um fork do repositório
2. Crie sua branch de feature: `git checkout -b feat/minha-feature`
3. Faça commit das alterações: `git commit -m 'feat: adiciona minha feature'`
4. Envie para a branch: `git push origin feat/minha-feature`
5. Abra um Pull Request

Siga o padrão de commits do [Conventional Commits](https://www.conventionalcommits.org/?utm_source=chatgpt.com).

---

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

<p align="center">Desenvolvido com ❤️ usando FastAPI + React</p>
