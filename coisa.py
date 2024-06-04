from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import logging
import time
import getopt
import datetime
import random
import json

# Read in command-line parameters
useWebsocket = False
host = ""
rootCAPath = ""
certificatePath = ""
privateKeyPath = ""
try:
    opts, args = getopt.getopt(sys.argv[1:], "hwe:k:c:r:", ["help", "endpoint=", "key=","cert=","rootCA=", "websocket"])
    if len(opts) == 0:
        raise getopt.GetoptError("No input parameters!")
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(helpInfo)
            exit(0)
        if opt in ("-e", "--endpoint"):
            host = arg
        if opt in ("-r", "--rootCA"):
            rootCAPath = arg
        if opt in ("-c", "--cert"):
            certificatePath = arg
        if opt in ("-k", "--key"):
            privateKeyPath = arg
        if opt in ("-w", "--websocket"):
            useWebsocket = True
except getopt.GetoptError:
    print("Missing parameters")
    exit(1)

# Configure logging
logger = None
if sys.version_info[0] == 3:
    logger = logging.getLogger("core")  # Python 3
else:
    logger = logging.getLogger("AWSIoTPythonSDK.core")  # Python 2

logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None

myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub")
myAWSIoTMQTTClient.configureEndpoint(host, 8883)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

thing = "MeuPrimeiroDispositivo"
topic = "dispositivos/MeuPrimeiroDispositivo/reportar"

# Publish to the same topic in a loop forever
while True:
    print(thing)
    temp = random.randint(10, 35)
    data = { "thing": thing, 
        "thing-type": "thermometer",
        "temperature": temp
    }
    myAWSIoTMQTTClient.publish(topic, json.dumps(data), 1)
    print("O dispositivo {} reportou a temperatura {} pelo topico {}.".format(thing, temp, topic))
    time.sleep(10)
