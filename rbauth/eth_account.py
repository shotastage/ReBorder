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
        output = str(cmd.before)
        cmd.close()


        start_index = 0
        end_index = 0
        default_index = 1

        for char in output:
            if char == "{":
                start_index = default_index
            elif char == "}":
                end_index = default_index - 1
            default_index = default_index + 1


        print(output[start_index:end_index])


# b' \r\nAddress: {37b65d8968ce826663ed6f6f0ba94a32981639a6}\r\n'
