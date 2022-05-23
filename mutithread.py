import base64
import json
import pickle
import sys
import threading
import os
import time
import paho.mqtt.client as mqtt
#from function.tcos.Constant import MQTT_PORT,MQTT_IP,MQTT_LIVE
#from function.tcos.Util import pack
MQTT_PORT=1883
MQTT_IP="10.214.131.155"
MQTT_LIVE=60
def pack():
    return base64.b64decode(pickle.dumps(v))
def add_subscribe(client,topic,method):
    client.subscribe(topic)
    client.on_message = method
    client.connect(MQTT_IP, MQTT_PORT, MQTT_LIVE)
    client.loop_forever()

class Tcos_Msg_Queue:
    def __init__(self):
        self.client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.client = mqtt.Client(self.client_id, transport='tcp')
        self.client.connect(MQTT_IP, MQTT_PORT, MQTT_LIVE)  # 此处端口默认为1883，通信端口期keepalive默认60
        self.client.loop_start()
        self.cur_sub={}

    def publish(self,Topic,Data):
        tstr=str(time.time())
        data={"timestamp":tstr,"data":pack(Data)}
        self.client.publish(Topic,json.dumps(data))

    def get_a_client(self):
        client_id=str(time.time_ns())
        return mqtt.Client(client_id, transport='tcp')

    def subscribe(self,topic,method):
        if topic in self.cur_sub.keys():
            self.cur_sub[topic].loop_stop()
        client=self.get_a_client()
        self.cur_sub[topic]=client
        th=threading.Thread(target=add_subscribe,args=(client,topic,method,))
        th.start()
        time.sleep(2)
        return th
        #mq.stop_subscribt("test")
    def stop_subscribt(self,topic):
        if topic in self.cur_sub.keys():
            self.cur_sub[topic].loop_stop()
            del self.cur_sub[topic]
            exit(0)


def on_message(client, userdata, msg):
    """
    接收客户端发送的消息
    :param client: 连接信息
    :param userdata:
    :param msg: 客户端返回的消息
    :return:
    """
    print("Start server!")
    payload = json.loads(msg.payload.decode('utf-8'))
    print(payload)

mq=Tcos_Msg_Queue()
mq.subscribe("test",on_message)
time.sleep(2)
mq.stop_subscribt("test")
print(1)
