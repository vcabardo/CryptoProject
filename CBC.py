import random
import myDES

class CBC:

    def __init__(self, blockSize=8, key=0):
        self.blockSize = blockSize
        self.key = key
        self.DES = myDES.DESBase(key)
        
    def encrypt(self, input):
        blocks = self._createBlocks(input)
        for i in range(len(blocks)):
            blocks[i] = self._convertToBytes(blocks[i])

        IV = self._genIV()
        enBlock = IV
        cipherText = ""
        
        for block in blocks:
            for i in range(len(block)):
                block[i] = block[i] ^ enBlock[i]
            block = self.DES.encrypt(block, False)
            enBlock = block
            cipherText +=self._convertToString(block)
        return cipherText,IV

    def decrypt(self, input, IV):
        blocks = self._createBlocks(input)
        for i in range(len(blocks)):
            blocks[i] = self._convertToBytes(blocks[i])
        plainText = ""
        for block in blocks:
            enBlock = block
            block = self.DES.encrypt(block, True)
            for i in range(len(block)):
                block[i] = block[i] ^ IV[i]
            IV = enBlock
            plainText += self._convertToString(block)
        return plainText
        
    def _createBlocks(self, input):
        i = 0
        output = []
        while (i+self.blockSize) < len(input):
            output.append(input[i:i+self.blockSize])
            i += self.blockSize
        while (len(input) - i) <self.blockSize:
            input += chr(0)
        output.append(input[i:i+self.blockSize])
        return output
 
    def _genIV(self):
        output = []
        for i in range(self.blockSize):
            output.append(random.randint(0,255))
        return output

    def _convertToBytes(self, block):
        newBlock = []
        for each in block:
            newBlock.append(ord(each))
        return newBlock

    def _convertToString(self, block):
        newBlock = ""
        for each in block:
            newBlock+=chr(each)
        return newBlock

