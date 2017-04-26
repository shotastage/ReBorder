import uuid
import random
from main.models import GameSessionData

class SessionUtils():
    def genPass(self):
        a = str(random.randrange(10))
        b = str(random.randrange(10))
        c = str(random.randrange(10))
        d = str(random.randrange(10))

        return a + b + c + d

class GameSession():
    util = SessionUtils()

    def createSession(self):
        session_id = uuid.uuid4()
        session_enrollment_pass = self.util.genPass()

        session = GameSessionData(
            session_id = session_id,
            session_passwd = session_enrollment_pass,
            isEnable = True,
            isRevoked = False,
        )
        session.save()

        return (session_id, session_enrollment_pass)
