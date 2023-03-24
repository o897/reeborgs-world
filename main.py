move()

def turn_right() :
        turn_left()
        turn_left()
        turn_left()

def jump() :
    for l in range(1,7) :  
        for j in range (0,1) :
            turn_left()
            move()
            turn_right()
            move()

        for d in range (0,1) :
            turn_right()
            move()
            turn_left()
        
        if l == 6 :
            done()
            
        move()
          
jump()

  

    