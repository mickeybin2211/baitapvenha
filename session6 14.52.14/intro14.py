from datetime import *
import pyglet
while True:
    currentHour = datetime.now().hour
    currentMinute = datetime.now().minute
    if currentHour == 16 and currentMinute == 23:
 
        music = pyglet.resource.media('mmm-1.wav')
        music.play()
        pyglet.app.run()
        break 
    else : 
        print ("sdgsd")


    

    