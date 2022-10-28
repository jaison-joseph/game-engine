from collections import deque

class WalkieTalkie:
    def __init__(self) -> None:
        self.messages = deque()

    def addMessage(self, msg):
        self.messages.append(msg)

    def getMessage(self):
        if not self.messages:
            return None
        return  self.messages.popleft()