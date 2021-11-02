#Program for obtaining metrics for the performance of the
#CBC, OFB, and CTR Modes of Encryption
import matplotlib.pyplot as plt
import time

cbc_ciphertext = ""
ofb_ciphertext = ""
ctr_ciphertext = ""

encrypt_y_cbc = []
encrypt_y_ofb = []
encrypt_y_ctr = []

decrypt_y_cbc = []
decrypt_y_ofb = []
decrypt_y_ctr = []

#subject to change when we decide how large the inputs should be
num_blocks = [1, 2, 4, 8, 16, 32, 64, 128]

for i in range(8):
    #create a plaintext message with a size that gets larger with each iteration

    #time the CBC encryption operation
    start = time.time()

    #CBC encryption goes here

    end = time.time();
    cbc_encryption_elapsed_time = end - start;
    encrypt_y_cbc.append(cbc_encryption_elapsed_time)

    #time the CBC decryption operation
    start = time.time()

    #CBC decryption goes here

    end = time.time();
    cbc_decryption_elapsed_time = end - start;
    decrypt_y_cbc.append(cbc_decryption_elapsed_time)

    #time the OFB encryption operation
    start = time.time()

    #OFB encryption goes here

    end = time.time();
    ofb_encryption_elapsed_time = end - start;
    encrypt_y_ofb.append(ofb_encryption_elapsed_time)

    #time the OFB decryption operation
    start = time.time()

    #OFB decryption goes here

    end = time.time();
    ofb_decryption_elapsed_time = end - start;
    decrypt_y_ofb.append(ofb_decryption_elapsed_time)

    #time the CTR encryption operation
    start = time.time()

    #CTR encryption goes here

    end = time.time();
    ctr_encryption_elapsed_time = end - start;
    encrypt_y_ctr.append(ctr_encryption_elapsed_time)

    #time the CTR decryption operation
    start = time.time()

    #CTR decryption goes here

    end = time.time();
    ctr_decryption_elapsed_time = end - start;
    decrypt_y_ctr.append(ctr_decryption_elapsed_time)


#graph code obtained from https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
encryption_graph = plt.figure(1);

# plotting the points
plt.plot(num_blocks, encrypt_y_cbc, label = "CBC Mode")
plt.plot(num_blocks, encrypt_y_ofb, label = "OFB Mode")
plt.plot(num_blocks, encrypt_y_ctr, label = "CTR Mode")

# naming the x axis
plt.ylabel('Speed of Operation (Seconds)')
# naming the y axis
plt.xlabel('Size of Input')

# giving a title to my graph
plt.title('Performance Comparisons of Encryption in CBC, OFB, and CTR Modes')


decryption_graph = plt.figure(2);

# plotting the points
plt.plot(num_blocks, decrypt_y_cbc, label = "CBC Mode")
plt.plot(num_blocks, decrypt_y_ofb, label = "OFB Mode")
plt.plot(num_blocks, decrypt_y_ctr, label = "CTR Mode")

# naming the x axis
plt.ylabel('Speed of Operation (Seconds)')
# naming the y axis
plt.xlabel('Size of Input')

# giving a title to my graph
plt.title('Performance Comparisons of Decryption in CBC, OFB, and CTR Modes')

# function to show the plots
plt.show()
