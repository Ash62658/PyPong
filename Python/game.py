from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random
from kivy.uix.label import Label




class PongPaddle(Widget):
    score = NumericProperty(0)
    


    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = 0
    velocity_y = 0
    velocity = ObjectProperty(Vector(0, 0))

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos



class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    

    def serve_ball(self):
        self.ball.center = (540,1300)
        list = [0, 180]
        ballValLoc = random.choice(list)    
        self.ball.velocity = Vector(10, 0).rotate(ballValLoc)

    def update(self, dt):
        self.ball.move()
        
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball()
            
                
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball()

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    def pause_game(self):
        Clock.unschedule(self.update)
        

           
            
        