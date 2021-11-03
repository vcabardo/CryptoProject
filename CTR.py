import random
from joblib import Parallel, delayed

class CTR:

    #Initialize with default values
    def __init__(self, blockSize=1024, key=0, jobs=2):
        self.blockSize = blockSize
        self.key = key
	self.jobs = jobs

    #Basic Skeleton for encryption        
    def encrypt(self, input):
	def loopBody(self, input, CTR):
           #CTR = encrypt(CTR)
	   #XOR CTR with the plain text
	   #return the cipher text block

        blocks = self._createBlocks(input)
        CTR = self._genCTR()
        cipherText = ""
        #Create the ciphertext from the encrypted blocks
        cipherBlocks = Parallel(n_jobs = self.jobs)(delayed(loopBody)(blocks[i], CTR+i) for i in range(len(blocks))
        for each in cipherBlocks:
	    cipherText += each

        return cipherText

    #Basic Skeleton for decryption     
    def decrypt(self, input, CTR):
	def loopBody(self, input, CTR):
           #CTR = encrypt(CTR)
	   #XOR CTR with the cipher text
	   #return the plain text block

        blocks = self._createBlocks(input)
        plainText = ""
        #Create the plain text from the decrypted blocks
        plainBlocks = Parallel(n_jobs = self.jobs)(delayed(loopBody)(blocks[i], CTR+i) for i in range(len(blocks))

        for each in plainBlocks:
	    plainText += each
        return plainText

    #Function to extract blocks from a string input        
    def _createBlocks(input):
        i = 0
        output = []
	#Split up the text up until the last block
        while (i+1024) < len(input):
            output.append(input[i:i+self.blockSize])
            i += self.blockSize
	#Check if last block requires any padding
        while (len(input) - i) <1024:
            input += char(0)
        output.append(input[i:i+self.blockSize])
        return output

    #Function to generate a random nonce  
    def _genCTR():
        output = ""
        for i in range(blockSize):
            output += char(random.randint(0,127))
        return output
