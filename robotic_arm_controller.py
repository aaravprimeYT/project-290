from controller import Robot
from controller import Keyboard

robot = Robot()
kb = Keyboard()

motorA = robot.getDevice("A motor")
motorB = robot.getDevice("B motor")
motorC = robot.getDevice("C motor")
motorD = robot.getDevice("D motor")
motorE = robot.getDevice("E motor")
motorF = robot.getDevice("F motor")

timestep = int(robot.getBasicTimeStep())
kb.enable(timestep)

motorA_pos = 0
motorB_pos = 0
motorC_pos = 0
motorD_pos = 0
motorE_pos = 0
motorF_pos = 0

# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed = kb.getKey()   
    print(key_pressed) 
    
    if(key_pressed == 65):
        motorA_pos += 0.005
    if(key_pressed == 68):
        motorA_pos -= 0.005
        
    if(key_pressed == 87):
        motorB_pos += 0.01
    if(key_pressed == 83):
        motorB_pos-=0.01
        
    if(key_pressed == 67):
        motorC_pos += 0.01
    if(key_pressed == 90):
        motorC_pos -= 0.01
        
    if(key_pressed == 82):
        motorD_pos += 0.01
    if(key_pressed == 70):
        motorD_pos -= 0.01
        
    if(key_pressed == 315):
        motorE_pos += 0.01
    if(key_pressed == 317):
        motorE_pos -= 0.01
         
    if(key_pressed == 81):
        motorF_pos += 0.01
    if(key_pressed == 69):
        motorF_pos -= 0.01
        
    motorA.setPosition(motorA_pos)
    motorB.setPosition(motorB_pos)
    motorC.setPosition(motorC_pos)
    motorD.setPosition(motorD_pos)
    motorE.setPosition(motorE_pos)
    motorF.setPosition(motorF_pos)