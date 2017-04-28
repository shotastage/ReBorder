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
        GameSessionData.objects.filter(session_id=session).update(isRevoked=True)

    def addMember(self, req, passwd):
        model = GameSessionData.objects.filter(session_passwd=passwd)
        existing_mem = model.members
        member = existing_mem + ',' + req.user.get_full_name()
        GameSessionData.objects.filter(sesssion_passwd=passwd).update(members=member)
