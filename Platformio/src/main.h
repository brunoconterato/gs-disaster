#ifndef MAIN_H
#define MAIN_H

#include <Arduino.h>
#include <ArduinoJson.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <RTClib.h>

// WiFi credentials
extern const char* ssid;
extern const char* password;

// MQTT broker configuration
extern const char* mqtt_server;
extern const int mqtt_port;
extern const char* mqtt_user;
extern const char* mqtt_password;

// Tópicos MQTT
extern const char* send_topics[];
extern const char* recive_topics[];

// Definições de pinos do sensor HC-SR04 (ou similar)
#define HC_OUT 18  // Trigger
#define HC_IN  17  // Echo

// I2C pins for the LCD
#define SDA_PIN 21
#define SCL_PIN 22

// Definições de pinos e modelos
#define RAIN_ANALOG 34
#define RAIN_DIGITAL 16
#define DHT_COM_PIN 4   // Defina o pino real de dados do DHT aqui
#define DHT_MODEL DHT22

// Instâncias globais (serão definidas em main.cpp)
extern DHT dht22;
extern LiquidCrystal_I2C lcd;
extern RTC_DS1307 rtc;

// Protótipos de função
void mqttCallback(char* topic, byte* payload, unsigned int length);
float get_rain();
void read_sensors(); 
void initializeLCD();
void EnviaValores(float rain, float river_level_cm, float temperature, float umidade, const char* topic); // <-- ponto-e-vírgula
void connectToWiFi();
void connectMQTT();
void logToSerial(float temperature, float umidade, float rain, float distance);
void displayReadingsOnLCD(float temperature, float humidity, float rain, float distance);
float get_distance();

#endif // MAIN_H