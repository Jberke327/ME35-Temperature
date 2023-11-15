import machine
from machine import Pin, PWM
import simple as mqtt
import network
import ADC
import time
import airtable
import controller as gamepad


station = network.WLAN(network.STA_IF)
station.active(True)

station.connect('Tufts_Wireless')
while station.isconnected() == False:
    time.sleep(1)
    pass
print('Connection successful')
print(station.ifconfig())

YOUR_USERNAME = 'Jberke327'  # Replace with your Adafruit IO username
YOUR_AIOKEY = 'aio_SUOq77frYgPzWYbHJjWm4tbK0SkF'  # Replace with your Adafruit IO AIO key

url = f'https://io.adafruit.com/api/v2/{YOUR_USERNAME}/feeds'  # Use an f-string to insert your username

headers = {'X-AIO-Key': YOUR_AIOKEY, 'Content-Type': 'application/json'}

reply = requests.get(url, headers=headers)

if reply.status_code == 200:
    print(reply.text)
    reply_data = reply.json()  # Parse the JSON response into a Python data structure
    keys = [x['key'] for x in reply_data]
    groups = [x['group']['name'] for x in reply_data]
    names = [x['name'] for x in reply_data]
    values = [x['last_value'] for x in reply_data]
    ids = [x['id'] for x in reply_data]
    print(keys)
    print(values)
else:
    print(f"Request failed with status code: {reply.status_code}")


unit = "C"
temp = 25
gyros = [0, 0, 0]

gamepad.digital_setup()

x, y, button = gamepad.read_everything()
red = Pin(15, Pin.OUT, Pin.PULL_UP)
white = Pin(14, Pin.OUT, Pin.PULL_UP)
blue = pin(13, pin.OUT, Pin.PULL_UP)
temp = ADC(26)

async def buttoncheck()
    if (button == 'A')
        sending = "Temperature too hot! Turning on AC"
        url = '' % (YOUR_USERNAME, "up-down")
        data = {'value':sending}
        reply = requests.post(url,headers=headers,json=data)
        reply.close()
        red.off()
        await asyncio.sleep (0.2)
    elif (button =='B')
        sending = "Temperature normal"
        url = '' % (YOUR_USERNAME, "up-down")
        data = {'value':sending}
        reply = requests.post(url,headers=headers,json=data)
        reply.close()
        white.off()
        await asyncio.sleep (0.2)
    elif (button =='X')
        sending = "Temperature too cold! Turning on heater"
        url = '' % (YOUR_USERNAME, "up-down")
        data = {'value':sending}
        reply = requests.post(url,headers=headers,json=data)
        reply.close()
        blue.off()
        await asyncio.sleep (0.2)
    else:
        await asyncio.sleep (0.2)
        
async def tempcheck()
        temp = 10000.0 / (65535 / float(therm.read_u16()) - 1)
        lntemp = log(temp / 10000)
        degC = -273.15 + 1/(1/298.15 + lntemp/3977)
        degF = degC*(9/5) + 32
        if unit == "C":
            temperature = degC
        else:
            temperature = degF
        print(temp)
    if (temperature > 70):
        red.on()
        await asyncio.sleep(1)
    elif (temperature <= 70 and temperature >= 50):
        white.on()
        await asyncio.sleep(1)
    else:
        blue.on()
        await asyncio.sleep(1)
        
async def timer():
    now = time.localtime(time.time())
    minutes = 0
    current_sec = timer()
    if (current_sec == 59):
        mins = minutes + 1
        
        if (mins % 5 == 0):
            sending = temperature
            url = '' % (YOUR_USERNAME, "temperature")
            data = {'value':sending}
            reply = requests.post(url,headers=headers,json=data)
            reply.close()
            await asyncio.sleep(0.2)
        else:
            await asyncio.sleep(0.2)
    else:
        await asynio.sleep(0.2)
        
async def read_airtable():
    global unit
    while True:
        color = airtable.getColor()
        if color == "Red":
            unit = "F"
        else:
            unit = "C"
        await asyncio.sleep(3)
        

async def main():
    try:
        temp_task = asyncio.create_task(tempcheck)
        pub_task = asyncio.create_task(timer)
        button_task = asyncio.create_task(buttoncheck)
        air_task = asyncio.create_task(read_airtable)
        await asyncio.gather(button_task, temp_task, pub_task, air_task)
    except:
        print("error")

#Infinite loop that will send out data until the program ends        
while True:
    asyncio.run(main())

    
