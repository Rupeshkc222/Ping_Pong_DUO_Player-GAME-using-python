import pygame

pygame.init()
game_font=pygame.font.SysFont('Arial',40)

#some constants and variables
object_color=(222, 116, 111)
black=(0,0,0)

width=600
height=600

delay=30 #more value then slow

paddle_speed=20
paddle_width=10
paddle_height=100

p1_x_pos=10
p1_y_pos=height/2 - paddle_height/2

p2_x_pos=width-paddle_width-10
p2_y_pos=height/2 - paddle_height/2

p1_score=0
p2_score=0

p1_up=False
p1_down=False
p2_up=False
p2_down=False

ball_x_pos=width/2
ball_y_pos=height/2
ball_width=8
ball_x_velocity=-10
ball_y_velocity=0

#window to display
window=pygame.display.set_mode((width,height))

#to display the player
def display():
    pygame.draw.rect(window,object_color,(int(p1_x_pos),int(p1_y_pos),paddle_width,paddle_height))
    pygame.draw.rect(window,object_color,(int(p2_x_pos),int(p2_y_pos),paddle_width,paddle_height))
    pygame.draw.circle(window, object_color, (ball_x_pos,ball_y_pos),ball_width)
    pygame.draw.aaline(window,object_color,(300,0),(300,600))
    pygame.draw.circle(window,(222, 116, 111),center=(300,300),radius=930,width=1)
    score=game_font.render(f"P1   {str(p1_score)}-{str(p2_score)}   P2",False,object_color)
    window.blit(score,(width/2-90,20))  #display the score in the screen

def on_player_move():
    global p1_y_pos
    global p2_y_pos

    if p1_up:
        p1_y_pos=max(p1_y_pos-paddle_speed,0)
    elif p1_down:
        p1_y_pos=min(p1_y_pos+paddle_speed,height)
    if p2_up:
        p2_y_pos=max(p2_y_pos-paddle_speed,0)
    elif p2_down:
        p2_y_pos=min(p2_y_pos+paddle_speed,height)

def on_ball_movement():
    global ball_x_pos
    global ball_y_pos
    global ball_x_velocity
    global ball_y_velocity
    global p1_score
    global p2_score

    if (ball_x_pos + ball_x_velocity < p1_x_pos+paddle_width) and (p1_y_pos<ball_y_velocity+ball_y_pos+ball_width < p1_y_pos + paddle_height):
        ball_x_velocity=-ball_x_velocity
        ball_y_velocity=(p1_y_pos+paddle_height/2 - ball_y_pos) / 15
        ball_y_velocity=-ball_y_velocity
    elif ball_x_pos+ball_x_velocity<0:
        p2_score+=1
        ball_x_pos=width/2
        ball_y_pos=height/2
        ball_x_velocity=10
        ball_y_velocity=0
    if (ball_x_pos + ball_x_velocity > p2_x_pos-paddle_width) and (p2_y_pos<ball_y_velocity+ball_y_pos+ball_width < p2_y_pos +paddle_height):
        ball_x_velocity = -ball_x_velocity
        ball_y_velocity = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_velocity = -ball_y_velocity
    elif ball_x_pos+ball_x_velocity>height:
        p1_score+=1
        ball_x_pos=width/2
        ball_y_pos=height/2
        ball_x_velocity=-10
        ball_y_velocity=0
    if ball_y_velocity+ball_y_pos >height or ball_y_pos+ball_y_velocity <0:
        ball_y_velocity=-ball_y_velocity

    ball_x_pos+=ball_x_velocity
    ball_y_pos += ball_y_velocity


pygame.display.set_caption("PING PONG GAME")
pygame.display.flip()

runn=True
while runn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runn=False
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runn=False
            if event.key == pygame.K_w:
                p1_up=True
            if event.key == pygame.K_s:
                p1_down=True
            if event.key == pygame.K_UP:
                p2_up=True
            if event.key == pygame.K_DOWN:
                p2_down=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1_up=False
            if event.key == pygame.K_s:
                p1_down=False
            if event.key == pygame.K_UP:
                p2_up=False
            if event.key == pygame.K_DOWN:
                p2_down=False
    window.fill(black)
    on_player_move()
    on_ball_movement()
    display()
    pygame.display.flip()
    pygame.time.wait(delay)



