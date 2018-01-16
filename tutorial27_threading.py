# two different programs are running at the same time
import threading

class BuckysMessenger(threading.Thread):
    def run(self):  # when a thread is created, the function will be called
        for _ in range(10): # _ means the code will loop times without caring the values
            print(threading.currentThread().getName())

# Create threads
x = BuckysMessenger(name='Send out message')
y = BuckysMessenger(name = 'Receive messages')
x.start()   # to find the Run() function and kick off the thread
y.start()   # thread y will start without waiting for thread x finish
