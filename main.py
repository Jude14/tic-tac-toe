import turtle
import time

def draw_cross(crosses):
  crosses.pendown()
  crosses.goto( crosses.pos() + (15,-15) )
  crosses.goto( crosses.pos() + (-30,30) )
  crosses.goto( crosses.pos() + (15,-15) )
  crosses.goto( crosses.pos() + (15,15) )
  crosses.goto( crosses.pos() + (-30,-30) )
  crosses.penup()


def draw_circle(circles):
  circles.goto( circles.pos() + (0,-20) )
  circles.pendown()
  circles.circle(20)
  circles.penup()

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
coordinates = {'7': (-60,60) , '8': (0,60) , '9': (60,60) ,
            '4': (-60,0) , '5': (0,0) , '6': (60,0) ,
            '1': (-60,-60) , '2': (0,-60) , '3': (60,-60) }

    
  
  
def game():
    circles = turtle.Turtle()
    circles.color("red")
    circles.penup()
    circles.hideturtle()
    crosses = turtle.Turtle()
    crosses.color("blue")
    crosses.penup()
    crosses.hideturtle()
  
    lines = turtle.Turtle()
    lines.hideturtle()
    lines.penup()
  
    lines.goto(30,100)
    lines.pendown()
    lines.goto(30,-100)
    lines.penup()
    lines.goto(-30,-100)
    lines.pendown()
    lines.goto(-30,100)
    lines.penup()
  
    lines.goto(100,30)
    lines.pendown()
    lines.goto(-100,30)
    lines.penup()
    lines.goto(-100,-30)
    lines.pendown()
    lines.goto(100,-30)
    lines.penup()
    lines.hideturtle()
  

    turn = 'X'
    count = 0


    while count!=9:
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            if turn=='X':
              crosses.goto(coordinates[move])
              draw_cross(crosses)#at location
            else:
              circles.goto(coordinates[move])
              draw_circle(circles)#at location
            
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
      
        


      
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                lines.goto(coordinates['7'])
                lines.pendown()
                lines.forward(130)
                lines.penup()
                time.sleep(1)


                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                lines.goto(coordinates['4'])
                lines.pendown()
                lines.forward(130)
                lines.penup()                
                time.sleep(1)

                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                lines.goto(coordinates['1'])
                lines.pendown()
                lines.forward(130)
                lines.penup()                
                time.sleep(1)

                
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                lines.goto(coordinates['7'])
                lines.pendown()
                lines.goto(lines.pos()+(0,-130))
                lines.penup()
                time.sleep(1)

                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                lines.goto(coordinates['8'])
                lines.pendown()
                lines.goto(lines.pos()+(0,-130))
                lines.penup()
                time.sleep(1)

                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                lines.goto(coordinates['9'])
                lines.pendown()
                lines.goto(lines.pos()+(0,-130))
                lines.penup()
                time.sleep(1)

                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                lines.goto(coordinates['7'])
                lines.pendown()
                lines.goto(lines.pos()+(160,-160))
                lines.penup()
                time.sleep(1)
                
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                lines.goto(coordinates['1'])
                lines.pendown()
                lines.goto(lines.pos()+(160,160))
                lines.penup()
                time.sleep(1)

                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

      
        if count == 9:
            lines.goto(-30,150)
            lines.write("Game Over")
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            break

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    

game()
  
