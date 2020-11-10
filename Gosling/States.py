import math
import time
from rlbot.agents.base_agent import  SimpleControllerState
from Util import *

class pathFollow:
    def __init__(self):
        self.expired = False
        self.path = None
    def available(self):
        return True
    def reset(self):
        self.expired = False
        self.path = None
    def execute(self,agent):
        if isinstance(self.path,linePath):
            if self.path.game_time < agent.current_time:
                self.path = None
                return calcController(agent,agent.me.location,0)
            else:
                return pathController(agent,self.path)
        else:
            target = vectorLine(agent.ball.location, Vector3(0, 5150*-side(agent.team), 250))
            car_location = agent.me.location + (agent.me.velocity * 0.6)
            
            prediction = agent.get_ball_prediction_struct()
            for i in range(1,prediction.num_slices,60):
                prediction_slice = prediction.slices[i]
                time = prediction_slice.game_seconds - agent.current_time
                ball_location = Vector3(prediction_slice.physics.location.x,prediction_slice.physics.location.y,prediction_slice.physics.location.z)
                intercept = ball_location - (target.direction * (90+50))
                car_direction = vectorLine(intercept,car_location)
                distance = car_direction.length
                if ((ball_location[2]-100) / 1000) + 0.5 > (agent.me.boost/33.4):
                    continue
                else:
                    rotator = RotationMatrix2D(cap((math.pi - math.acos(car_direction.direction.dot(target.direction))) * -sign(car_direction.direction.dot(target.direction.cross(Vector3(0,0,1)))),-0.9,0.9))
                    temp = rotator.dot(target.direction * (distance / 2))
                    final = vectorLine(intercept-temp,intercept)
                    final.events.append(Event("aerial",time=prediction_slice.game_seconds))
                    final.events.append(Event("dodge",target=intercept))

                    secondary = vectorLine(car_location,final.start)
                    if abs(final.direction.angle(secondary.direction)) > 1.57:
                        secondary.events.append(Event("drift",target=final.end))
                    distance =final.length + secondary.length
                   
                    if (distance+.01)/time > 2200:
                        continue
                    print(distance, time)
                    self.path = linePath(prediction_slice.game_seconds, secondary,final)
                    break
        return calcController(agent,agent.me.location,0)

def pathController(agent,path):
    agent.renderer.begin_rendering()
    agent.renderer.draw_line_3d(path.lines[0].start, path.lines[0].end, agent.renderer.create_color(255,255,255,255))
    agent.renderer.draw_line_3d(path.lines[1].start, path.lines[1].end, agent.renderer.create_color(255,255,255,255))
    agent.renderer.end_rendering()
    c = SimpleControllerState()
    #this massive chain of if/elif handles all events that could have been triggered along the path
    if isinstance(path.Event,Event):
        event = path.Event
        if event.type == "drift":
            local = toLocal(path.lines[-1].end,agent.me)
            angle = math.atan2(local[1],local[0])
            c.yaw= steerPD(angle,-agent.me.rvelocity.data[1]/5)
            c.throttle = 1.0
            c.handbrake = True
            if abs(angle) < 0.1:
                c.handbrake = False
                path.Event.done = True
                path.Event = None
            return c
        elif event.type == "dodge":
            elapsed = agent.current_time - agent.jump_time
            local = toLocal(event.target,agent.me).normalize()
            if elapsed > 2.2 and agent.me.grounded:
                agent.jump_time = agent.current_time
                c.jump = True
            elif elapsed <= 0.1:
                c.jump = True
                c.pitch = -local[1]
                c.yaw= -local[0]
            elif elapsed > 0.1 and elapsed <= 0.15:
                c.jump = False
                c.pitch = -local[1]
                c.yaw = -local[0]
            elif elapsed > 0.15 and elapsed <=1:
                c.jump = True
                c.pitch = -local[1]
                c.yaw = -local[0]
            else:
                c.jump = False
                path.Event.done = True
                path.Event = None
            return c
        elif event.type == "aerial":
            elapsed = agent.current_time - agent.jump_time
            if elapsed > 2.2 and agent.me.grounded:
                agent.jump_time = agent.current_time
                c.jump = True
            elif elapsed <0.25:
                c.jump = True
            time_left = event.time-agent.current_time
            target = backsolveFuture(agent.me.location, agent.me.velocity,path.lines[-1].end,time_left)
            if target.magnitude() < 100:
                local = tolocal(path.lines[-1].end,agent.me)
            else:
                local = toLocal(agent.me.location+target,agent.me)
                c.boost = True
            yaw_to = math.atan2(local[1],local[0])
            pitch_to = math.atan2(local[2],local[0])
            c.yaw = steerPD(yaw_to,-agent.me.rvelocity[1]/4)
            c.pitch = steerPD(pitch_to,agent.me.rvelocity[0]/4)
            if abs(pitch_to) + abs(angle_to) >0.9:
                c.boost = False
            else:
                top = toLocal(agent.me.location+Vector3(0,0,500))
                roll_to = math.atan2(top[1],top[2])
                c.roll = steerPD(roll_to, agent.me.rvelocity[2]*0.5)
            if time_left <= 0.1:
                event.done = True
                path.Event = None
            return c

    turnRate = 1.5
    v = velocity1D(agent.me)[1]
    r = turn_radius(v)
    
    if path.line == 0:
        line = path.lines[0]
        nextLine = path.lines[1]
        firstProjection = line.project_distance(agent.me.location)
        secProjection = nextLine.project_distance(agent.me.location)
        if (agent.me.location - (line.start + line.direction *firstProjection)).magnitude() > (agent.me.location - (nextLine.start + nextLine.direction*secProjection)).magnitude():
            path.line = 1
        td = firstProjection + r
        for event in line.events:
            if event.type == "drift" and event.done == False:
                local = toLocal(nextLine.end,agent.me)
                angle = abs(math.atan2(local[1],local[0]))
                if angle/turnRate > (line.length-firstProjection) / (v+1):
                    path.Event = event                
        if td > line.length:
            target = nextLine.start + (nextLine.direction*(td-line.length))
        else:
            target = line.start + (line.direction * td)

        speed = ((line.length-firstProjection)+nextLine.length) / cap(path.game_time-agent.current_time,0.01,10)
    else:
        line = path.lines[-1]
        projection = line.project_distance(agent.me.location)
        td = projection + r

        for event in line.events:
            if event.type == "aerial" and event.done == False:
                time_2D = (line.end.flatten() - agent.me.location.flatten()).magnitude() / (v+1)
                time_3D = (line.end[2] - 100) / 1000
                if time_2D - 1 < time_3D:
                    path.Event = event
            elif event.type == "dodge" and event.done == False:
                time_2D = (line.end.flatten() - agent.me.location.flatten()).magnitude() / (v+1)
                if time_2D <= 1.1:
                    path.Event = event

        target = line.start + (line.direction * td)
        speed = (line.length - projection) / cap(path.game_time-agent.current_time,0.01,10)
    local = toLocal(target,agent.me)
    angle = math.atan2(local.data[1],local.data[0])
    c.steer = steer(angle)
    c.throttle, c.boost = throttle(speed,v)
    return c
                    
        
        
        
            
class futureShot:
    def __init__(self):
        self.expired = False
        self.path = None
    def available(self):
        return True
    def reset(self):
        self.expired = False
        self.path = None
    def execute(self,agent):
        if True == False:
            pass
        else:
            target = vectorLine(agent.ball.location, Vector3(0, 5150*-sign(agent.team), 200))
            intercept = agent.ball.location - (target.direction * (90+50))
            car_location = agent.me.location + (agent.me.velocity * 0.6)
            car_direction = (car_location - intercept).normalize()
            #angle = math.asin(target.direction.cross(car_direction).dot(Vector3(0,0,1)))
            angle = (math.pi - math.acos(car_direction.dot(target.direction))) * -sign(car_direction.dot(target.direction.cross(Vector3(0,0,1))))
            
            first_distance = cap((0.5 * agent.me.velocity.magnitude()) + ((intercept-car_location).magnitude() * 0.15),100,3000)
            
            print(angle,first_distance)

            if abs(angle) < 0.8:
                first_line = vectorLine(intercept+(car_direction*first_distance), intercept)
                self.path = linePath(first_line)
            else:
                rotator = RotationMatrix2D(cap(angle,-0.8,0.8))
                first_line = vectorLine(intercept + (rotator.dot(target.direction*-1).normalize()*first_distance), intercept)
                second_line = vectorLine(car_location, first_line.start)
                self.path = linePath(second_line, first_line)
            agent.renderer.begin_rendering()
            agent.renderer.draw_line_3d(agent.ball.location, target.start, agent.renderer.create_color(255,255,0,0))
            agent.renderer.draw_line_3d(agent.ball.location, intercept, agent.renderer.create_color(255,0,255,0))
            for line in self.path.lines:
                agent.renderer.draw_line_3d(line.start, line.end, agent.renderer.create_color(255,0,0,255))
            agent.renderer.end_rendering()
        return calcController(agent, agent.foes[0].location, cap((distance2D(agent.me.location, agent.foes[0].location)/5)-70,0,2300))

class calcShot:
    def __init__(self):
        self.expired = False

    def available(self,agent):
        if (ballReady(agent) and abs(agent.ball.location[1]) < 5050) and (ballProject(agent) > 0.3 * distance2D(agent.me,agent.ball)):
            return True
        return False

    def execute(self,agent):
        agent.controller = calcController

        #getting the coordinates of the goalposts
        leftPost = Vector3(-sign(agent.team)*700 , 5100*-sign(agent.team), 200)
        rightPost = Vector3(sign(agent.team)*700, 5100*-sign(agent.team), 200)
        center = Vector3(0, 5150*-sign(agent.team), 200)

        #time stuff that we don't worry about yet, the fact that guess is forced to 0 means this doesn't actually do anything right now
        time_guess = 0
        bloc = future(agent.ball,time_guess)

        #vectors from the goalposts to the ball & to Gosling
        ball_left = angle2(bloc,leftPost)
        ball_right = angle2(bloc,rightPost)
        agent_left = angle2(agent.me,leftPost)
        agent_right = angle2(agent.me,rightPost)

        #determining if we are left/right/inside of cone
        if agent_left > ball_left and agent_right > ball_right:
            goal_target = rightPost
        elif agent_left > ball_left and agent_right < ball_right:
            goal_target = None
        elif agent_left < ball_left and agent_right < ball_right:
            goal_target = leftPost
        else:
            goal_target = None

        if goal_target != None:
            #if we are outside the cone, this is the same as Gosling's old code
            goal_to_ball = (agent.ball.location - goal_target).normalize()
            goal_to_agent = (agent.me.location - goal_target).normalize()
            difference = goal_to_ball - goal_to_agent
            error = cap(abs(difference[0])+ abs(difference[1]),1,10)
        else:
            #if we are inside the cone, our line to follow is a vector from the ball to us (although it's still named 'goal_to_ball')
            goal_to_ball = (agent.me.location - agent.ball.location).normalize()
            error = cap( distance2D(bloc,agent.me) /1000,0,1)

        testVector = ROTATE * goal_to_ball

        #same as Gosling's old distance calculation, but now we consider dpp_skew which helps us handle when the ball is moving
        target_distance =cap( (40 + distance2D(agent.ball.location,agent.me)* (error**2))/1.8, 0,4000)
        target_location = agent.ball.location + Vector3([(goal_to_ball.data[0]*target_distance), goal_to_ball.data[1]*target_distance,0])

       #this adjusts the target based on the ball velocity perpendicular to the direction we're trying to hit it
        multiplier = cap(distance2D(agent.me,target_location) / 1500,0,2) #reduces the adjustment as we get closer so that we still hit the ball
        target_mod_distance = cap((testVector * agent.ball.velocity)*multiplier, -1000,1000)
        final_mod_vector = Vector3([ testVector.data[0] * target_mod_distance, testVector.data[1] * target_mod_distance,0])
        pre_loc = target_location
        target_location += final_mod_vector
        
        #another target adjustment that applies if the ball is close to the wall
        extra = 3850 - abs(target_location.data[0])
        if extra < 0:
            # we prevent our target from going outside the wall, and extend it so that Gosling gets closer to the wall before taking a shot, makes things more reliable
            target_location.data[0] = cap(target_location.data[0],-3850,3850) 
            target_location.data[1] = target_location.data[1] + (-sign(agent.team)*cap(extra,-800,800))

        #getting speed, this would be a good place to modify because it's not very good
        target_local = toLocal(target_location,agent.me)
        angle_to_target = math.atan2(target_local.data[1], target_local.data[0])
        distance_to_target = distance2D(target_location,agent.me.location)
        speed = 2300 -  cap((900*(angle_to_target**2)),0,2200) + cap((distance_to_target-1000)/4,0,500)

        #picking our rendered target color based on the speed we want to go
        colorRed = cap(int( (speed/2300) * 255),0,255)
        colorBlue =cap(255-colorRed,0,255)

        #see the rendering tutorial on github about this, just drawing lines from the posts to the ball and one from the ball to the target

        agent.renderer.begin_rendering()
        agent.renderer.draw_line_3d(bloc.data, leftPost.data, agent.renderer.create_color(255,255,0,0))
        agent.renderer.draw_line_3d(bloc.data, rightPost.data, agent.renderer.create_color(255,0,255,0))

        agent.renderer.draw_line_3d(agent.ball.location.data,pre_loc.data, agent.renderer.create_color(255,colorRed,0,colorBlue))
        agent.renderer.draw_line_3d(pre_loc.data,target_location.data, agent.renderer.create_color(255,colorRed,0,colorBlue))
        agent.renderer.draw_rect_3d(target_location.data, 10,10, True, agent.renderer.create_color(255,colorRed,0,colorBlue))
        agent.renderer.end_rendering()


        if  ballReady(agent) == False or abs(agent.ball.location.data[1]) > 5050 or ballProject(agent) < 0:
            self.expired = True
        return agent.controller(agent,target_location,speed)
        

class quickShot:
    def __init__(self):
        self.expired = False
        
    def available(self,agent):
        if ballProject(agent) > -0.5 * distance2D(agent.me,agent.ball) and (timeZ(agent.ball)<0.8):
            return True
        return False
    
    def execute(self,agent):
        leftPost = Vector3([-sign(agent.team)*700 , 5100*-sign(agent.team), 200])
        rightPost = Vector3([sign(agent.team)*700, 5100*-sign(agent.team), 200])
        ball_left = angle2(agent.ball.location,leftPost)
        ball_right = angle2(agent.ball.location,rightPost)
        agent_left = angle2(agent.me,leftPost)
        agent_right = angle2(agent.me,rightPost)
        if agent_left > ball_left and agent_right > ball_right:
            goal_target = leftPost
        elif agent_left > ball_left and agent_right < ball_right:
            goal_target = None
        elif agent_left < ball_left and agent_right < ball_right:
            goal_target = rightPost
        else:
            goal_target = None
        if goal_target != None:
            goal_to_ball = (agent.ball.location - goal_target).normalize()
        else:
            goal_to_ball = (agent.me.location - agent.ball.location).normalize()
            
        testVector = ROTATE * goal_to_ball
        target_distance =cap( distance2D(agent.ball.location,agent.me)/4, 0,1000)
        target_location = agent.ball.location + Vector3([(goal_to_ball.data[0]*target_distance), goal_to_ball.data[1]*target_distance,0])

        multiplier = cap(distance2D(agent.me,target_location) / 1500,0,2)
        target_mod_distance = cap((testVector * agent.ball.velocity)*multiplier, -1000,1000)
        final_mod_vector = Vector3([ testVector.data[0] * target_mod_distance, testVector.data[1] * target_mod_distance,0])
        target_location += final_mod_vector
        
        location = toLocal(target_location,agent.me)
        angle_to_target = math.atan2(location.data[1],location.data[0])  
        distance_to_target = distance2D(target_location,agent.me.location)
        speed = 2300 -  cap((900*(angle_to_target**2)),0,2200) + cap((distance_to_target-1000)/4,0,500)

        agent.controller = shotController
        
        if self.available(agent) == False:
            self.expired = True
        if calcShot().available(agent) == True:
            self.expired = True

        agent.renderer.begin_rendering()
        agent.renderer.draw_line_3d(agent.ball.location.data, leftPost.data, agent.renderer.create_color(255,255,0,0))
        agent.renderer.draw_line_3d(agent.ball.location.data, rightPost.data, agent.renderer.create_color(255,0,255,0))
        agent.renderer.draw_line_3d(agent.ball.location.data,target_location.data, agent.renderer.create_color(255,0,255,255))
        agent.renderer.end_rendering()

        
        return agent.controller(agent,target_location, speed)

class wait():
    def __init__(self):
        self.expired = False
    def available(self, agent):
        if timeZ(agent.ball) > 1:
            return True
    def execute(self,agent):
        #taking a rough guess at where the ball will be in the future, based on how long it will take to hit the ground
        ball_future = future(agent.ball, timeZ(agent.ball))
        if agent.me.boost < 35: #if we are low on boost, we'll go for boot
            closest = 0
            closest_distance =  distance2D(boosts[0], ball_future) 

            #going through every large pad to see which one is closest to our ball_future guesstimation
            for i in range(1,len(boosts)):
                if distance2D(boosts[i], ball_future) < closest_distance:
                    closest = i
                    closest_distance =  distance2D(boosts[i], ball_future)

            target = boosts[closest]
            speed = 2000
        else:
            #if we have boost, we just go towards the ball_future position, and slow down just like in exampleATBA as we get close
            target = ball_future
            target_local = toLocal(target,agent.me)
            current = velocity1D(agent.me).data[1]
            ratio = distance2D(agent.me,target)/(current+0.01)
            
            speed = cap(600 * ratio,0,2300)
            if speed < 100:
                speed = 0
  

        if ballReady(agent):
            self.expired = True
        return frugalController(agent,target,speed)  
      

def frugalController(agent,target,speed):
    controller_state = SimpleControllerState()
    location = toLocal(target,agent.me)
    angle_to_target = math.atan2(location.data[1],location.data[0])

    controller_state.steer = steer(angle_to_target)
    
    speed -= ((angle_to_target**2)*300)
    current_speed = velocity1D(agent.me).data[1]
    if current_speed < speed:
        controller_state.throttle = 1.0
    elif current_speed - 50 > speed:
        controller_state.throttle = -1.0
    else:
        controller_state.throttle = 0

    time_difference = time.time() - agent.start
    if time_difference > 2.2 and distance2D(target,agent.me) > (velocity2D(agent.me)*2.3) and abs(angle_to_target) < 0.9 and current_speed < speed and current_speed > 220:
        agent.start = time.time()
    elif time_difference <= 0.1:
        controller_state.jump = True
        controller_state.pitch = -1
    elif time_difference >= 0.1 and time_difference <= 0.15:
        controller_state.jump = False
        controller_state.pitch = -1
    elif time_difference > 0.15 and time_difference < 1:
        controller_state.jump = True
        controller_state.yaw = controller_state.steer
        controller_state.pitch = -1

    return controller_state

def calcController(agent, target_object,target_speed):
    location = toLocal(target_object,agent.me)
    controller_state = SimpleControllerState()
    angle_to_ball = math.atan2(location.data[1],location.data[0])

    current_speed = velocity1D(agent.me).data[1]
    controller_state.steer = steer(angle_to_ball)

    #throttle
    controller_state.throttle, controller_state.boost = throttle(target_speed,current_speed)
    
    return controller_state

def shotController(agent, target_object,target_speed,goal = None):
    if goal == None:
        goal =  [0,-sign(agent.team)*FIELD_LENGTH/2,100]
    goal_local = toLocal(goal,agent.me)
    goal_angle = math.atan2(goal_local.data[1],goal_local.data[0])
    location = toLocal(target_object,agent.me)
    controller_state = SimpleControllerState()
    angle_to_target = math.atan2(location.data[1],location.data[0])

    current_speed = velocity1D(agent.me).data[1]#velocity2D(agent.me)
    #steering
    controller_state.steer = steer(angle_to_target)

    #throttle
    if target_speed > 1400 and target_speed > current_speed and agent.start > 2.5 and current_speed < 2250 and agent.me.grounded == True:
        controller_state.boost = True
    if target_speed > current_speed:
        controller_state.throttle = 1.0
    elif target_speed < current_speed:
        controller_state.throttle = -1.0

    #dodging
    closing = distance2D(target_object,agent.me)/cap(-dpp(target_object, agent.ball.velocity,agent.me.location,agent.me.velocity),1,2300)
    time_difference = time.time() - agent.start
    if ballReady(agent) and time_difference > 2.2 and closing <=0.8 and distance2D(agent.me,target_object)< 200:
        agent.start = time.time()
    elif time_difference <= 0.1:
        controller_state.jump = True
        controller_state.pitch = -1
    elif time_difference >= 0.1 and time_difference <= 0.15:
        controller_state.jump = False
        controller_state.pitch = -1
    elif time_difference > 0.15 and time_difference < 1:
        controller_state.jump = True
        controller_state.yaw = math.sin(goal_angle)
        controller_state.pitch = -abs(math.cos(goal_angle))      

    return controller_state
