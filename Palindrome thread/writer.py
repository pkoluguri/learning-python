import wikipediaapi
import io

wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Palindrome')

with io.open("words.txt","w",encoding="utf-8") as file:
    for word in page_py.text.split(" "):
        file.write(word+"\n")