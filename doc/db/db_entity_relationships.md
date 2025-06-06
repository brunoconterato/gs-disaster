# **Modelo de Dados para HydroGuard: Monitoramento e Alerta de Enchentes**

Este projeto visa estruturar um banco de dados relacional (PostgreSQL) para suportar o sistema **HydroGuard**. Ele armazenará dados de sensores (reais e simulados), informações geográficas de rios e estações, histórico de medições, metadados de modelos de Machine Learning, previsões de enchentes e registros de alertas emitidos.

---

# Diagrama Entidade-Relacionamento (DER)

![Diagrama Entidade-Relacionamento (DER)](./mer.png)

---

# Modelo Entidade-Relacionamento (MER) - Textual

## Entidades e Atributos

### `river`
Representa um rio ou corpo d'água principal monitorado pelo sistema.

- `id_river`: Identificador único do rio (PK, UUID ou SERIAL)
- `river_name`: Nome do rio (VARCHAR, NOT NULL)
- `description`: Descrição opcional do rio (TEXT, NULLABLE)

---

### `river_segment`
Define um trecho específico de um rio monitorado. Um rio pode ter múltiplos trechos monitorados, cada um com suas próprias características e estações.

- `id_segment`: Identificador único do trecho (PK, UUID ou SERIAL)
- `id_river`: Chave estrangeira para `river` (FK, NOT NULL)
- `segment_name`: Nome do trecho (ex: "Montante de Goiânia") (VARCHAR, NOT NULL)
- `location_description`: Descrição mais detalhada da localização do trecho (TEXT, NULLABLE)
- `geographic_coordinates`: Geometria geoespacial do trecho (Linestring para PostGIS) (GEOMETRY(LINESTRING, 4326), NULLABLE)
- `critical_threshold_level`: Nível de água (em metros) que define um limiar crítico de enchente para este trecho específico (NUMERIC, NULLABLE)

---

### `station_type`
Categoriza o tipo de estação de monitoramento (e.g., oficial da ANA, implantação IoT do HydroGuard).

- `id_station_type`: Identificador único do tipo de estação (PK, UUID ou SERIAL)
- `name`: Nome do tipo (ex: "ANA Hidroweb", "HydroGuard IoT", "CEMADEN") (VARCHAR, NOT NULL)
- `description`: Descrição detalhada do tipo de estação (TEXT, NULLABLE)

---

### `monitoring_station`
Representa uma estação física de monitoramento onde sensores estão instalados. Cada estação está associada a um `river_segment`.

- `id_station`: Identificador único da estação (PK, UUID ou SERIAL)
- `id_segment`: Chave estrangeira para `river_segment` (FK, NOT NULL)
- `id_station_type`: Chave estrangeira para `station_type` (FK, NOT NULL)
- `station_name`: Nome ou identificação da estação (VARCHAR, NOT NULL)
- `geographic_location`: Coordenadas geográficas da estação (Ponto para PostGIS) (GEOMETRY(POINT, 4326), NULLABLE)
- `installation_date`: Data de instalação ou ativação da estação (TIMESTAMP WITH TIME ZONE, NULLABLE)
- `status`: Status operacional da estação (e.g., 'Active', 'Inactive', 'Maintenance', 'Faulty') (VARCHAR, NOT NULL, DEFAULT 'Active')

---

### `sensor_type`
Descreve o tipo de grandeza física que um sensor mede (e.g., nível da água, precipitação).

- `id_sensor_type`: Identificador único do tipo de sensor (PK, UUID ou SERIAL)
- `name`: Nome da grandeza medida (ex: "Nível da Água", "Precipitação", "Vazão", "Umidade do Solo") (VARCHAR, NOT NULL)
- `unit_of_measure`: Unidade de medida (ex: "m", "mm", "m³/s", "%") (VARCHAR, NOT NULL)
- `description`: Descrição opcional do tipo de sensor (TEXT, NULLABLE)

---

### `sensor`
Representa um sensor individual instalado em uma `monitoring_station`. Uma estação pode ter vários sensores de diferentes tipos.

- `id_sensor`: Identificador único do sensor (PK, UUID ou SERIAL)
- `id_station`: Chave estrangeira para `monitoring_station` (FK, NOT NULL)
- `id_sensor_type`: Chave estrangeira para `sensor_type` (FK, NOT NULL)
- `sensor_identifier`: Identificação específica do sensor (ex: "Ultrasonic_Level_01", "Pluviometer_A") (VARCHAR, NOT NULL)
- `model`: Modelo ou tipo de hardware do sensor (VARCHAR, NULLABLE)
- `calibration_date`: Data da última calibração do sensor (DATE, NULLABLE)
- `status`: Status operacional do sensor (e.g., 'Operational', 'Faulty', 'Disconnected') (VARCHAR, NOT NULL, DEFAULT 'Operational')

---

### `sensor_measurement`
Armazena as medições brutas coletadas pelos sensores.

- `id_measurement`: Identificador único da medição (PK, UUID ou SERIAL)
- `id_sensor`: Chave estrangeira para `sensor` (FK, NOT NULL)
- `measurement_value`: O valor numérico da medição (NUMERIC, NOT NULL)
- `timestamp`: Data e hora exata da coleta da medição (TIMESTAMP WITH TIME ZONE, NOT NULL)
- `data_source`: Origem dos dados (e.g., "ANA Hidroweb", "HydroGuard ESP32", "INMET") (VARCHAR, NOT NULL)
- `quality_flag`: Indicador de qualidade dos dados (e.g., 'Good', 'Doubtful', 'Missing Data') (VARCHAR, NULLABLE)

---

### `ml_model`
Contém metadados sobre os modelos de Machine Learning treinados e usados para previsão de enchentes.

- `id_model`: Identificador único do modelo ML (PK, UUID ou SERIAL)
- `model_name`: Nome do modelo (ex: "Flood_Predictor_v1.0") (VARCHAR, NOT NULL)
- `model_type`: Tipo de algoritmo do modelo (ex: "Random Forest Regressor", "LSTM Neural Network") (VARCHAR, NOT NULL)
- `training_date`: Data e hora em que o modelo foi treinado (TIMESTAMP WITH TIME ZONE, NOT NULL)
- `performance_metrics`: Métricas de avaliação do modelo (ex: RMSE, R2, F1-score), armazenadas como JSON (JSONB, NULLABLE)
- `model_path`: Caminho para o arquivo serializado do modelo (VARCHAR, NULLABLE)
- `input_features_description`: Descrição das features de entrada esperadas pelo modelo (JSONB, NULLABLE)
- `output_target_description`: Descrição do que o modelo prevê (JSONB, NULLABLE)
- `is_active`: Flag para indicar se o modelo está ativo para uso em produção (BOOLEAN, NOT NULL, DEFAULT TRUE)

---

### `flood_prediction`
Registra as previsões de nível do rio e risco de enchente geradas pelos modelos de Machine Learning.

- `id_prediction`: Identificador único da previsão (PK, UUID ou SERIAL)
- `id_model`: Chave estrangeira para `ml_model` (FK, NOT NULL)
- `id_station`: Chave estrangeira para `monitoring_station`. A previsão é feita para esta estação (FK, NOT NULL)
- `prediction_timestamp`: Data e hora em que a previsão foi gerada (TIMESTAMP WITH TIME ZONE, NOT NULL)
- `predicted_level`: Nível do rio previsto (em metros) (NUMERIC, NULLABLE)
- `predicted_risk_level`: Classificação do nível de risco (e.g., 'Baixo', 'Médio', 'Alto', 'Enchente Iminente') (VARCHAR, NULLABLE)
- `forecast_horizon_minutes`: Horizonte de tempo da previsão em minutos (e.g., 60, 120) (INTEGER, NOT NULL)
- `prediction_confidence`: Métrica de confiança da previsão (e.g., probabilidade, desvio padrão) (NUMERIC, NULLABLE)

---

### `alert`
Registra todos os alertas emitidos pelo sistema HydroGuard em resposta a uma `flood_prediction`.

- `id_alert`: Identificador único do alerta (PK, UUID ou SERIAL)
- `id_prediction`: Chave estrangeira para `flood_prediction`. O alerta foi gerado por esta previsão (FK, NOT NULL)
- `alert_timestamp`: Data e hora em que o alerta foi emitido (TIMESTAMP WITH TIME ZONE, NOT NULL)
- `alert_type`: Tipo de alerta (e.g., 'Visual LED', 'Console Message', 'SMS', 'Email') (VARCHAR, NOT NULL)
- `message`: Conteúdo da mensagem do alerta (TEXT, NOT NULL)
- `severity`: Gravidade do alerta (e.g., 'Informativo', 'Aviso', 'Crítico') (VARCHAR, NOT NULL)
- `status`: Status de entrega/recebimento do alerta (e.g., 'Sent', 'Failed', 'Acknowledged', 'Resolved') (VARCHAR, NOT NULL)

---

## Explicação das Cardinalidades

As cardinalidades indicam o número mínimo e máximo de ocorrências que uma entidade pode ter em relação a outra.

- Uma `river` pode ter **vários** `river_segment`s, e cada `river_segment` **pertence a um único** `river`.
- Um `river_segment` pode ter **várias** `monitoring_station`s, e cada `monitoring_station` **pertence a um único** `river_segment`.
- Um `station_type` pode categorizar **várias** `monitoring_station`s, e cada `monitoring_station` **possui um único** `station_type`.
- Uma `monitoring_station` pode ter **vários** `sensor`s, e cada `sensor` **pertence a uma única** `monitoring_station`.
- Um `sensor_type` pode descrever **vários** `sensor`s, e cada `sensor` **possui um único** `sensor_type`.
- Um `sensor` realiza **várias** `sensor_measurement`s ao longo do tempo, e cada `sensor_measurement` **é feita por um único** `sensor`.
- Um `ml_model` pode gerar **várias** `flood_prediction`s, e cada `flood_prediction` **é feita por um único** `ml_model`.
- Uma `monitoring_station` pode ter **várias** `flood_prediction`s feitas para ela, e cada `flood_prediction` **é específica para uma única** `monitoring_station`.
- Uma `flood_prediction` pode disparar **vários** `alert`s (e.g., um para o console, outro para SMS), e cada `alert` **é gerado por uma única** `flood_prediction`.

---

## Tabela de Cardinalidade Entre Entidades

| Entidade Fonte        | Entidade Alvo             | Cardinalidade Mínima (Fonte para Alvo) | Cardinalidade Máxima (Fonte para Alvo) |
|-----------------------|---------------------------|----------------------------------------|----------------------------------------|
| `river`               | `river_segment`           | 0                                      | N                                      |
| `river_segment`       | `monitoring_station`      | 0                                      | N                                      |
| `station_type`        | `monitoring_station`      | 0                                      | N                                      |
| `monitoring_station`  | `sensor`                  | 0                                      | N                                      |
| `sensor_type`         | `sensor`                  | 0                                      | N                                      |
| `sensor`              | `sensor_measurement`      | 0                                      | N                                      |
| `ml_model`            | `flood_prediction`        | 0                                      | N                                      |
| `monitoring_station`  | `flood_prediction`        | 0                                      | N                                      |
| `flood_prediction`    | `alert`                   | 0                                      | N                                      |
| `river_segment`       | `river`                   | 1                                      | 1                                      |
| `monitoring_station`  | `river_segment`           | 1                                      | 1                                      |
| `monitoring_station`  | `station_type`            | 1                                      | 1                                      |
| `sensor`              | `monitoring_station`      | 1                                      | 1                                      |
| `sensor`              | `sensor_type`             | 1                                      | 1                                      |
| `sensor_measurement`  | `sensor`                  | 1                                      | 1                                      |
| `flood_prediction`    | `ml_model`                | 1                                      | 1                                      |
| `flood_prediction`    | `monitoring_station`      | 1                                      | 1                                      |
| `alert`               | `flood_prediction`        | 1                                      | 1                                      |
