# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# share resources
import multiprocessing
import os
from time import sleep, ctime, time

# Basket of sharing
class Basket:
    def __init__(self) -> None:
        self.egg = 50
    
    def use_egg(self, index):
        print(f"{ctime()} Kitchen-{index}   : Chef-{index} has lock with eggs remaining {self.egg}")
        self.egg -= 1
        print(f"{ctime()} Kitchen-{index}   : Chef-{index} has released lock with eggs remaining {self.egg}")        

def cooking(index, basket):
     # chef use eggs for cooking
    basket.use_egg(index)
    sleep(2)

def kitchen(index, share_eggs):
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index}   : Begin cooking...PID {os.getpid()}')
    cooking_time = time()
    cooking(index, share_eggs)
    duration = time() - cooking_time 
    print(f'{ctime()} Kitchen-{index}   : Cooking done in {duration:0.2f} second!')


if __name__ == "__main__":
    # Begin of  main thread
    print(f'{ctime()} Main  : Start Cooking...PID {os.getpid()}')
    start_time = time()

    basket = Basket()

    # Multi kitchens with each chef
    kitchens = list()
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index, basket ))
        kitchens.append(p)
        # starting process
        p.start()

    for index, p in enumerate(kitchens):
        # wait until processes are finished
        p.join()

    
    print(f"{ctime()} Main      : Basket eggs remaining {basket.egg}")
    duration = time() - start_time
    print(f"{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds")