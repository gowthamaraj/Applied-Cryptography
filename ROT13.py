Alphabet  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

text = input("Enter the text : ");
num = input("Enter the Shift value : ");
l = len(text);
output = "";


for i in range(l):
    current_word = Alphabet.find(text[i]);
    shift_word = (current_word+num-26) if (current_word+num>=26) else (current_word+num);
    output += Alphabet[shift_word];

print(output);