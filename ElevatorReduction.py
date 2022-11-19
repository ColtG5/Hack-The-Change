import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def init():
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
    cycles = 0
    while (cycles < 3):
        GPIO.output(26,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(26,GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(26,GPIO.HIGH)
        cycles += 1

def main():

    init()
    
    try:
        while True:
            dist = distance()
            sleep_time = 0.2
            time.sleep(sleep_time)
            prev_dist = 0
            if ((dist < 100) and (prev_dist < 100)):
                buzzer()
                prompt()
            prev_dist = dist

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

if __name__ == '__main__':
    main()

        