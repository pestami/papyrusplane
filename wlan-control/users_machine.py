# users_machine.py

class my_machine:
   
    def do_commands(machine_cmd):

        from machine import Pin, PWM
      
        print("-----my_machine command-----")
        print(machine_cmd)
        for key, value in machine_cmd.items():
          print(f"{key}: {value}")
          
   # | MOTORL:1 | MOTORL:0 | MOTORL_PWM:73
        
        MOTORL= int(machine_cmd.get("MOTORL"))
        MOTORL_PWM= int(machine_cmd.get("MOTORL_PWM"))
        
        ndutyL=65535/100*(MOTORL_PWM)*MOTORL
        
        
        print(f"Duty Left: {ndutyL}")
        
        
        motorL = PWM(Pin(22,Pin.OUT), freq = 5000, duty = int(ndutyL))
        
#         MOTORR= machine_cmd.get["Lstatus"]
#         MOTORR_PWM= machine_cmd.get["Lduty"]
        
#         motorR = PWM(Pin(22), freq = 5000, duty = 65535*(MOTORR_PWM/100)*MOTORR)
       
#         from machine import Pin, PWM
#         p = Pin(22, machine.Pin.OUT)
#         pwm = machine.PWM(p, 1024)
#         pwm.duty(1010)

      


