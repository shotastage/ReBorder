""" Registering Data Validater """
class Validation():

    """ Methods of checking registering data. """
    def overflow(self, value):
        """ Check overflow """
        for i in value:
            status = len(i) > 150
        return status

    def empty(self, value):
        for i in value:
            if len(i) == 0:
                return True
                break
            else:
                return False

    def email(self, value):
        """ Valid E-mail adress"""
        # Temporary avoid
        return False

    def password(self, passwd):
        """ Check password size """
        if len(passwd) < 8:
            return True
        else:
            return False
