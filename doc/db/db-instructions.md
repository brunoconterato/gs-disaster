# Guia de Uso do Banco de Dados HydroGuard

Este documento orienta com informações extras e gerais sobre o banco de dados do projeto HydroGuard, complementando o MER já existente. Aqui você encontra instruções práticas para instalar dependências, preparar o banco de dados PostgreSQL com PostGIS e mais.

## 1. Visão Geral do Banco de Dados

O banco de dados do HydroGuard foi projetado para armazenar informações de rios, trechos, estações de monitoramento, sensores, medições, modelos de machine learning, previsões de enchentes e alertas. Ele utiliza PostgreSQL com a extensão PostGIS para suportar dados geoespaciais (geometria de pontos e linhas).

- **Tecnologia:** PostgreSQL + PostGIS
- **ORM:** SQLAlchemy + GeoAlchemy2
- **Scripts:**
  - `db/scripts/init_db.py`: Criação das tabelas
  - `db/scripts/populate_db.py`: População inicial de dados
- **Biblioteca:**
  - `db/crud.py`: Funções de manipulação (Create, Read, Update, Delete)
  - `db/models.py`: Definição das entidades e relacionamentos
  - `db/database_session.py`: Configuração da conexão e sessão

## 2. Instalação de Dependências

### Instale o PostgreSQL e o PostGIS

No Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install postgresql postgis postgresql-14-postgis-3
```

## 3. Estrutura dos Principais Arquivos

- **db/models.py**: Define as classes das entidades e seus relacionamentos, incluindo tipos geoespaciais (POINT, LINESTRING).
- **db/crud.py**: Funções para criar, consultar, atualizar e deletar registros de cada entidade.
- **db/database_session.py**: Configura a conexão com o banco usando variáveis de ambiente e fornece o gerenciador de sessão.
- **db/scripts/init_db.py**: Cria todas as tabelas no banco de dados.
- **db/scripts/populate_db.py**: Popula o banco com dados iniciais de exemplo.

## 4. Dicas e Resolução de Problemas

- **Variáveis de ambiente**: Sempre confira se o `.env` está correto e corresponde ao banco criado.
- **Dependências**: Se faltar algum pacote Python, instale com `pip install ...`.

## 5. Observações Finais

- O MER detalhado está disponível em `doc/db_entity_relationships.md`.
- O banco foi projetado para ser flexível e extensível, suportando múltiplos rios, trechos, estações, sensores e modelos.
- Para manipulação dos dados, utilize as funções do `crud.py` dentro de sessões obtidas via `get_db()`.
- Para uso geoespacial, utilize tipos e funções do PostGIS (consultas espaciais, etc).

---

**Dúvidas ou sugestões? Consulte o README.md do projeto ou entre em contato com os integrantes do grupo.**
