# **Listener Saver** - Pipeline de Ingestão de Dados via MQTT

## Visão Geral

Este pipeline realiza a ingestão de dados em tempo real a partir de um broker MQTT e insere as mensagens processadas em um banco de dados relacional.

## Arquitetura

- **Fonte de dados:** Broker MQTT
- **Transporte:** Cliente MQTT 
- **Destino:** Banco de dados relacional (PostgreSQL)

## Fluxo de Dados

1. Assinatura dos tópicos de interesse no broker MQTT.
2. Recebimento contínuo das mensagens em formato JSON.
3. Parsing e validação dos campos recebidos.
4. Conversão do timestamp para formato datetime padronizado.
5. Inserção dos registros na tabela de destino no banco de dados.
6. Registro de erros e controle de reconexão automática.

## Exemplo de Payload

```json
{
  "station_id": "meiaponte_001",
  "timestamp": "11/06/2022 23:59:34",
  "river_level_cm": 96.934,
  "temperature": 60.1,
  "soil_moisture_pct": 24,
  "rain_mm": 753
}
```

## Transformações Realizadas

| Campo | Transformação Aplicada |
|-------|-------------------------|
| `station_id` | Validação de string |
| `timestamp` | Conversão de string para datetime (formato DD/MM/YYYY HH:mm:ss → UTC) |
| `river_level_cm` | Conversão para float |
| `temperature` | Conversão para float |
| `soil_moisture_pct` | Conversão para inteiro ou float |
| `rain_mm` | Conversão para inteiro ou float |

## Tratamento de Erros

- **Falhas de Conexão:** Reconexão automática com o broker MQTT.
- **Payload Inválido:** Registro em log de mensagens inválidas ou não processáveis.
- **Erros de Banco de Dados:** Registro em log de falhas de inserção; possibilidade de implementação de política de retry.

## Possíveis Melhorias Futuras

- Controle de idempotência para evitar duplicidades.
- Integração com sistemas de monitoramento e alertas (ex.: Prometheus, Grafana).

## Observação Final

Ainda que o pipeline atualmente processe uma única fonte de dados e uma única tabela, sua arquitetura já segue o conceito de **ingestão de dados** por tratar-se de um fluxo contínuo, automatizado e controlado.
