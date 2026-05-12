#leaky bucket algoritm 
import time

class Leak:
    def __init__(self,capacity,rate):
        self.bucket=capacity
        self.current_water=0
        self.last_check=time.time()
        self.rate=rate

    def leakage(self):
        now=time.time()
        #time in between
        elapsed=now-self.last_check
        #how much has leaked 
        leaked_amount=elapsed*self.rate
        #max(0,)cancels out negative 
        self.current_water=max(0, self.current_water - leaked_amount)
        self.last_check=now

    def allow_request(self):
        self.leakage()
        if self.current_water <self.bucket:
            self.current_water+=1
            return True
        
        return False



bucket=Leak(capacity=5,rate=1)
for i in range(10):
    if bucket.allow_request():
        print(f"request:{i+1}:accepted ")
    else:
        print(f"request:{i+1}:rejected ")
    time.sleep(0.2)
    
