x = int(input("enter number: "))
y = int(input("enter number: "))
z = int(input("enter number: "))
ans=(x,y,z)
print(max(ans))


def loop(x):
    for i in range(i, x+1, 1):
        print(i);

loop(x=int(input("enter number: ")))  
loop(y=int(input("enter number: ")))
loop(z=int(input("enter number: ")))   

sq = lambda s : s*s
print(sq(s))

class car:
    def run(self):
        print('car runs')

class honda(car):
    def stop(self):
        print('honda stops')

my_car = honda()                