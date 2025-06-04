# Guia de Uso do Banco de Dados HydroGuard

Este documento orienta sobre a configuração, inicialização e uso do banco de dados do projeto HydroGuard, complementando o MER já existente. Aqui você encontra instruções práticas para instalar dependências, configurar variáveis de ambiente, preparar o banco de dados PostgreSQL com PostGIS, rodar scripts de inicialização e popular a base com dados de exemplo.

---

## 1. Visão Geral do Banco de Dados

O banco de dados do HydroGuard foi projetado para armazenar informações de rios, trechos, estações de monitoramento, sensores, medições, modelos de machine learning, previsões de enchentes e alertas. Ele utiliza PostgreSQL com a extensão PostGIS para suportar dados geoespaciais (geometria de pontos e linhas).

- **Tecnologia:** PostgreSQL + PostGIS
- **ORM:** SQLAlchemy + GeoAlchemy2
- **Scripts principais:**
  - `init_db.py`: Criação das tabelas
  - `populate_db.py`: População inicial de dados, leitura de arquivos CSV de medições hidrológicas e criação de view/tabela de medições diárias resampleadas
  - `crud.py`: Funções de manipulação (Create, Read, Update, Delete) para todas as entidades do banco
  - `models.py`: Definição das entidades e relacionamentos, incluindo tipos geoespaciais e entidades auxiliares (ex: métricas de modelos de ML)
  - `database_session.py`: Configuração da conexão e sessão com o banco, via variáveis de ambiente

- **Entidades principais:** River, RiverSegment, StationType, MonitoringStation, SensorType, Sensor, SensorMeasurement, MLModel, MLModelMetric, FloodPrediction, Alert, ResampledMeasurementsDaily.

---

## 2. Instalação de Dependências

### a) Python

Certifique-se de ter o Python 3.8+ instalado.

### b) Instale os requirements do projeto

As dependências Python estão listadas no arquivo `requirements.txt` do projeto. Para instalar, execute:

```bash
pip install -r requirements.txt
```

> **Obs.:** As bibliotecas incluem, além das básicas para ORM e PostGIS, também `tqdm` e `pandas` (usadas para importação de dados e barra de progresso em scripts de população de dados).

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

### b) Habilite a extensão PostGIS (necessário ser superusuário)

```bash
sudo -u postgres psql -d <nome_do_banco>
# No prompt do psql:
CREATE EXTENSION IF NOT EXISTS postgis;
```

> **Atenção:** A extensão PostGIS deve estar habilitada **antes** da criação das tabelas, pois há campos do tipo geoespacial (POINT, LINESTRING).

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

Esse script insere um rio, um trecho, tipos de estação e sensor, três estações de monitoramento e nove sensores, além de importar dados de medições hidrológicas a partir de arquivos CSV localizados em `data/ANA HIDROWEB/RIO MEIA PONTE/`.

- O script também pode criar uma tabela/view chamada `resampled_measurements_daily` para análises agregadas.
- O mapeamento de sensores e estações é feito por código fixo no script, então para adicionar novos sensores/estações, o script deve ser adaptado.
- O script pode ser executado múltiplas vezes, mas pode gerar duplicidade se não houver controle de existência prévia dos dados.

---

## 6. Estrutura dos Principais Arquivos

- **db/models.py**: Define as classes das entidades e seus relacionamentos, incluindo tipos geoespaciais (POINT, LINESTRING) e entidades auxiliares como métricas de modelos de ML e view de medições diárias.
- **db/crud.py**: Funções para criar, consultar, atualizar e deletar registros de cada entidade. Algumas funções ainda estão como esqueleto e podem precisar ser implementadas para operações completas em todas as entidades.
- **db/database_session.py**: Configura a conexão com o banco usando variáveis de ambiente e fornece o gerenciador de sessão via context manager `get_db()`.
- **db/init_db.py**: Cria todas as tabelas no banco de dados.
- **db/populate_db.py**: Popula o banco com dados iniciais de exemplo, lê arquivos CSV de medições e pode criar a view/tabela de medições diárias resampleadas.

---

## 7. Dicas e Resolução de Problemas

- **Erro "type geometry does not exist"**: Certifique-se de que a extensão PostGIS está habilitada no banco **antes** de criar as tabelas.
- **Permissão para criar extensão**: Apenas o superusuário do PostgreSQL pode instalar extensões. Use `sudo -u postgres`.
- **Variáveis de ambiente**: Sempre confira se o `.env` está correto e corresponde ao banco criado.
- **Dependências**: Se faltar algum pacote Python, instale com `pip install -r requirements.txt`.
- **Arquivos de dados**: Certifique-se de que os arquivos CSV de medições estejam no caminho `data/ANA HIDROWEB/RIO MEIA PONTE/` conforme esperado pelo script `populate_db.py`.
- **Funções CRUD**: Algumas funções em `crud.py` ainda estão como esqueleto e podem precisar ser implementadas para operações completas em todas as entidades.
- **View de medições diárias**: O script `populate_db.py` pode criar uma tabela/view chamada `resampled_measurements_daily` para análises agregadas.

> ⚠️ Algumas funções de manipulação de dados (CRUD) ainda estão em desenvolvimento e podem não estar totalmente implementadas para todas as entidades. Consulte o arquivo `crud.py` para detalhes e, se necessário, implemente as funções faltantes conforme o padrão das já existentes.

---

## 8. Observações Finais

- O MER detalhado está disponível em `doc/db_entity_relationships.md`.
- O banco foi projetado para ser flexível e extensível, suportando múltiplos rios, trechos, estações, sensores e modelos.
- Para manipulação dos dados, utilize as funções do `crud.py` dentro de sessões obtidas via `get_db()`.
- Para uso geoespacial, utilize tipos e funções do PostGIS (consultas espaciais, etc).

---

**Dúvidas ou sugestões? Consulte o README.md do projeto ou entre em contato com o mantenedor.**
