class Vehicle:
    def __init__(self,top_speed,acceleration,wheels = 4):
        self.wheels = wheels
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.position = 0
        self.speed = 0
    
    def move(self):
        self.acceleration()
        self.position += self.speed

    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed

all_cars = {
"minivan":Vehicle(20,40),
"motorcycle":Vehicle(50,70,2),
"sport":Vehicle(40,60),
"truck" :Vehicle(30,50)
}

print("20 second run!")

for i in range(20):
    for car_name in all_cars:
        all_cars[car_name].move()

for car_name in all_cars:
    print(f"{car_name} -{all_cars[car_name].position}")