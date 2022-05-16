data = 'From JeremyMondreal@yahoo.com stevenJoseph'

finddata= data.find('@')

findend= data.find(' ',finddata)

print(data[finddata+1:findend])

text = "X-DSPAM-Confidence:    0.8475"

start = text.find(':')
end = text.find('5',start)

a = text[start+1 : end+1]
a = a.strip()
a = float(a)
print(a)