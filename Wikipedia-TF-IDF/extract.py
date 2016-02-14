from goose import Goose
import pickle

g = Goose()

links = pickle.load(open('wiki-links.p', "rb"))

for link in links:
    url = "https://en.wikipedia.org" + link
    print url

    article = g.extract(url=url)

    filename = "Wikipedia-Pages/" + link[6:]
    f = open(filename, 'w')
    f.write(article.cleaned_text.encode('ascii', 'ignore'))
    f.close()
