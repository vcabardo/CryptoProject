class DESBase():
    
    #Iniltialize global table
    # permuted choice (table 1)
    __pc1 = [
        56, 48, 40, 32, 24, 16, 8,
        0, 57, 49, 41, 33, 25, 17,
        9,  1, 58, 50, 42, 34, 26,
        18, 10,  2, 59, 51, 43, 35,
        62, 54, 46, 38, 30, 22, 14,
        6, 61, 53, 45, 37, 29, 21,
        13,  5, 60, 52, 44, 36, 28,
        20, 12,  4, 27, 19, 11,  3
        ]
    #Number of left shifts
    __leftShifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    # permuted choice (table 2)
    __pc2 = [   13, 16, 10, 23,  0,  4,
		 2, 27, 14,  5, 20,  9,
		22, 18, 11,  3, 25,  7,
		15,  6, 26, 19, 12,  1,
		40, 51, 30, 36, 46, 54,
		29, 39, 50, 44, 32, 47,
		43, 48, 38, 55, 33, 52,
		45, 41, 49, 35, 28, 31 ]

    # initial permutation table IP
    __ip = [    57, 49, 41, 33, 25, 17, 9,  1,
		59, 51, 43, 35, 27, 19, 11, 3,
		61, 53, 45, 37, 29, 21, 13, 5,
		63, 55, 47, 39, 31, 23, 15, 7,
		56, 48, 40, 32, 24, 16, 8,  0,
		58, 50, 42, 34, 26, 18, 10, 2,
		60, 52, 44, 36, 28, 20, 12, 4,
		62, 54, 46, 38, 30, 22, 14, 6 ]

    # expansion table IP
    __expand = [31,  0,  1,  2,  3,  4,
		 3,  4,  5,  6,  7,  8,
		 7,  8,  9, 10, 11, 12,
		11, 12, 13, 14, 15, 16,
		15, 16, 17, 18, 19, 20,
		19, 20, 21, 22, 23, 24,
		23, 24, 25, 26, 27, 28,
		27, 28, 29, 30, 31,  0	]
    
    # S-boxes
    __sboxes = [
		# S1
		[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
		 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
		 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
		 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

		# S2
		[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
		 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
		 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
		 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

		# S3
		[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
		 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
		 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
		 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

		# S4
		[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
		 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
		 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
		 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

		# S5
		[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
		 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
		 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
		 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

		# S6
		[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
		 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
		 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
		 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

		# S7
		[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
		 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
		 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
		 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

		# S8
		[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
		 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
		 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
		 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
            ]

    # permutation function P used S-box output
    __p = [ 15,  6, 19, 20, 
            28, 11, 27, 16,
             0, 14, 22, 25,
	     4, 17, 30,  9, 
              1, 7, 23, 13, 
             31, 26, 2,  8,
             18, 12, 29, 5, 
             21, 10,  3, 24 ]

    # final permutation
    __fp = [39,  7, 47, 15, 55, 23, 63, 31,
		38,  6, 46, 14, 54, 22, 62, 30,
		37,  5, 45, 13, 53, 21, 61, 29,
		36,  4, 44, 12, 52, 20, 60, 28,
		35,  3, 43, 11, 51, 19, 59, 27,
		34,  2, 42, 10, 50, 18, 58, 26,
		33,  1, 41,  9, 49, 17, 57, 25,
		32,  0, 40,  8, 48, 16, 56, 24]
    
    #Intilize with key with 8 bytes
    def __init__(self, key):
        if len(key) != 8:
            print("Key is not the correct size, needs to be 8 bytes")
            exit()
	#Convert from bytes to bits then generate subkeys
        self.k = self.bytesToBits(key)
        self.subK = self.subKeyGeneration(self.k)
        
    #DES subkey generation implementation 
    def subKeyGeneration(self, key):
        baseKey = []
	#Pass through permuted choice table 1
        for index in self.__pc1:
            baseKey.append(key[index])

        subkeys = []
	#Create the 16 subkeys for encryption
        for i in range(16):
	    #Shift based on table value
            shifts = self.__leftShifts[i]
            subkeys.append([])
            #Left side of key
            for index in range(28):
                subkeys[i].append(baseKey[(index+shifts)%28])
            #Right side of key
            for index in range(28):
                subkeys[i].append(baseKey[((index+shifts)%28)+28])
            #Set base for permuation and next shift
            baseKey = subkeys[i]
            subkeys[i] = [] 
            #Final  permutaion
            for index in self.__pc2:
                subkeys[i].append(baseKey[index])

        return subkeys
    
    #Utility function to convert bytes to bits
    def bytesToBits(self, byts):
        bits = []
        for byte in byts:
            bits += self.get8Bits(byte)
        return bits
        
    #Returns 8 bit rep of a byte
    def get8Bits(self, byte):
        strB = format(byte, "08b")
        ret = []
        for i in range(len(strB)):
            ret.append(int(strB[i]))
        return ret
       
    #Convert bits to bytes
    def bitsToBytes(self, bits):
        byts = []
        val = 0
        for i in range(len(bits)):
            val += (pow(2, 7- i%8) * bits[i])
            if (i+1) % 8 == 0:
                byts.append(val)
                val = 0
        return byts
        
    #Encryption algorithm 
    def encrypt(self, block, decrypt):
        if len(block) != 8:
            print("Block is not the correct size, needs to be 8 bytes")    
            exit()
	#Convert from bytes to bits in order to process permutation
        bits = self.bytesToBits(block)
        permBits = []

	#Pass through the initial permutation
        for index in self.__ip:
            permBits.append(bits[index])  
	#Convert from bits to bytes for simple computations
        permBlock = self.bitsToBytes(permBits)
	
	#Split into left and right
        left = permBlock[:4]
        right = permBlock[4:]
	#Begin the 16 rounds
        for i in range(16):
            subKey = self.subK[i]
	    #If decryption use key in reverese order
            if(decrypt):
                subKey = self.subK[15-i]
            temp = left
            left = right
	    #Call round function then XOR
            right = self.roundFunction(right, subKey)
            for k in range(len(right)):
                right[k] = right[k] ^ temp[k]
	#Combine blocks together and convert from bytes to bits for final permutation
        permBlock = right + left
        permBits = self.bytesToBits(permBlock)
        finalBits = []
        for index in self.__fp:
            finalBits.append(permBits[index]) 
	#After permutation convert back to bytes for return value
        return self.bitsToBytes(finalBits)

    #DES round function
    def roundFunction(self, block, key):
	#Convert to bits inorder to run values through the tables
        bits = self.bytesToBits(block)
        #Expand bits
        exBits = []
        for index in self.__expand:
            exBits.append(bits[index])         
        #XOR bits, convert to bytes for XOR, then go back to bits
        keyBlock = self.bitsToBytes(key)
        exBlock = self.bitsToBytes(exBits)
        for i in range(len(exBlock)):
            exBlock[i] = exBlock[i] ^ keyBlock[i]
        
        exBits = self.bytesToBits(exBlock)
        #Sbox conversion
        sBits = []
        for i in range(8):
            shift = i*6
            sBits += self.sBoxConv(self.__sboxes[i], exBits[(shift+0):(shift+6)])
        
        #Permutation 
        finalBits = []
        for index in self.__p:
            finalBits.append(sBits[index])
	#Return the value in bytes
        return self.bitsToBytes(finalBits)
    
    #Simple function for performing sBox conversions, using given tables
    def sBoxConv(self, sBox, bits):
        row = 2*bits[0]+1*bits[5]
        col = 8*bits[1]+4*bits[2]+2*bits[3]+1*bits[4]
        index = col + row*16
        return self.get8Bits(sBox[index])[4:]
