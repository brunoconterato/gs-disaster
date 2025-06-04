#include "main.h"

// Instâncias globais
RTC_DS1307 rtc;
DHT dht22(DHT_COM_PIN, DHT_MODEL);
LiquidCrystal_I2C lcd(0x27, 20, 4);

// Credenciais de Wi-Fi (extern no .h)
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// Configurações MQTT (extern no .h)
const char* mqtt_server = "759d2f782c6f48d68eafab33492641f8.s1.eu.hivemq.cloud";
const int mqtt_port = 8883;
const char* mqtt_user = "sla";
const char* mqtt_password = "sla";

// Tópicos (extern no .h)
const char* send_topics[] = { "esp32/s0" };
const char* recive_topics[] = { "py/s0" };

// Cliente MQTT com TLS
WiFiClientSecure secureClient;
PubSubClient client(secureClient);

// Controle de intervalos
unsigned long lastReadTime = 0;
// Ajuste conforme necessário (ex: 60000 para 1 min)
const unsigned long readInterval = 6000; 

void setup() {
  Serial.begin(115200);

  // Inicializa LCD
  initializeLCD();

  // Conecta ao Wi-Fi
  connectToWiFi();

  // Configura pinos
  pinMode(RAIN_ANALOG, INPUT);
  pinMode(RAIN_DIGITAL, INPUT);
  pinMode(HC_IN,  INPUT);
  pinMode(HC_OUT, OUTPUT);
  analogReadResolution(10);

  // Configura MQTT
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(mqttCallback);
  connectMQTT();

  // Inicializa e valida RTC
  if (!rtc.begin()) {
    Serial.println("RTC não encontrado!");
  }
  if (!rtc.isrunning()) {
    Serial.println("RTC não está rodando, ajustando data/hora!");
    // rtc.adjust(DateTime(F(__DATE__), F(__TIME__))); 
    // Descomente se quiser ajustar o RTC com data/hora de compilação.
  }

  Serial.println("Setup completo!");
}

void loop() {
  // Mantém a conexão MQTT viva
  client.loop();

  unsigned long currentMillis = millis();
  if (currentMillis - lastReadTime >= readInterval) {
    lastReadTime = currentMillis;
    read_sensors();
  }
}

// Callback de mensagens recebidas via MQTT
void mqttCallback(char* topic, byte* payload, unsigned int length) {
  payload[length] = '\0';
  String message = String((char*)payload);
  Serial.printf("Recebida mensagem no tópico %s: %s\n", topic, message.c_str());
}

// Leitura de chuva
float get_rain() {
  float rain = analogRead(RAIN_ANALOG);
  return rain;
}

// Leitura do sensor ultrassônico
float get_distance() {
  // Dispara o pulso
  digitalWrite(HC_OUT, LOW);
  delayMicroseconds(2);
  digitalWrite(HC_OUT, HIGH);
  delayMicroseconds(10);
  digitalWrite(HC_OUT, LOW);

  // Mede o tempo do pulso de retorno no pino Echo
  long duration_us = pulseIn(HC_IN, HIGH);
  // Cálculo aproximado: velocidade do som ~340 m/s => ~29 microsegundos/cm
  // Aqui está sendo usado 0.017 (metade de 0.034) por algum fator de conversão
  float distance_cm = duration_us * 0.017;
  return distance_cm;
}

// Leitura geral dos sensores
void read_sensors() {
  float rain          = get_rain();
  float humidity      = dht22.readHumidity();
  float temperature   = dht22.readTemperature();
  float river_level   = get_distance();

  logToSerial(temperature, humidity, rain, river_level);
  displayReadingsOnLCD(temperature, humidity, rain, river_level);

  // Envia valores em formato JSON via MQTT
  EnviaValores(rain, river_level, temperature, humidity, send_topics[0]);
}

// Inicialização do LCD
void initializeLCD() {
  Wire.begin(SDA_PIN, SCL_PIN); 
  lcd.init();                   
  lcd.backlight();              
  lcd.setCursor(0, 0);
  lcd.print("Inicializando...");
  delay(2000);
  lcd.clear();
}

// Envio de valores em JSON via MQTT
void EnviaValores(float rain, float river_level_cm, float temperature, float umidade, const char* topic) {
  DynamicJsonDocument doc(256);

  // Obtém objeto DateTime do RTC
  DateTime now = rtc.now();
  // Formata hora:minuto como string 
  String timeStr = String(now.hour()) + ":" + String(now.minute());

  // Monta o objeto JSON
  doc["station_id"]        = "meiaponte_001";
  doc["timestamp"]         = timeStr;  

  // Exemplo de mapeamento (ajuste conforme desejado):
  doc["river_level_cm"]    = river_level_cm;
  doc["temperature"]       = temperature; 
  doc["soil_moisture_pct"] = umidade;
  doc["rain_mm"]           = rain;

  // Serializa em buffer
  char jsonBuffer[256];
  serializeJson(doc, jsonBuffer);

  Serial.println("Enviando JSON:");
  Serial.println(jsonBuffer);

  // Publica via MQTT
  client.publish(topic, jsonBuffer);
}

// Conexão ao Wi-Fi
void connectToWiFi() {
  if (WiFi.status() == WL_CONNECTED) return;
  Serial.print("Conectando ao Wi-Fi: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi conectado!");
}

// Conexão ao broker MQTT
void connectMQTT() {
  while (!client.connected()) {
    Serial.print("Conectando ao broker MQTT...");
    secureClient.setInsecure(); // modo inseguro, para testes

    if (client.connect("ESP32Client", mqtt_user, mqtt_password)) {
      Serial.println("Conectado ao broker MQTT!");
      // Faz subscribe no(s) tópico(s) de recepção
      client.subscribe(recive_topics[0]);
      Serial.printf("Inscrito no tópico: %s\n", recive_topics[0]);
    } else {
      Serial.print("Falha na conexão, rc=");
      Serial.println(client.state());
      delay(5000);
    }
  }
}

// Log em Serial
void logToSerial(float temperature, float umidade, float rain, float distance) {
  Serial.println("----------------");
  Serial.print("Temp: ");
  Serial.println(temperature);
  Serial.print("Umid: ");
  Serial.println(umidade);
  Serial.print("Chuva: ");
  Serial.println(rain);
  Serial.print("river_level_cm: ");
  Serial.println(distance);
  Serial.println("----------------");
}

// Exibe leituras no LCD
void displayReadingsOnLCD(float temperature, float humidity, float rain, float distance) {
  // Exibe a distância do rio
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("River dist: ");
  lcd.print(distance, 1);
  lcd.print("cm");

  delay(1500);

  // Exibe temperatura e umidade
  lcd.clear(); 
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperature, 1); 
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("Umid: ");
  lcd.print(humidity, 1); 
  lcd.print("%");

  delay(1500);

  // Exibe estado de chuva
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Rain amount: ");
  lcd.print(analogRead(RAIN_ANALOG));
  delay(1000);
}