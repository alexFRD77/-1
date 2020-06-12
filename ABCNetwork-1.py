import markovify
ABCtext = open('Biden2020.txt', "r")
# Build the model.
text_model = markovify.Text(ABCtext, state_size=1)
# Print five randomly-generated sentences
print("write the name of the song name")
TT=""
# Uncomment this if you want to name your song
#TT = input()
ThePower = TT + "\n"
for i in range(10):
    C=text_model.make_sentence(tries=100)
    ThePower=ThePower+C+" \n"
    print(C)
BLDNM = open("Dementia_Hello.txt", "w")
BLDNM.write(ThePower)
BLDNM.close()
ABCtext.close()
#  ^\ no sence (of music should I have to make such crap)
# P.C. 44 of cource