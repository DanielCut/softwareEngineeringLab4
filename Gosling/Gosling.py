import math
import time
from Util import *
from States import *

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.utils.game_state_util import GameState, BallState, CarState, Physics, Vector3 as vector3, Rotator

'''
Gosling by ddthj
Episode 6 Code
'''

class Gosling(BaseAgent):
    def initialize_agent(self):
        self.me = obj(None) #Objects that hold information such as location, velocity, rotation, etc
        self.ball = obj(None)
        self.friends = [] #Lists of objs of our teammates and opponents
        self.foes = []
        
        self.states = [pathFollow()] #All of our states
        self.state = self.states[0] #Our current state
        
        self.jump_time = 0 #How long it has been since last jump
        self.current_time = 0

    def checkState(self):
        if self.state.expired:
            self.state.reset() #If our state has expired, reset it and choose the next available state
            
            car = CarState(boost_amount=100, physics=Physics(velocity=vector3(0,0,0),angular_velocity=vector3(0,0,0),location=vector3(400,3000,20),rotation=Rotator(0, math.pi/2,0)))
            ball = BallState(physics=Physics(location=vector3(-3000,1000,94), velocity=vector3(1500,0,0)))
            game = GameState(ball=ball, cars = {self.index: car})
            self.set_game_state(game)
            flag = True
            for item in self.states:
                if item.available() == True:
                    self.state = item
                    flag = False
            if flag: #If no states are available do this:
                self.state = wait() 

    def get_output(self, game: GameTickPacket) -> SimpleControllerState:
        self.preprocess(game)
        if self.foes[0].location[2]>2000:
            car = CarState(boost_amount=100, physics=Physics(velocity=vector3(0,0,0),angular_velocity=vector3(0,0,0),location=vector3(0,0,20),rotation=Rotator(0, math.pi/2,0)))
            ball = BallState(physics=Physics(location=vector3(0,2000,94), velocity=vector3(0,0,0)))
            game = GameState(ball=ball, cars = {self.index: car})
            self.set_game_state(game)
        self.checkState()
        return self.state.execute(self)

    def preprocess(self,game):
        ball = game.game_ball.physics
        self.ball.location.data = [ball.location.x, ball.location.y, ball.location.z]
        self.ball.velocity.data = [ball.velocity.x, ball.velocity.y, ball.velocity.z]

        self.current_time = game.game_info.seconds_elapsed
        #Updates all car info
        for i in range(game.num_cars):
            car = game.game_cars[i]
            if i == self.index:
                self.me.update(car)
            else:
                car.index = i
                flag = True
                if car.team == self.team:
                    for item in self.friends:
                        if item.index == i:
                            item.update(car)
                            flag = False
                    if flag:
                        self.friends.append(obj(car))
                else:
                    for item in self.foes:
                        if item.index == i:
                            item.update(car)
                            flag = False
                    if flag:
                        self.foes.append(obj(car))
