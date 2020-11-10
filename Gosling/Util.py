import math
from itertools import product
import time
GOAL_WIDTH = 1900
FIELD_LENGTH = 10280
FIELD_WIDTH = 8240

class Vector3:
    def __init__(self, *args):
        self.data = args[0] if isinstance(args[0],list) else [x for x in args]
    def __getitem__(self,key):
        return self.data[key]
    def __str__(self):
        return str(self.data)
    def __add__(self,value):
        return Vector3(self[0]+value[0], self[1]+value[1], self[2]+value[2])
    def __sub__(self,value):
        return Vector3(self[0]-value[0],self[1]-value[1],self[2]-value[2])
    def __mul__(self,value):
        return Vector3(self[0]*value, self[1]*value, self[2]*value)
    __rmul__ = __mul__
    def __div__(self,value):
        return Vector3(self[0]/value, self[1]/value, self[2]/value)
    def compare(self,value):
        x = 1 if self[0] == value[0] else 0
        if self[1] == value[1]: x += 1 
        if self[2] == value[2]: x += 1 
        return x
    def magnitude(self):
        return math.sqrt((self[0]*self[0]) + (self[1] * self[1]) + (self[2]* self[2]))
    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return Vector3(self[0]/mag, self[1]/mag, self[2]/mag)
        else:
            return Vector3(0,0,0)
    def dot(self,value):
        return self[0]*value[0] + self[1]*value[1] + self[2]*value[2]
    def cross(self,value):
        return Vector3((self[1]*value[2]) - (self[2]*value[1]),(self[2]*value[0]) - (self[0]*value[2]),(self[0]*value[1]) - (self[1]*value[0]))
    def flatten(self):
        return Vector3(self[0],self[1],0)
    def angle(self,vector):
        return math.atan2(vector[1],vector[0]) - math.atan2(self[1],self[0])
    
class RotationMatrix3D:
    def __init__(self,r):
        CR = math.cos(r[2])
        SR = math.sin(r[2])
        CP = math.cos(r[0])
        SP = math.sin(r[0])
        CY = math.cos(r[1])
        SY = math.sin(r[1])        
        self.data = [Vector3(CP*CY, CP*SY, SP),Vector3(CY*SP*SR-CR*SY, SY*SP*SR+CR*CY, -CP * SR),Vector3(-CR*CY*SP-SR*SY, -CR*SY*SP+SR*CY, CP*CR)]
    def dot(self,vector):
        return Vector3(self.data[0].dot(vector),self.data[1].dot(vector),self.data[2].dot(vector))
    
class RotationMatrix2D:
    def __init__(self,theta):
        self.data = [[math.cos(theta),-math.sin(theta)],[math.sin(theta), math.cos(theta)]]
    def dot(self,vector):
        return Vector3(self.data[0][0]*vector[0] + self.data[1][0]*vector[1], self.data[0][1]*vector[0] + self.data[1][1]*vector[1], 0)
    
class obj:
    def __init__(self, car):
        self.location = Vector3(0,0,0)
        self.velocity = Vector3(0,0,0)
        self.rotation = Vector3(0,0,0)
        self.rvelocity = Vector3(0,0,0)
        
        if car != None:
            self.team = car.team
            self.index = car.index
            self.update(car)
    def update(self,car):
        self.location.data = [car.physics.location.x, car.physics.location.y, car.physics.location.z]
        self.velocity.data = [car.physics.velocity.x, car.physics.velocity.y, car.physics.velocity.z]
        self.rotation.data = [car.physics.rotation.pitch, car.physics.rotation.yaw, car.physics.rotation.roll]
        self.boost = car.boost
        self.grounded = car. has_wheel_contact
        self.matrix = rotator_to_matrix(self)
        

        temp = Vector3(car.physics.angular_velocity.x, car.physics.angular_velocity.y, car.physics.angular_velocity.z)
        self.rvelocity.data = [temp.dot(self.matrix[1]),temp.dot(self.matrix[2]),temp.dot(self.matrix[0])]

class linePath:
    def __init__(self, time, *args):
        self.lines = [line for line in args]
        self.line = 0
        self.game_time = time
        self.Event = None

class vectorLine:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        temp = end-start
        self.length = temp.magnitude()
        self.direction = temp.normalize()
        self.events = []
    def project_distance(self,vector):
        return self.direction.dot(vector-self.start)

class Event:
    def __init__(self,t,**k):
        self.done = False
        self.type = t
        self.distance = k.get("distance")
        self.target = k.get("target")
        self.time = k.get("time")
        

def turn_radius(v):
    return 139.059 + (0.1539 * v) + (0.0001267716565 * v * v)

def in_field(point,radius):
    point = Vector3(abs(point[0]),abs(point[1]),abs(point[2]))
    if point[0] > 3860 - radius:
        return False
    elif point[1] > 5800 - radius:
        return False
    elif point[0] > 820 - radius and point[1] > 4950 - radius:
        return False
    elif point[0] > 2800 - radius and point[1] > -point[0] + 7750 - radius:
        return False
    return True

def quad(a,b,c):
    inside = (b**2) - (4*a*c)
    if inside < 0 or a == 0:
        return 0.1
    else:
        n = ((-b - math.sqrt(inside))/(2*a))
        p = ((-b + math.sqrt(inside))/(2*a))
        if p > n:
            return p
        return n

def future(ball,time):
    x = ball.location[0] + (ball.velocity[0] * time)
    y = ball.location[1] + (ball.velocity[1] * time)
    z = ball.location[2] + (ball.velocity[2] * time) - (325 * time * time)
    return Vector3(x,y,z)

def targetFuture(target,velocity,time):
    x = target[0] + (velocity[0] * time)
    y = target[1] + (velocity[1] * time)
    z = target[2] + (velocity[2] * time) - (325 * time * time)
    return Vector3(x,y,z)

def backsolveFuture(location,velocity,future,time):
    d = future-location
    dx = (2* ((d[0]/time)-velocity[0]))/time
    dy = (2* ((d[1]/time)-velocity[1]))/time
    dz = (2 * ((325*time)+((d[2]/time)-velocity[2])))/time
    return Vector3(dx,dy,dz)

def timeZ(ball):
    rate = 0.97
    return quad(-325, ball.velocity[2] * rate, ball.location[2]-92.75)

def futureZ(h,v,t):
    return h + v - (325 * t * t)

def dpp(target_loc,target_vel,our_loc,our_vel):
    target_loc = toLocation(target_loc)
    our_loc = toLocation(our_loc)
    our_vel = toLocation(our_vel)
    d = distance2D(target_loc,our_loc)
    if d != 0:
        return (((target_loc[0] - our_loc[0]) * (target_vel[0] - our_vel[0])) + ((target_loc[1] - our_loc[1]) * (target_vel[1] - our_vel[1])))/d
    else:
        return 0

def dpp3D(target_loc,target_vel,our_loc,our_vel):
    d = distance3D(target_loc,our_loc)
    if d!=0:
        return (((target_loc[0] - our_loc[0]) * (target_vel[0] - our_vel[0])) + ((target_loc[1] - our_loc[1]) * (target_vel[1] - our_vel[1])) + ((target_loc[2] - our_loc[2]) * (target_vel[2] - our_vel[2])))/d
    else:
        return 0

def to_local(target_object,our_object):
    x = (toLocation(target_object) - our_object.location).dot(our_object.matrix[0])
    y = (toLocation(target_object) - our_object.location).dot(our_object.matrix[1])
    z = (toLocation(target_object) - our_object.location).dot(our_object.matrix[2])
    return Vector3(x,y,z)

def rotator_to_matrix(our_object):
    r = our_object.rotation
    CR = math.cos(r[2])
    SR = math.sin(r[2])
    CP = math.cos(r[0])
    SP = math.sin(r[0])
    CY = math.cos(r[1])
    SY = math.sin(r[1])

    matrix = []
    matrix.append(Vector3(CP*CY, CP*SY, SP))
    matrix.append(Vector3(CY*SP*SR-CR*SY, SY*SP*SR+CR*CY, -CP * SR))
    matrix.append(Vector3(-CR*CY*SP-SR*SY, -CR*SY*SP+SR*CY, CP*CR))
    return matrix

def ballReady(agent):
    ball = agent.ball
    if abs(ball.velocity[2]) < 150 and timeZ(agent.ball) < 0.8:
        return True
    return False

def ballProject(agent):
    goal = Vector3(0,-sign(agent.team)*FIELD_LENGTH/2,100)
    goal_to_ball = (agent.ball.location - goal).normalize()
    difference = agent.me.location - agent.ball.location
    return difference.dot(goal_to_ball)
    
def side(x):
    if x <= 0:
        return -1
    return 1

def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def cap(x, low, high):
    if x < low:
        return low
    elif x > high:
        return high
    else:
        return x
    
def steer(angle):
    final = ((35 * angle)**3) / 20
    return cap(final,-1,1)

def steerPD(angle,rate):
    final = ((35*(angle+rate))**3)/20
    return cap(final,-1,1)

def throttle(speed, agent_speed):
    final = ((speed - agent_speed)/100)
    if final > 1.5:
        boost = True
    else:
        boost = False
    if final > 0 and speed > 1400:
        final = 1
    return cap(final,-1,1),boost
    

def angle2(target_location,object_location):
    difference = toLocation(target_location) - toLocation(object_location)
    return math.atan2(difference[1], difference[0])


def velocity2D(target_object):
    return math.sqrt(target_object.velocity[0]**2 + target_object.velocity[1]**2)

def velocity1D(target_object):
    x = target_object.velocity.dot( target_object.matrix[0])
    y = target_object.velocity.dot(target_object.matrix[1])
    z = target_object.velocity.dot(target_object.matrix[2])
    return Vector3(x,y,z)

def toLocal(target,our_object):
    if isinstance(target,obj):
        return target.local_location
    else:
        return to_local(target,our_object)

def toLocation(target):
    if isinstance(target,Vector3):
        return target
    elif isinstance(target,list):
        return Vector3(target)
    else:
        return target.location

def distance2D(target_object, our_object):
    difference = toLocation(target_object) - toLocation(our_object)
    return math.sqrt(difference[0]**2 + difference[1]**2)

def distance3D(target_object,our_object):
    difference = toLocation(target_object) - toLocation(our_object)
    return math.sqrt(difference[0]**2 + difference[1]**2 + difference[2]**2)

