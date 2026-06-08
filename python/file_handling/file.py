# with open ('file_handling/demo.txt','r') as f:
#     print(f.read()) 
# create a file and write some line
with open ('file_handling/demo.txt','w') as f:
    f.writelines(['hello this is me \n','answer the question\n','this file created in python\n'])
    print('File created succesfully')

# count number of lines in a file 
with open ('file_handling/demo.txt','r') as file:
    count=file.readline()
print('Total number of lines:',len(count))    
# convert file cotent (character) to uppercase

with  open('file_handling/demo.txt','r') as file1:
    content=file1.read()
    uppercase_co=content.upper()
print(uppercase_co)
with open('file_handling/demo.txt','w') as file1:
        file1.write(uppercase_co)

print('File cotent converted to uppercase sucessfully')        

# reverse file content
with open ('file_handling/demo.txt','r') as file2:
    content_1=file2.read()
reverse=content_1[::-1]
print(reverse)

with open('file_handling/reverse_s.txt','w') as file2:
    file2.write(reverse)
print('file content reverse')    

# read file line by line in reverse