# --------------
##File path for the file 
file_path
def read_file(path):
    file = open(path, "r") 
    sentence = file.readline() 
    file.close()
    return sentence
#Code starts here
sample_message = read_file(file_path)


# --------------
#Code starts here
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

def fuse_msg(message_a,message_b):
    quotient = (int(message_b)//int(message_a))
    return str(quotient)

secret_msg_1 = fuse_msg(message_1,message_2)    




# --------------
#Code starts here
message_3 = read_file(file_path_3)
print(message_3)
def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    if message_c == 'Green':
        sub = 'Data Scientist'    
    if message_c == 'Blue':
        sub = 'Marine Biologist'    
    return sub
secret_msg_2 = substitute_msg(message_3)        


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list=message_d.split()
    
    #Splitting the message into a list
    b_list=message_e.split()
    
    #Comparing the elements from both the lists
    c_list = [i for i in a_list if i not in b_list]
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(c_list)
    
    #Returning the sentence
    return final_msg


#Calling the function to read file
message_4=read_file(file_path_4)

#Calling the function to read file
message_5=read_file(file_path_5)

#Calling the function 'compare messages'
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)

#Code ends here


# --------------
#Code starts here
message_6 = read_file(file_path_6)

def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x: (len(x)%2==0)
    b_list = filter(even_word,a_list)    
    final_msg = " ".join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)  
print(secret_msg_4)  


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg = " ".join(message_parts)


final_path= user_data_dir + '/secret_message.txt'
def write_file(secret_msg,path):
    f=open(path,"a+")
    f.write(secret_msg)
    f.close()

#Code starts here
write_file(secret_msg,final_path)


