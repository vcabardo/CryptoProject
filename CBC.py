import random
import myDES

class CBC:

    #Initialize with default values
    def __init__(self, blockSize=8, key=0):
        self.blockSize = blockSize
        self.key = key
        self.DES = myDES.DESBase(key)

    #Encryption process       
    def encrypt(self, input):
      
        #Create the blocks, and convert from string to bytes
        blocks = self._createBlocks(input)
        for i in range(len(blocks)):
            blocks[i] = self._convertToBytes(blocks[i])

        IV = self._genIV()
        enBlock = IV
        cipherText = ""
       
        #Create the ciphertext from the encrypted blocks
        #XOR, and the encrypt with DES
        for block in blocks:
            for i in range(len(block)):
                block[i] = block[i] ^ enBlock[i]
            block = self.DES.encrypt(block, False)
            enBlock = block
            #Convert from string to bytes
            cipherText +=self._convertToString(block)
        return cipherText,IV

    #Encryption process       
    def decrypt(self, input, IV):
        #Create the blocks, and convert from string to bytes
        blocks = self._createBlocks(input)
        for i in range(len(blocks)):
            blocks[i] = self._convertToBytes(blocks[i])
        plainText = ""
        #Create the plain text from the decrypted blocks
        #Encrypt with DES then XOR
        for block in blocks:
            enBlock = block
            block = self.DES.encrypt(block, True)
            for i in range(len(block)):
                block[i] = block[i] ^ IV[i]
            IV = enBlock
            #Convert from string to bytes
            plainText += self._convertToString(block)
        return plainText

    #Function to extract blocks from a string input
    def _createBlocks(self, input):
        i = 0
        output = []
        #Split up the text up until the last block
        while (i+self.blockSize) < len(input):
            output.append(input[i:i+self.blockSize])
            i += self.blockSize
        #Check if last block requires any padding
        while (len(input) - i) <self.blockSize:
            input += chr(0)
        output.append(input[i:i+self.blockSize])
        return output

    #Function to generate a random IV  
    def _genIV(self):
        output = []
        for i in range(self.blockSize):
            output.append(random.randint(0,255))
        return output

    #Convert a block from a string to a list of bytes
    def _convertToBytes(self, block):
        newBlock = []
        for each in block:
            newBlock.append(ord(each))
        return newBlock

    #Convert a block from a list of bytes to a string
    def _convertToString(self, block):
        newBlock = ""
        for each in block:
            newBlock+=chr(each)
        return newBlock

