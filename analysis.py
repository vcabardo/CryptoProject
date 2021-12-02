#Program for obtaining metrics for the performance of the
#CBC, OFB, and CTR Modes of Encryption
import matplotlib.pyplot as plt
import time
import string
import random
from random import randrange
import CBC
import OFB
import CTR

cbc_ciphertext = ""
ofb_ciphertext = ""
ctr_ciphertext = ""

encrypt_y_cbc = []
encrypt_y_ofb = []
encrypt_y_ctr = []

decrypt_y_cbc = []
decrypt_y_ofb = []
decrypt_y_ctr = []

cbc_encryption_elapsed_time = 0
cbc_decryption_elapsed_time = 0
ofb_encryption_elapsed_time = 0
ofb_decryption_elapsed_time = 0
ctr_encryption_elapsed_time = 0
ctr_decryption_elapsed_time = 0

num_blocks = [1, 2, 3, 4, 5, 6, 7, 8]
num_runs = 5

for i in range(8):
    #create a plaintext message with a size that gets larger with each iteration
    str = ''.join(random.choice(string.ascii_uppercase + string.digits) for j in range(1024 * (i + 1)))
    key = [randrange(255), randrange(255), randrange(255), randrange(255), randrange(255), randrange(255), randrange(255), randrange(255)]

    ###################################################
    #time the CBC encryption operation
    for j in range(num_runs):
        start = time.time()

        CBC_object = CBC.CBC(8, key);
        ciphertext, iv = CBC_object.encrypt(str)

        end = time.time();
        cbc_encryption_elapsed_time += (end - start) / num_runs;

        #time the CBC decryption operation
        start = time.time()

        plaintext = CBC_object.decrypt(ciphertext, iv)

        end = time.time();
        cbc_decryption_elapsed_time += (end - start) / num_runs;

    encrypt_y_cbc.append(cbc_encryption_elapsed_time)
    decrypt_y_cbc.append(cbc_decryption_elapsed_time)

    ###################################################

    #time the OFB encryption operation
    for j in range(num_runs):
        start = time.time()

        OFB_object = OFB.OFB(8, key, 4);
        ciphertext, iv = OFB_object.encrypt(str)

        end = time.time();
        ofb_encryption_elapsed_time += (end - start) / num_runs;

        #time the OFB decryption operation
        start = time.time()

        plaintext = OFB_object.decrypt(ciphertext, iv)

        end = time.time();
        ofb_decryption_elapsed_time += (end - start) / num_runs;

    encrypt_y_ofb.append(ofb_encryption_elapsed_time)
    decrypt_y_ofb.append(ofb_decryption_elapsed_time)

    ###################################################

    #time the CTR encryption operation
    for j in range(num_runs):
        start = time.time()

        CTR_object = CTR.CTR(8, key, 4);
        ciphertext, iv = CTR_object.encrypt(str)

        end = time.time();
        ctr_encryption_elapsed_time += (end - start) / num_runs;

        #time the CTR decryption operation
        start = time.time()

        plaintext = CTR_object.decrypt(ciphertext, iv)

        end = time.time();
        ctr_decryption_elapsed_time += (end - start) / num_runs;

    encrypt_y_ctr.append(ctr_encryption_elapsed_time)
    decrypt_y_ctr.append(ctr_decryption_elapsed_time)

    ###################################################


#graph code obtained from https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
encryption_graph = plt.figure(1);

# plotting the points
plt.plot(num_blocks, encrypt_y_cbc, label = "CBC Mode")
plt.plot(num_blocks, encrypt_y_ofb, label = "OFB Mode")
plt.plot(num_blocks, encrypt_y_ctr, label = "CTR Mode")

# naming the x axis
plt.ylabel('Time Taken For Operation (Seconds)')
# naming the y axis
plt.xlabel('Size of Input (kB)')

# giving a title to my graph
plt.title('Performance Comparisons of Encryption in CBC, OFB, and CTR Modes')


decryption_graph = plt.figure(2);

# plotting the points
plt.plot(num_blocks, decrypt_y_cbc, label = "CBC Mode")
plt.plot(num_blocks, decrypt_y_ofb, label = "OFB Mode")
plt.plot(num_blocks, decrypt_y_ctr, label = "CTR Mode")

# naming the x axis
plt.ylabel('Time Taken For Operation (Seconds)')
# naming the y axis
plt.xlabel('Size of Input (kB)')

# giving a title to my graph
plt.title('Performance Comparisons of Decryption in CBC, OFB, and CTR Modes')

encryption_graph.legend(loc="lower right")
decryption_graph.legend(loc="lower right")
# function to show the plots
plt.show()
