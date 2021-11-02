import random

class CBC:

    def __init__(self, blockSize=1024, key=0):
        self.blockSize = blockSize
        self.key = key
        
    def encrypt(self, input):
        blocks = self._createBlocks(input)
        IV = self._genIV()
        cipherText = ""
        for block in blocks:
            #XOR block with IV
            #EncryptBlock
            #IV = enBlock
            #cipherText += enBlock
        return cipherText

    def decrypt(self, input, IV):
        blocks = self._createBlocks(input)
        plainText = ""
        for block in blocks:
            #DecryptBlock
            #IV = deBlock
            #XOR block with IV
            #plainText += deBlock
        return plainText
        
    def _createBlocks(input):
        i = 0
        output = []
        while (i+1024) < len(input):
            output.append(input[i:i+self.blockSize])
            i += self.blockSize
        while (len(input) - i) <1024:
            input += char(0)
        output.append(input[i:i+self.blockSize])
        return output
 
    def _genIV():
        output = ""
        for i in range(blockSize):
            output += char(random.randint(0,127))
        return output
