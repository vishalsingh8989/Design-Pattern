import time

class Producer:
    """ Define the resource-intensive object instantiate"""
    def produce(self):
        print("Producer is working hard")
    
    def meet(self):
        print("Producer has time to meet you now!!")


class Proxy:
    """ Define the relatively less resource -intensive  proxy class"""
    
    def __init__(self):
        self.occupied = "No"
        self.producer = None
    
    def produce(self):
        """ check if producer is available 
        """
        
        print("Artist checking if producer is available")
        if self.occupied == "No":
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")


p = Proxy()

p.produce()

p.occupied = "Yes"
p.produce()
