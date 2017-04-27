from .models import GameSessionData
from django.db import models

import uuid
import random


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
            isRevoked = False,
        )
        session.save()

        return (session_id, session_enrollment_pass)


    def revokeSession(self, session):
        print("THISs")
        print(session)
        revoking_session = GameSessionData.objects.filter(session_id=session).update(isRevoked=True)
