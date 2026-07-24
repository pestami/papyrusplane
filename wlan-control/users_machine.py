# users_machine.py

from DIYables_MicroPython_Servo import Servo
from machine import Pin, PWM

try:
      # LEFT
  if motorL_FORWARD is not None:
          motorL_FORWARD.deinit()
  if motorL_FORWARD is not None:
          motorL_BACKWARD.deinit()
      # RIGHT
  if motorL_FORWARD is not None:
          motorR_FORWARD.deinit()
  if motorL_FORWARD is not None:
          motorR_FORWARD.deinit()
  print("Deintialized PWM")
except:
  print("No PWM instantiated")
  
lPINS=[19,13,23,18]

if 5==5:
    # LEFT
    motorL_FORWARD = PWM(Pin(lPINS[0],Pin.OUT), freq = 5000, duty = 0)
    motorL_BACKWARD = PWM(Pin(lPINS[1],Pin.OUT), freq = 5000, duty = 0)

    # RIGHT
    motorR_FORWARD = PWM(Pin(lPINS[2],Pin.OUT), freq = 5000, duty = 0)
    motorR_BACKWARD = PWM(Pin(lPINS[3],Pin.OUT), freq = 5000, duty = 0)
#finally:

    
    # Create a Servo object
servo = Servo(17) # The ESP32 pin GPIO26 connected to the servo motor

class my_machine: 


    def __init__(self): 
      print("=======================================")
      #print("__init__()-----my_machine command-----")     
      #print("__init__()-----COMPLETED--------------")
#---------------------------------------------------------------   
    def do_commands(self,machine_cmd): 
        print("==================================================")
        print("\n BEGIN do_commands()-----my_machine command-----")
        print("echo Recieved JASON =\n ")  
        print(machine_cmd)
        print("LIST parameters---BEGIN---------------------------")  
        for key, value in machine_cmd.items():
          print(f"{key}: {value}")
      
        print("LIST parameters---END-----------------------------")  
        print("==================================================")
#---------------------------------------------------------------  

        #------------GET operational values for motors
        
        #{ "MOTORL_PWM": value1, "MOTORL_ENABLE": value2, "MOTORL_DIRECTION": value3, "MOTORR_PWM": value4, "MOTORR_ENABLE": value5, "MOTORR_DIRECTION": value6, "SERVO_A": value7 }
      
       
        print("DEBUG LINE 45")  
        MOTORL_PWM= int(machine_cmd.get("MOTORL_PWM"))
        MOTORL_ENABLE= int(machine_cmd.get("MOTORL_ENABLE"))    
        MOTORL_DIRECTION= int(machine_cmd.get("MOTORL_DIRECTION"))
       
        MOTORR_PWM= int(machine_cmd.get("MOTORR_PWM"))
        MOTORR_ENABLE= int(machine_cmd.get("MOTORR_ENABLE"))        #MOTORR_ENABLE: 0: 0
        MOTORR_DIRECTION= int(machine_cmd.get("MOTORR_DIRECTION"))
        
        SERVO_A= int(machine_cmd.get("SERVO_A"))
        
#----------------------Calculate Duty
        
        print("BEGIN ----------------Calculate Motor Duty Cycle-----18:10")  
      
        nDutyL=int(1021/100*(MOTORL_PWM)) # max duty is 1023 LED is LOW
        if MOTORL_ENABLE==0:
          nDutyL=0
        
        nDutyR=int(1021/100*(MOTORR_PWM)) # max duty is 1023 LED is LOW
        if MOTORR_ENABLE==0:
          nDutyR=0
        
        print(f"Duty Left PWM: {nDutyL} Motor ON/OFF: {MOTORL_ENABLE} Motor Direction: {MOTORL_DIRECTION}")
        print(f"Duty Right PWM: {nDutyR} Motor ON/OFF: {MOTORR_ENABLE} Motor Direction: {MOTORR_DIRECTION}")
        
        if MOTORL_DIRECTION == 1:
            motorL_FORWARD.duty(nDutyL)
            motorL_BACKWARD.duty(0)
        else:
            motorL_FORWARD.duty(0)
            motorL_BACKWARD.duty(nDutyL)
            
        if MOTORR_DIRECTION == 1:
            motorR_FORWARD.duty(nDutyR)
            motorR_BACKWARD.duty(0)
        else:
            motorR_FORWARD.duty(0)
            motorR_BACKWARD.duty(nDutyR)
        

        print("END----------------------Calculate Motor Duty Cycle-----")
        
        print("BEGIN---ROTATE SERVO--------------------------------------\n")
        print(SERVO_A)
        servo.move_to_angle(SERVO_A)  # Set servo position to calculated angle
        print("END---ROTATE SERVO--------------------------------------")

        # ----------------------

def main():
    print("==================================================")
    print("main()---TEST_MY_MACHINE--------------------------")
  
    from users_machine import my_machine
    mpa_machine=my_machine()
  
    
    props={ "MOTORL_PWM": 90, "MOTORL_ENABLE": 0, "MOTORL_DIRECTION": 0, "MOTORR_PWM": 90, "MOTORR_ENABLE": 0, "MOTORR_DIRECTION": 0, "SERVO_A": 90 }         
    mpa_machine.do_commands(props) 
  
    print("main()---COMPLETED--------------------------------")
    print("==================================================")
   
    
if __name__ == "__main__":
    main()


