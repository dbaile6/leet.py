def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

original_text = raw_input("Put something here to have it translated.")

reps = {'a':'n', 'b':'o', 'c':'p', 'e':'q', 'f':'r', 'g':'s', #'h':'t', 'i':'u', 'j':'v', 'k':'w', 'l':'x', 'm':'y', 'n':'z', 'o':'a', 'p':'b', 'q':'c', 'r':'d', 's':'e', 't':'f', 'u':'g', 'v':'h' 'w':'i', 'x':'j', 'y':'k', 'z':'l'}

text = replace_all(original_text, reps)
print txt