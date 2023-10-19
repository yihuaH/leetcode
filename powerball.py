import random
win_blue_number = [22,24,40,52,64]
win_red_number = 10

win = False
my_blueballs = []
my_blueball = random.randint(1,70)
    
    
def new_lottery():
    blueball = random.sample(range(1,70), 5)         
    redball = random.randint(1,26)
    blueball.sort()
    blueball.append(redball)
    return blueball


with open('powerball.txt', 'a') as f:
    count = 0
    my_blueballs = []
    my_blueball = random.randint(1,70)
    while len(my_blueballs)!= 5:
        if count % 1000000 == 0:
            print(count)
        if len(my_blueballs) == 0:
            my_redball = random.randint(1,26)
            if my_redball != win_red_number:
                count += 1
                continue
        my_blueball = random.randint(1,70)
        while my_blueball in my_blueballs:
            my_blueball = random.randint(1,70)
        if my_blueball in win_blue_number:
            my_blueballs.append(my_blueball)
        else:
            my_blueballs = []
            count += 1
            continue
        
    print("OK, you got it {}".format(count))
    f.write("OK, you got it! {}\n".format(count))
    print(my_blueballs)
    print(my_redball)