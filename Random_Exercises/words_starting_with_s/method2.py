st = 'Print only the words that start with s in this sentence'
x= st.split()
s= [word for word in x if word[0] == 's']


for x in s:
    print(x)
