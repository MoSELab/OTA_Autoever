import paho.mqtt.client as mqtt
import os

TOPIC = '<topic>' #Message 수신 주제를 정의하는 변수
BROKER_IP = "<broker ip>" #Message publish를 중개해주는 MQTT Broker의 주소
BROKER_PORT - "<broker port>" #연결하려는 MQTT Broker의 open port

def on_connect(client, userdata, flags, reasonCode):
    if reasonCode == 0:
        print("Connected successfully.")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {reasonCode}")

def on_disconnect(client, userdata, flags, rc = 0):
    print(str(rc) + '/')

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode('utf-8')        

        print('Receive a message: ', payload)

    except Exception as e:
        print(f"Error: {e}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(broker_ip, port, keepalive = 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
