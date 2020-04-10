class TVSwasta:  # template

    def __init__(self, inputNama, inputChannel, inputType):
        self.Nama = inputNama
        self.Channel = inputChannel
        self.Type = inputType


TVSwasta1 = TVSwasta("Indosiar", 90, "Stereo")
TVSwasta2 = TVSwasta("RCTI", 85, "Zweiton")
TVSwasta3 = TVSwasta("SCTV", 44, "Stereo")

print(TVSwasta1.__dict__)
print(TVSwasta2.__dict__)
print(TVSwasta3.__dict__)