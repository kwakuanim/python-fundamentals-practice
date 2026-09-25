##Write information into a file

with open ('Learning_log.txt', 'w', encoding= 'utf-8') as file:
     file.write('I am learning Python.\n')
     file.write('My goal is to apply data science to biomedical research.\n')
     print('The file was successfully created.')


##Read information into a file
with open ('Learning_log.txt', 'r', encoding= 'utf-8') as file:
     content = file.read()
     print('\nContents of learning_log.txt:')
     print(content)

###Append new information
with open ('Learning_log.txt', 'a', encoding= 'utf-8') as file:
     file.write('Today I am practicing writing and reading fil.\n')

print('New information added successfully.')

##Read the file line by line
with open('Learning_log.txt', 'r', encoding='utf-8') as file:
       for line_number, line in enumerate (file, start=1):
           print(f'line {line_number}: {line.strip()}')
