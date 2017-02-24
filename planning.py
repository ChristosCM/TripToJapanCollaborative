import random

users = [n for n in range(1,21)]
travel = ["plane","train","boat","car"]
purpose = ["Studies","Leisure","Business","Sport"]
duration = [n for n in range(1,366)]
cost = [n for n in range(500,5000)]
group = [n for n in range(1,11)]

output = open("travel_data.txt", "w")

for passenger in users:
    count = 1
    u = passenger
    t = random.choice(travel)
    p = random.choice(purpose)
    d = random.choice(duration)
    c =random.choice(cost)
    g = random.choice(group)
    passenger = [u,t,p,d,c,g]
    count+= 1
    output.write(str(passenger))
    print passenger
    
output.close()

