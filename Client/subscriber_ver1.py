import paho.mqtt.client as mqtt
import os
import base64

topic = '<topic>'
broker_ip = "<broker ip>"
username = '<user name>'
password = '<password>'

port = '<broker port number>'
tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Downloads')
os.makedirs(tmp_dir, exist_ok = True)

file_data = None
file_name = None

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

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # UNIX 계열 (Linux, macOS 등)
        os.system('clear')

def main():
    clear_screen()
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(broker_ip, port, keepalive = 60)
    client.loop_forever()

if __name__ == "__main__":
    main()