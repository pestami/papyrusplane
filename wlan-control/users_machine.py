# users_machine.py

class my_machine:
   
    def do_commands(machine_cmd):

        from machine import Pin, PWM
      
        motorR = PWM(Pin(22), freq = 5000, duty = 200)
        motorL = PWM(Pin(19), freq = 5000, duty = 200)
      
        print("-----my_machine command-----")
        print(machine_cmd)
        for key, value in machine_cmd.items():
          print(f"{key}: {value}")
   

