
text_to_morse = {"a":"._",
                 "b":"_...",
                 "c":"_._.",
                 "d":"_..",
                 "e":".",
                 "f":".._.",
                 "g":"__.",
                 "h":"....",
                 "i":"..",
                 "j":"._ _ _",
                 "k":"_._",
                 "l":"._..",
                 "m":"__",
                 "n":"_.",
                 "o":"___",
                 "p":".__.",
                 "q":"__._",
                 "r":"._.",
                 "s":"...",
                 "t":"_",
                 "u":".._",
                 "v":"..._",
                 "w":".__",
                 "x":"_.._",
                 "y":"_.__",
                 "z":"__..",
                 " ":"/",
                 "?":"..__..",
                 ".":"._._._"}

morse_to_text = {value:key for key,value in zip(text_to_morse.keys(),text_to_morse.values())}


def englishtomorse(word):
    morse_string = ""
    for c in word:
       morse_string+=" "+text_to_morse[c.lower()]
    print(morse_string)
    return morse_string

def morsetoenglish(morse_code):
    morse_code = morse_code.split(" ")
    text = ""
    for c in morse_code:
        if c != "":
         text += morse_to_text[c.lower()]
    return text

print(morsetoenglish(englishtomorse("what is your name?")))