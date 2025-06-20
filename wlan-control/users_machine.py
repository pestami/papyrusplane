# users_machine.py

from machine import Pin, PWM

motorL = PWM(Pin(22,Pin.OUT), freq = 5000, duty = 0)
motorR = PWM(Pin(23,Pin.OUT), freq = 5000, duty = 0)

class my_machine: 


    def __init__(self):        
      print("\n__init__()-----my_machine command-----\n")     
      print("\n__init__()---------------COMPLETED----\n")
      
    def do_commands(self,machine_cmd):           
        print("\n do_commands()-----my_machine command-----")
        print(machine_cmd)
        for key, value in machine_cmd.items():
          print(f"{key}: {value}")        
   # | MOTORL:1 | MOTORL:0 | MOTORL_PWM:73

      #------------GET operational values for motors
        nMotorL= int(machine_cmd.get("MOTORL"))
        nMotorL_PWM= int(machine_cmd.get("MOTORL_PWM")) #LED is bright when PWM = 0

        nMotorR= int(machine_cmd.get("MOTORR"))
        nMotorR_PWM= int(machine_cmd.get("MOTORR_PWM"))       
        
      #----------------------Calculate Duty
        print("BEGIN ----------------Calculate Motor Duty Cycle-----16H10")  
      
        nDutyL=int(1021/100*(nMotorL_PWM)) # max duty is 1023 LED is LOW
        if nMotorL==0:
          nDutyL=0
        print("INFO: (1023=LED_dim 0=LED_bright)")
        print(f"Duty Left PWM: {nDutyL} Motor ON/OFF: {nMotorL}")
        motorL.duty(nDutyL)

        nDutyR=int(1021/100*(nMotorR_PWM)) # max duty is 1023 LED is LOW
        if nMotorR==0:
          nDutyR=0
        print("INFO: (1023=LED_dim 0=LED_bright)")
        print(f"Duty Left PWM: {nDutyR} Motor ON/OFF: {nMotorR}")
        motorR.duty(nDutyR)

        print("END----------------------Calculate Motor Duty Cycle-----")       
        # ----------------------

def main():
    print("\n main()===TEST_MY_MACHINE=============================================")
  
    from users_machine import my_machine
    mpa_machine=my_machine()

    props={ "MOTORL_PWM": 10, "MOTORL": 1, "MOTORR_PWM": 1, "MOTORR": 0  }          
    mpa_machine.do_commands(props) 
  
    print("main()===COMPLETED==================================================")

   
    
if __name__ == "__main__":
    main()


