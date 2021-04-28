#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// WiFi informathon and UUID
#define UUID "eb956ae7-a406-11eb-95ee-a4c3f077fe6a"
#define STASSID "KD"
#define STAPASS "19980326"

int relayPin = 0; // GPIO0 for Relay
int ledPin   = 2; // GPIO2 of ESP8266-01S
int httpCode;

WiFiClient client;
HTTPClient http;

void setup() 
{
    // Set bit rate
    Serial.begin(115200);  

    // WiFi Setting
    WiFi.mode(WIFI_STA);    
    WiFi.setAutoReconnect(true);
    WiFi.begin(STASSID, STAPASS);
    while(WiFi.status() != WL_CONNECTED)
    {
      delay(500);  
    }

    // GPIO Init
    pinMode(ledPin, OUTPUT);
    pinMode(relayPin, OUTPUT);
    digitalWrite(ledPin, HIGH);  // LOW is active
    digitalWrite(relayPin, HIGH);
    
    http.begin(client, "http://192.168.3.113:8000/" UUID "/controlESP");
}


void loop() 
{
    String state = "False";
    
    // Check WiFi State
    if (WiFi.status() != WL_CONNECTED) // If WiFi dissconnected
    {
        digitalWrite(ledPin, HIGH); // Turn off LED of ESP
        state = "False";            // Turn off relay
        
        WiFi.disconnect();
        delay(10);
        WiFi.begin(STASSID, STAPASS);
        while (WiFi.status() != WL_CONNECTED) { delay(500); }
    }
    else if (WiFi.status() == WL_CONNECTED)
    {
        digitalWrite(ledPin, LOW);        
        httpCode = http.GET();                  
        if (httpCode > 0) 
        {         
            Serial.printf("[HTTP] GET... code: %d\n", httpCode);         
            if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) 
            {
                state = http.getString();        
                Serial.print("STATE: ");
                Serial.println(state);
                if(state == "True")
                {
                    // Serial.println("Command: OPEN");
                    digitalWrite(relayPin, LOW);
                }
                else if (state == "False")
                {
                    // Serial.println("Command: CLOSE");
                    digitalWrite(relayPin, HIGH);
                }                 
            }
        } 
        else { Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str()); }
        http.end();        
    }
    delay(10000); // 1S = 1000
}
