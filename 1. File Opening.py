with open('file.txt', 'a+') as file:
    file.read()
    file.write('. My name is Naresh Singh Dhami and I am from Nepal. Working in Japan was my childhood dream and now I am living it to the fullest. \nHolding Bachelors degree from Kathmandu University.')
    file.close()
with open('file.txt', 'r') as file:
    print(file.read())
    print(file.tell())  #Location of the cursor after reading the sentence
    print(file.seek(0)) #Moves cursor at the start of the sentence or paragraph
