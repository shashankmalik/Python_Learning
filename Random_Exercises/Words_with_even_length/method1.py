st = 'Print every word in this sentence that has an even number of letters'
x=st.split()
for y in x:
    z=len(y)
    if z%2==0:
        print(y)
