class SFCoinAccount:
    def get(self):
        print("Hello, world!")

    def detectSFCoinAcName(self, ethAccount):
        # number = "0xf3c986c3d8e2481b3be06ec195beb665f578dd78"
        n = []
        initName = str(int(ethAccount, 16))

        tmp = [(i+j) for (i,j) in zip(initName[::2],initName[1::2])]

        for i in tmp:
            n[i] = int(list(tmp[i])[0]) + int(list(tmp[i])[1])


#sfc = SFCoinAccount()

#print(sfc.detectSFCoinAcName("0xf3c986c3d8e2481b3be06ec195beb665f578dd78"))
