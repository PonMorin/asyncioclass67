# extending the Thread class
from time import sleep, ctime
from threading import Thread

# custome thread class
class CustomeThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print(f'{ctime()} This is coming from another thread')

# create the thread
thread = CustomeThread()
# start the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thread.join()