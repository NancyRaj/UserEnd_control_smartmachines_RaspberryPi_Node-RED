
#Code to Subscribe topic with user defined call back function
import paho.mqtt.client as mq
import RPi.GPIO as gp
gp.setmode(gp.BOARD)
gp.setup(8,gp.OUT)
gp.setup(10,gp.OUT)
c=mq.Client()
c.connect('iot.eclipse.org',1883)
def onc(c,userdata,flag,rc):
    print('connected rc is',rc)
    c.subscribe('smartfactory0/m1')
    c.subscribe('smartfactory0/m2')
def on_m1(c,userdata,msg):
    m=msg.payload.decode()
    print('for m1',m)
    if m=='1':
        gp.output(8,1)
    elif m=='0':
        gp.output(8,0)
def on_m2(c,userdata,msg):
    m=msg.payload.decode()
    print('for m2',m)
    if m=='1':
        gp.output(10,1)
    elif m=='0':
        gp.output(10,0)
c.message_callback_add('smartfactory0/m1',on_m1)
c.message_callback_add('smartfactory0/m2',on_m2)
c.on_connect=onc
c.loop_forever()

    
