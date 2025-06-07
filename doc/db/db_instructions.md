# Guia Prático do Banco de Dados HydroGuard

Este documento complementa o MER do projeto HydroGuard, detalhando o uso prático do banco de dados, scripts de inicialização e população, além de dicas para desenvolvedores. Para o modelo conceitual, consulte o arquivo `doc/db_entity_relationships.md`.

---

## 1. Visão Geral

O banco de dados HydroGuard utiliza **PostgreSQL** com a extensão **PostGIS** para dados geoespaciais. O acesso e manipulação dos dados é feito via **SQLAlchemy ORM** e **GeoAlchemy2**. O projeto inclui scripts para criação das tabelas, população inicial e funções CRUD.

- **Tecnologia:** PostgreSQL + PostGIS
- **ORM:** SQLAlchemy + GeoAlchemy2
- **Scripts principais:**
  - `db/scripts/init_db.py`: Criação/recriação das tabelas e extensão PostGIS
  - `db/scripts/populate_db.py`: População inicial de dados, incluindo importação de medições de arquivos CSV
- **Bibliotecas:**
  - `db/crud.py`: Funções CRUD para todas as entidades
  - `db/models.py`: Definição das entidades e relacionamentos
  - `db/database_session.py`: Configuração de conexão, sessão e pool de conexões

---

## 2. Instalação de Dependências

### Banco de Dados

No Ubuntu/Debian, instale PostgreSQL e PostGIS:

```bash
sudo apt-get update
sudo apt-get install postgresql postgis postgresql-14-postgis-3
```

### Python

Instale as dependências do projeto (incluindo SQLAlchemy, GeoAlchemy2, psycopg2, dotenv, pandas, tqdm):

```bash
pip install -r requirements.txt
```

---

## 3. Estrutura dos Arquivos

- **db/models.py**: Define as classes ORM das entidades (rios, segmentos, estações, sensores, medições, modelos ML, previsões, alertas) e tipos geoespaciais (POINT, LINESTRING).
- **db/crud.py**: Funções CRUD para cada entidade, usando sessões SQLAlchemy.
- **db/database_session.py**: Configura a conexão com o banco via SQLAlchemy, carrega variáveis de ambiente do `.env` e implementa pool de conexões com psycopg2.
- **db/scripts/init_db.py**: 
  - Garante a extensão PostGIS.
  - Remove a view `resampled_measurements_daily` se existir.
  - Dropa e recria todas as tabelas do banco.
- **db/scripts/populate_db.py**:
  - Cria entidades em ordem lógica (rio, segmento, tipo de estação, tipos de sensores, estações, sensores).
  - Importa medições brutas de arquivos CSV usando pandas e insere em lote via psycopg2.
  - Utiliza tqdm para feedback visual durante a população.

---

## 4. Observações Importantes

- **Variáveis de ambiente:** O acesso ao banco depende de variáveis no `.env` (POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD).
- **Extensão PostGIS:** O script de inicialização garante a criação da extensão antes das tabelas.
- **View resampled_measurements_daily:** 
  - Não é criada pelo ORM.
  - Para consultas, reflita a view manualmente usando SQLAlchemy Core (veja comentário em `models.py`).
- **Importação de medições:** O script de população lê arquivos CSV de medições e faz o mapeamento para sensores via dicionário fixo.
- **Feedback visual:** O uso de tqdm nos scripts facilita o acompanhamento do progresso da população de dados.
- **Tipos geoespaciais:** Campos de localização usam POINT ou LINESTRING, suportados pelo PostGIS.

---

## 5. Dicas e Resolução de Problemas

- **Erro de conexão:** Verifique se o PostgreSQL está rodando e se as variáveis do `.env` estão corretas.
- **Dependências Python:** Instale sempre via `pip install -r requirements.txt`.
- **Problemas com tipos geoespaciais:** Certifique-se de que a extensão PostGIS está ativa no banco.
- **População de dados:** Os arquivos CSV de medições devem estar nos caminhos esperados pelo script de população.

---

**Dúvidas ou sugestões? Consulte o README.md do projeto ou entre em contato com os integrantes do grupo.**
