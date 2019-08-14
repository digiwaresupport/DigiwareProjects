#include <TTP229.h>
int led = 13;

const int SCL_PIN = 2;  
const int SDO_PIN = 3;  

TTP229 ttp229(SCL_PIN, SDO_PIN); 

void setup()
{
	Serial.begin(115200);
	Serial.println("Tes Fungsi Keypad Kapasitif 16 Tombol:");
  Serial.print(".");
  delay(1000);
  Serial.print(" .");
  delay(1000);
  Serial.println(" .");
  delay(1000);
  Serial.println("Silahkan Tekan Tombol!");
  Serial.println(" ");
}

void loop()
{
	uint8_t key = ttp229.ReadKey16(); 

  if(key == 1)
  {
    Serial.println("Tombol 1 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 2)
  {
    Serial.println("Tombol 2 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }
if(key == 3)
  {
    Serial.println("Tombol 3 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }
  if(key == 4)
  {
    Serial.println("Tombol 4 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }
  
  if(key == 5)
  {
    Serial.println("Tombol 5 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 6)
  {
    Serial.println("Tombol 6 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 7)
  {
    Serial.println("Tombol 7 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 8)
  {
    Serial.println("Tombol 8 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 9)
  {
    Serial.println("Tombol 9 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 10)
  {
    Serial.println("Tombol 10 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 11)
  {
    Serial.println("Tombol 11 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 12)
  {
    Serial.println("Tombol 12 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 13)
  {
    Serial.println("Tombol 13 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 14)
  {
    Serial.println("Tombol 14 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 15)
  {
    Serial.println("Tombol 15 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }

  if(key == 16)
  {
    Serial.println("Tombol 16 ditekan");
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
  }
}


