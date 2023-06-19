import paho.mqtt.client as mqtt

# MQTT broker adresi ve portu
broker_address = "broker_adresi"
broker_port = 1883

# MQTT istemci ad�
client_name = "mesajla�ma_istemci"

# MQTT istemcisiyle ba�lant� kuruldu�unda ger�ekle�tirilecek eylemler
def on_connect(client, userdata, flags, rc):
    print("Broker'a ba�land�: " + str(rc))
    # Mesajla�ma kanal�na abone ol
    client.subscribe("mesajlasma/kanal")

# Mesaj al�nd���nda ger�ekle�tirilecek eylemler
def on_message(client, userdata, msg):
    print("Mesaj al�nd�: " + msg.payload.decode())

# MQTT istemcisi olu�tur
client = mqtt.Client(client_name)

# Ba�lant� ve mesaj olaylar�n� tan�mla
client.on_connect = on_connect
client.on_message = on_message

# Broker'a ba�lan
client.connect(broker_address, broker_port)

# Mesaj g�ndermek i�in d�ng�y� ba�lat
client.loop_start()

# Kullan�c�dan mesajlar� al ve mesajla�ma kanal�na g�nder
while True:
    message = input("Mesaj�n�z� girin: ")
    client.publish("mesajlasma/kanal", message)

# D�ng�y� durdur
client.loop_stop()

