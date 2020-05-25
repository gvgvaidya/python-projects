#capitalise sentence and if the sentence is a itorogetive adds a question mark
def sent_maker(phrase):
    capitalised=phrase.capitalize()

    intorogative= ("how",'when',"why",'what','who')
    if  phrase.startswith(intorogative):
        phrase = f"{capitalised}?"
    else:
        phrase=f"{capitalised}."
    return phrase
#to print all user input together append all inputs in a list
lis=[]

print('hey this is just a sample\n')
print("_________________________________________________________________________________________________________________________")
print("talk to me                                                    *to end the conversation please type \end")
#main loop
while True:
    user = input("say something:")
    if user == '\end':
         break
    else:

        convert=sent_maker(user)
        lis.append(convert)
print("\n".join(lis))