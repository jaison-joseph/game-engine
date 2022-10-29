from collections import deque

'''
the walkieTalkie is an abstraction used for the sprites to 'neatly' communicate
with the Scene

a WalkieTalkie object maintains a queue of messages that any of the 
sprites as well as the scene can append/read from. 

theoretically the walkieTalkie can be used as a 2 way communication channel 
between the sprites and the Scene, but for the time being it is used 
as a 1 way channel just for any of the sprites to signal the scene to stop the main loop

the data structure used is a deque (https://docs.python.org/3/library/collections.html#collections.deque)
that is optimized for fast append/pop from either sides
'''
class WalkieTalkie:
    def __init__(self) -> None:
        self.messages = deque()

    '''
    add message to queue
    '''
    def addMessage(self, msg):
        self.messages.append(msg)

    '''
    returns None if the queue is empty, else returns the earliest message received by the walkieTalkie
    '''
    def getMessage(self):
        if not self.messages:
            return None
        return  self.messages.popleft()