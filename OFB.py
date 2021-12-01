import random
from joblib import Parallel, delayed
import myDES

class OFB:

    #Initialize with default values
    def __init__(self, blockSize=8, key=0, jobs=2):
        self.blockSize = blockSize
        self.key = key
        self.jobs = jobs
        self.DES = myDES.DESBase(key)        

    #Basic Skeleton for encryption        
    def encrypt(self, input):
        def loopBody(block, enNonce, cipherText):
            out = []
            for i in range(len(block)):
                out.append(block[i] ^ enNonce[i])
            cipherText += self._convertToString(out)
            #return out

        blocks = self._createBlocks(input)
        for i in range(len(blocks)):
            blocks[i] = self._convertToBytes(blocks[i])
        
        nonce = self._genNonce()
        lastNonce = nonce
        cipherText = ""
        enNonces = []
        #Create the ciphertext from the encrypted blocks
        for _ in range(len(blocks)):
            lastNonce = self.DES.encrypt(lastNonce, False)
            enNonces.append(lastNonce)
        #cipherBlocks = 
        Parallel(n_jobs = self.jobs)(delayed(loopBody)(blocks[i], enNonces[i], cipherText) for i in range(len(blocks)))

        #for each in cipherBlocks:
        #    cipherText += self._convertToString(each)
        return cipherText, nonce

    #Basic Skeleton for decryption     
    def decrypt(self, input, nonce):
        def loopBody(block, enNonce):
            out = []
            for i in range(len(block)):
                out.append(block[i] ^ enNonce[i])
            return out

        blocks = self._createBlocks(input)
        for i in range(len(blocks)):
            blocks[i] = self._convertToBytes(blocks[i])
        
        plainText = ""
        enNonces = []
        #Create the plain text from the decrypted blocks
        for _ in range(len(blocks)):
            nonce = self.DES.encrypt(nonce, False)
            enNonces.append(nonce)
        plainBlocks = Parallel(n_jobs = self.jobs)(delayed(loopBody)(blocks[i], enNonces[i]) for i in range(len(blocks)))

        for each in plainBlocks:
            plainText += self._convertToString(each)
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

    #Function to generate a random nonce  
    def _genNonce(self):
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
        
