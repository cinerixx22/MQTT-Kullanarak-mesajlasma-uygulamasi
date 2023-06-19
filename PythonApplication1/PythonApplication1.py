import paho.mqtt.client as mqtt

# MQTT broker adresi ve portu
broker_address = "broker_adresi"
broker_port = 1883

# MQTT istemci adý
client_name = "mesajlaþma_istemci"

# MQTT istemcisiyle baðlantý kurulduðunda gerçekleþtirilecek eylemler
def on_connect(client, userdata, flags, rc):
    print("Broker'a baðlandý: " + str(rc))
    # Mesajlaþma kanalýna abone ol
    client.subscribe("mesajlasma/kanal")

# Mesaj alýndýðýnda gerçekleþtirilecek eylemler
def on_message(client, userdata, msg):
    print("Mesaj alýndý: " + msg.payload.decode())

# MQTT istemcisi oluþtur
client = mqtt.Client(client_name)

# Baðlantý ve mesaj olaylarýný tanýmla
client.on_connect = on_connect
client.on_message = on_message

# Broker'a baðlan
client.connect(broker_address, broker_port)

# Mesaj göndermek için döngüyü baþlat
client.loop_start()

# Kullanýcýdan mesajlarý al ve mesajlaþma kanalýna gönder
while True:
    message = input("Mesajýnýzý girin: ")
    client.publish("mesajlasma/kanal", message)

# Döngüyü durdur
client.loop_stop()

