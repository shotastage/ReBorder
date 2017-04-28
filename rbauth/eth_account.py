import pexpect
import sys

class EthAccount():
    def createAccount(self, password):
        cmd = pexpect.spawn ('geth account new')
        cmd.expect ('Passphrase:')
        cmd.sendline ("password")
        cmd.expect('Repeat passphrase:')
        cmd.sendline ("password")
        cmd.expect( pexpect.EOF )
        cmd.close()
