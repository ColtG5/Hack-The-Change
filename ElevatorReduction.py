import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

# distance is in cm
DISTANCE_FOR_SENSOR_ACTIVATION = 325

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def init():
        GPIO.setmode(GPIO.BCM)

        GPIO_TRIGGER = 18
        GPIO_ECHO = 24

        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)


        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26,GPIO.OUT)
        pass

def distance():
    
    GPIO.output(GPIO_TRIGGER, True)
    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    
    distance = (TimeElapsed * 34300) / 2
    
    return distance


def prompt():
    print("Use stairs or die")

def buzzer():
    init()
    cycles = 0
    while (cycles < 5):
        GPIO.output(26,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(26,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(26,GPIO.HIGH)
        cycles += 1

def sensor():

    init()

    prev_dist = 0

    try:
        while True:
            dist = distance()
            print(dist)
            sleep_time = 0.1
            time.sleep(sleep_time)
            # if ((dist < DISTANCE_FOR_SENSOR_ACTIVATION) and (prev_dist < DISTANCE_FOR_SENSOR_ACTIVATION)):
            #     GPIO.cleanup()
            #     return
            # prev_dist = dist
            if (dist < DISTANCE_FOR_SENSOR_ACTIVATION):
                GPIO.cleanup()
                return

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

