# **Collector Sender**

Este documento detalha o funcionamento interno do firmware embarcado no ESP32, responsável por coletar os dados dos sensores, processá-los e transmiti-los via MQTT no formato JSON.

## Componentes de Hardware Simulados

- ESP32: Microcontrolador central do sistema.
- Sensor Ultrassônico HC-SR04: Mede a distância até a superfície da água, estimando o nível do rio.
- Sensor de Umidade DHT22: Mede umidade relativa do ar e temperatura (substituto do sensor de umidade do solo para simulação em Wokwi).
- Pluviômetro Simulado (Sensor Analógico): Mede a quantidade de chuva (analogicamente), simulando um pluviômetro simples.
- RTC DS1307: Módulo de relógio em tempo real, usado para registrar a marcação temporal dos dados.
- Display LCD I2C: Exibe localmente leituras em tempo real.

## Arquitetura do Firmware

- Inicialização (setup)
- Inicializa LCD, RTC, sensores conectados.
- Conecta à rede Wi-Fi.
- Configura as credenciais seguras do MQTT.
- Se conecta ao broker MQTT (em modo seguro; para testes, a verificação TLS é desativada).
- Faz subscribe no tópico de recebimento para eventual controle remoto.

## Fluxo Resumido de Dados

```mermaid
[Sensor] ----
            \
                >   ESP32    ---->   [Mensagem JSON] ----> [Broker MQTT] ----> [Consumidor Python/Banco/Alerta]
[RTC | LCD] --
```

## Loop Principal (loop)

- Mantém a conexão MQTT ativa (`client.loop()`).
- Periodicamente (a cada N segundos definidos em `readInterval`), realiza:
- Leitura dos sensores.
- Exibição das leituras no LCD.
- Publicação dos dados via MQTT como um objeto JSON.

## Leitura dos Sensores

- `get_rain()`: Faz leitura analógica do sensor de chuva.
- `get_distance()`: Mede distância via ultrassônico para estimar nível do rio em cm.
- `dht22.readHumidity()`: Lê umidade do ar.
- `dht22.readTemperature()`: Lê temperatura do ar.

## Formato do JSON Enviado

```json
{
    "station_id": "meiaponte_001",
    "timestamp": "13:42",
    "river_level_cm": 85.5,
    "temperature": 26.4,
    "soil_moisture_pct": 48.7,
    "rain_mm": 34.1
}
```
