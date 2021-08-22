st = 'Print only the words that start with s in this sentence'
x= st.split()

for word in x:
    if word[0] == "s":
        print(word)
