import time 


def automated_task():
    path='/Users/fourofour/Professional/Jio-2024/JIO-MLOPS-24/ML-OPS/001-Introduction-To-Automation'
    file_name = f'{path}/file_{time.time()}.txt' 
    file = open(file_name, 'w') 
    file.write('Hello, Automation!') 
    file.write('Automation makes ML more fun!') 
    file.write('We last executed on ' + str(time.time()))

    file.close() 


if __name__ == '__main__':
    automated_task() 