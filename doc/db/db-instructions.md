# Guia de Uso do Banco de Dados HydroGuard

Este documento orienta sobre a configuração, inicialização e uso do banco de dados do projeto HydroGuard, complementando o MER já existente. Aqui você encontra instruções práticas para instalar dependências, configurar variáveis de ambiente, preparar o banco de dados PostgreSQL com PostGIS, rodar scripts de inicialização e popular a base com dados de exemplo.

---

## 1. Visão Geral do Banco de Dados

O banco de dados do HydroGuard foi projetado para armazenar informações de rios, trechos, estações de monitoramento, sensores, medições, modelos de machine learning, previsões de enchentes e alertas. Ele utiliza PostgreSQL com a extensão PostGIS para suportar dados geoespaciais (geometria de pontos e linhas).

- **Tecnologia:** PostgreSQL + PostGIS
- **ORM:** SQLAlchemy + GeoAlchemy2
- **Scripts principais:**
  - `init_db.py`: Criação das tabelas
  - `populate_db.py`: População inicial de dados
  - `crud.py`: Funções de manipulação (Create, Read, Update, Delete)
  - `models.py`: Definição das entidades e relacionamentos
  - `database_session.py`: Configuração da conexão e sessão

---

## 2. Instalação de Dependências

### a) Python
Certifique-se de ter o Python 3.8+ instalado.

### b) Instale os pacotes necessários:
```bash
pip install sqlalchemy psycopg2-binary python-dotenv geoalchemy2
```

### c) Instale o PostgreSQL e o PostGIS
No Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install postgresql postgis postgresql-14-postgis-3
```

---

## 3. Configuração do Banco de Dados

### a) Crie o banco de dados PostgreSQL
```bash
sudo -u postgres createdb <nome_do_banco>
```

### b) Habilite a extensão PostGIS (necessário ser superusuário):
```bash
sudo -u postgres psql -d <nome_do_banco>
# No prompt do psql:
CREATE EXTENSION IF NOT EXISTS postgis;
```

---

## 4. Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (pode usar `.env.example` como base):

```
HOST=<host_do_postgres>
DATABASE=<nome_do_banco>
USER=<usuario_postgres>
PASSWORD=<senha_postgres>
PORT=<porta_postgres>
```

Exemplo típico:
```
HOST=localhost
DATABASE=gs-disaster
USER=postgres
PASSWORD=suasenha
PORT=5432
```

---

## 5. Inicialização do Banco de Dados

### a) Crie as tabelas
Execute o script de inicialização:
```bash
python db/init_db.py
```
Isso criará todas as tabelas conforme definidas em `models.py`.

### b) Popule o banco com dados de exemplo
Execute:
```bash
python db/populate_db.py
```
Esse script insere um rio, um trecho, tipos de estação e sensor, três estações de monitoramento e nove sensores, conforme exemplo do Rio Meia Ponte.

---

## 6. Estrutura dos Principais Arquivos

- **db/models.py**: Define as classes das entidades e seus relacionamentos, incluindo tipos geoespaciais (POINT, LINESTRING).
- **db/crud.py**: Funções para criar, consultar, atualizar e deletar registros de cada entidade.
- **db/database_session.py**: Configura a conexão com o banco usando variáveis de ambiente e fornece o gerenciador de sessão.
- **db/init_db.py**: Cria todas as tabelas no banco de dados.
- **db/populate_db.py**: Popula o banco com dados iniciais de exemplo.

---

## 7. Dicas e Resolução de Problemas

- **Erro "type geometry does not exist"**: Certifique-se de que a extensão PostGIS está habilitada no banco.
- **Permissão para criar extensão**: Apenas o superusuário do PostgreSQL pode instalar extensões. Use `sudo -u postgres`.
- **Variáveis de ambiente**: Sempre confira se o `.env` está correto e corresponde ao banco criado.
- **Dependências**: Se faltar algum pacote Python, instale com `pip install ...`.

---

## 8. Observações Finais

- O MER detalhado está disponível em `doc/db_entity_relationships.md`.
- O banco foi projetado para ser flexível e extensível, suportando múltiplos rios, trechos, estações, sensores e modelos.
- Para manipulação dos dados, utilize as funções do `crud.py` dentro de sessões obtidas via `get_db()`.
- Para uso geoespacial, utilize tipos e funções do PostGIS (consultas espaciais, etc).

---

**Dúvidas ou sugestões? Consulte o README.md do projeto ou entre em contato com o mantenedor.**
