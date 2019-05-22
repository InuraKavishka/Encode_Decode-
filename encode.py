alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def main():
    check = True
    while check:
        prompt=str(input('please enter\n e to encode :\n d to decode :\n q to quit   :\n ==>'))    
        if prompt=='e':                                                                 #when input e programe go throught the encodeword
            encode_text()#calling function for encoding
                
        elif prompt=='d':
            decode_text()#calling function for decoding
            
        elif prompt=='q':
            print('thank you!')
            check = False
        else :
            print ('Incorrect Input')
#hello
def encode_text():
    #global makes these variable global that means can access any where
    global encodeword
    global skipword
    global secret
    global check2
    encodeword=str(input("Enter your word:"))                                   
    try:                                                                        #when entered encodeword  
        skipword = int(input("Enter a value between 1-25 :"))
        if skipword<=26 :
            secret=('')
            for i in range(len(encodeword)):
                check2=False
                for j in range(len(alphabet)):
                    if encodeword[i]==alphabet[j]:
                        check2=True
                        secret=secret + (alphabet[(j + skipword)%26])
                if check2==False:
                    secret=secret + encodeword[i]
            print("ENCODED MESSAGE IS :",secret)
        else:
            print('invalid input please enter again')
    except ValueError:
        print("you Entered value invalid")
        return#makes go out of the function

            
def decode_text():
    global decodeword
    global skipword
    global secret
    global check3
    global prompt
    decodeword=str(input("Enter your word:"))
    try:
        skipword = int(input("Enter a value between 1-25 :"))
        if skipword<=26:
            secret=('')
            for i in range(len(decodeword)):
                check3=False
                for j in range(len(alphabet)):
                    if decodeword[i]==alphabet[j]:
                        check3=True 
                        secret=secret + (alphabet[(j - skipword)%26])
                if check3==False:
                    secret=secret + decodeword[i]
            print(secret)
        else:
            print('invalid input please enter again')
    except ValueError:
        print("you Entered value invalid")
        return
   

main()
