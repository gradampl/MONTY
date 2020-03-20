texts = []
for i in range(5):
    texts.append(input("Wpisz jakiś tekst: \n"))

j = 0
while j < 5:
    print(len(texts[j]))
    j += 1
    
texts.clear()