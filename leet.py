def replace_all(text, d):
    for i, j in d.items():
        text = text.replace(i, j)
    return text

text = raw_input("Put something here to have it translated.")

leet = {'a':'4', 'e':'3', 'g':'6', 'i':'1', 'o':'0', 's':'5', 't':'7'}

txt = replace_all(text, leet)
print txt