initial_velocity = 0
t = int(input("time spent on road"))
a = int(input("acceleration"))
d = int(input("distance travelled"))
speed_limit = 60

for i in range (0, t + 1):
    print("*" * int((0.5*a*i*i)/10))
    velocity = a * i
if velocity < 60:
    print("The person did not go over the speed limit")
else:
    print("The person went over the speed limit")

s = 0.5*a*t*t
s = int(s)
if s >= d:
    print("The person reached the destination")
else:
    print("The person did not reach the destination")

