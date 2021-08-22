st = 'Print every word in this sentence that has an even number of letters'
for y in st.split():
    if (len(y)%2)==0:
        print(y)
