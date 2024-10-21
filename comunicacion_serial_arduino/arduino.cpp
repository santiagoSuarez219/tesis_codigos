void setup() {
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        String message = "";
        // Leer el mensaje completo
        while (Serial.available()) {
            char c = Serial.read();
            message += c;
            delay(10);  // Pequeña espera para asegurarse de leer el mensaje completo
        }
        // Imprimir el mensaje recibido
        Serial.print("Mensaje recibido: ");
        Serial.println(message);

        // Enviar confirmación de recibido
        Serial.println("Recibido");
    }
}
