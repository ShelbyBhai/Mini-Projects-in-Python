from textblob import TextBlob

_input_file = open("roughinput.txt", "r+")

test = _input_file.read()

new = TextBlob(test)

print("Given text was: "+str(_input_file))

print("Corrected text is: "+str(new.correct()))

_input_file.close()

_output_file = open("CorrectedVersion.txt", "w")

_output_file.write(str(new.correct()))

_output_file.close()

