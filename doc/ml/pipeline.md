# Pipeline de Processamento de Dados e Machine Learning

Este documento descreve o pipeline de processamento de dados e machine learning do projeto HydroGuard, detalhando as principais etapas, funções e boas práticas para uso e manutenção.

---

## 1. Visão Geral do Pipeline

O pipeline de machine learning é composto por etapas de extração, limpeza, transformação, engenharia de atributos, preparação de dados para séries temporais e uso de modelos preditivos. Todo o fluxo é implementado em Python, com integração ao banco de dados PostgreSQL/PostGIS via SQLAlchemy.

---

## 2. Processamento de Dados

O processamento de dados é realizado principalmente pelo módulo `ml/data_process.py`. As principais etapas são:

### 2.1. Extração de Dados
- **Função:** `load_data_from_db`
- **Descrição:** Carrega dados do banco de dados, podendo filtrar por intervalo de datas.
- **Ajuste de datas:** A função `adjust_date_range` amplia o intervalo para garantir contexto suficiente para agregações.

### 2.2. Formatação e Limpeza
- **Função:** `format_db_data_columns`
- **Descrição:** Renomeia colunas para um padrão consistente (ex: `rain_upstream`, `level_downstream`).
- **Função:** `fill`
- **Descrição:** Preenche valores ausentes. Chuvas ausentes são zeradas; níveis e vazões usam preenchimento para trás (bfill).

### 2.3. Reamostragem e Agregação
- **Função:** `resample_data`
- **Descrição:** Reamostra os dados para frequência diária, calculando média, máximo, mínimo, quartis (q25, q75).

### 2.4. Engenharia de Atributos
- **Função:** `feature_engineering`
- **Descrição:** Adiciona colunas de chuva acumulada (2 e 3 dias), codificação cíclica de datas (seno/cosseno) e ano.

---

## 3. Preparação para Machine Learning

O módulo `ml/ml_utils.py` centraliza a preparação dos dados para modelos de séries temporais.

### 3.1. Normalização
- **Função:** `get_scaler` e uso de `StandardScaler` (scikit-learn).
- **Descrição:** Normaliza os dados (exceto colunas cíclicas) para entrada nos modelos.

### 3.2. Criação de Datasets
- **Classe:** `TimeSeriesDataset`
- **Descrição:** Organiza os dados em janelas deslizantes para previsão de séries temporais.

### 3.3. Função de Preparação
- **Função:** `prepare_timeseries_data`
- **Descrição:** Remove colunas de vazão (opcional), normaliza e retorna dataset pronto para uso em modelos.

---

## 4. Modelos de Machine Learning

Os modelos estão definidos em `ml/models.py` e são carregados/utilizados via `ml_utils.py`.

- **Modelos suportados:** MLP, LSTM, GRU (PyTorch)
- **Função de carregamento:** `load_model`
- **Função de predição:** `predict`
- **Denormalização:** Função `denormalize_column` para converter previsões ao valor original.

---

## 5. Boas Práticas e Observações

- **Integração com banco:** Sempre utilize as funções do pipeline para garantir consistência.
- **Datas:** Forneça datas no formato `YYYY-MM-DD`.
- **Escalonamento:** O scaler deve ser salvo durante o treinamento e reutilizado na inferência.
- **Engenharia de atributos:** Novos atributos devem ser adicionados na função `feature_engineering`.
- **Debug:** Prints de debug estão presentes para facilitar rastreamento de problemas.

---

## 6. Referências de Código

- `ml/data_process.py`: Funções de processamento e engenharia de dados.
- `ml/ml_utils.py`: Utilitários para datasets, normalização, carregamento e predição de modelos.
- `ml/models.py`: Definição dos modelos MLP, LSTM e GRU.

---

## 7. Notebooks: Onde a Magia do ML Acontece

Os notebooks da pasta `ml/` são o coração do pipeline de machine learning do HydroGuard. Eles não são apenas exemplos práticos, mas sim o ambiente onde todo o processamento, treinamento, avaliação e análise dos modelos realmente acontece. A execução dos notebooks deve seguir a ordem numérica, pois cada etapa depende da anterior:

### 7.1. 1. Process Data.ipynb

- **Função:** Prepara e processa todos os dados necessários para as etapas seguintes.
- **O que faz:**
  - Extrai dados do banco, realiza limpeza, preenchimento de valores nulos e reamostragem.
  - Aplica engenharia de atributos, como agregações e codificações temporais.
  - Salva o DataFrame processado para uso nos próximos notebooks.
- **Importância:** É obrigatório rodar este notebook antes dos demais, pois ele gera os dados prontos para análise e modelagem.

### 7.2. 2. EDA.ipynb (opcional, mas deve ser executado após o 1.)

- **Função:** Realiza a Análise Exploratória dos Dados (EDA) sobre o dataset já processado.
- **O que faz:**
  - Gera estatísticas descritivas, gráficos de distribuição, boxplots, heatmaps de correlação e análise de outliers.
  - Permite entender padrões, sazonalidades, tendências e possíveis problemas nos dados.
- **Importância:** Opcional, mas recomendada para garantir que os dados estejam adequados antes do treinamento dos modelos.

### 7.3. 3. ML.ipynb

- **Função:** Executa todo o pipeline de machine learning: do pré-processamento ao treinamento, otimização e avaliação dos modelos.
- **O que faz:**
  - Carrega os dados preparados pelo notebook 1.
  - Realiza pré-processamento adicional (remoção de colunas, normalização, chunking temporal).
  - Define, treina e avalia modelos MLP, LSTM e GRU usando PyTorch Lightning.
  - Utiliza Optuna para otimização automática de hiperparâmetros.
  - Gera visualizações comparativas e métricas quantitativas dos resultados.
- **Importância:** É aqui que os modelos são realmente treinados e avaliados. Os artefatos gerados (modelos, hiperparâmetros, scaler) são salvos para uso em inferência.

> **Atenção:** Execute sempre os notebooks na ordem 1 → 2 (opcional) → 3. O notebook 1 é pré-requisito para os demais, pois prepara os dados. O notebook 3 depende dos dados processados pelo 1. e, opcionalmente, das análises do 2.

---

## 8. Inferência: Utilização dos Modelos Treinados

As funções presentes nos arquivos Python (`ml/data_process.py`, `ml/ml_utils.py`) são dedicadas a utilizar os modelos treinados nos notebooks para inferência em produção ou em outros experimentos. Elas permitem:
- Carregar modelos e hiperparâmetros salvos.
- Normalizar e preparar novos dados para predição.
- Realizar previsões (inferência) com os modelos treinados.
- Denormalizar os resultados para o formato original.

---

**Para detalhes completos, consulte e execute os notebooks em `ml/` na ordem recomendada. Os scripts Python dão suporte à inferência e automação do pipeline.**
