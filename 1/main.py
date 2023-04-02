cypher = {'a' : 'c',
'b' : 'd',
'c' : 'e',
'd' : 'f',
'e' : 'g',
'f' : 'h',
'g' : 'i',
'h' : 'j',
'i' : 'k',
'j' : 'l',
'k' : 'm',
'l' : 'n',
'm' : 'o',
'n' : 'p',
'o' : 'q',
'p' : 'r',
'q' : 's',
'r' : 't',
's' : 'u',
't' : 'v',
'u' : 'w',
'v' : 'x',
'w' : 'y',
'x' : 'z',
'y' : 'a',
'z' : 'b'}

def decript (msg):
    dec_msg = ""
    for i in range(len(msg)):
        if (msg[i] >= 'a' and msg[i] <= 'z'):
            dec_msg = dec_msg + cypher[msg[i]]
        else:
            dec_msg = dec_msg + msg[i]
    return dec_msg

def decript_v2 (msg):
    x = "abcdefghijklmnopqrstuvwxyz"
    y = "cdefghijklmnopqrstuvwxyzab"
    local_cypher = str.maketrans(x,y)
    return msg.translate(local_cypher)

enc_msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
dec_msg = decript_v2(enc_msg)
print(dec_msg)

url = "http://www.pythonchallenge.com/pc/def/map.html"
dec_url = decript_v2(url)
print(dec_url)

# Answer = "ocr"