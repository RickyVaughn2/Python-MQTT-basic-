import paho.mqtt.client as mqtt

# Callback function to handle incoming messages
def on_message(client, userdata, msg):
    print("Message received: ", str(msg.payload.decode("utf-8")))

# MQTT client setup
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)
client.subscribe("example/topic")
client.on_message = on_message

# Send message to broker
client.publish("example/topic", "Hello World!")

# Wait for incoming messages
client.loop_forever()
