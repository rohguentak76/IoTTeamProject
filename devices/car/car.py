import time
import json
import sys

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

host = "azjctapxbp7sc-ats.iot.ap-northeast-2.amazonaws.com"

rootCAPath = "./RootCA.crt"
certificatePath = "./5bf4c37523-certificate.pem.crt"
privateKeyPath = "./5bf4c37523-private.pem.key"
port = 8883
clientId = "car_pi"
parent_topic = "car/parent"

myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myAWSIoTMQTTClient.connect()


def Callback_func(payload, responseStatus, token):
    print()
    print('UPDATE: $aws/things/' + Thing_Name + '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + responseStatus)
    print("token = " + token)


loopCount=0


while True:
    
    message = {}
    message['message'] = "car/parent"
    message['sequence'] = loopCount
    messageJson = json.dumps(message)

    message = myAWSIoTMQTTClient.publish(parent_topic,messageJson,1)
    print(message, loopCount)
    
    time.sleep(3)
    loopCount +=1




