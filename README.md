# Advanced Big Data Analytics

## Wikipedia-TF-IDF

####Steps

1. Choose any random wikipedia article as a seed page ([Supervised Learning](https://en.wikipedia.org/wiki/Supervised_learning))
2. Gather up all the immediate outlinks from the page and form a set of these links

  ```python
  from goose import Goose
  
  url = 'https://en.wikipedia.org/wiki/Supervised_learning'
  g = Goose()
  
  article = g.extract(url = url)
  
  outlinks = article.links
  ```

3. Curate the links, form a set and store in a pickle file.

4. Load the pickle file (there are roughly 127 links in the set)

  ```python
  import pickle
  
  links = pickle.load(open('wiki-links.p', "rb"))
  ```

5. Crawl through each of the page and store the cleaned text from each page in a separate text file

  ```python
  from goose import Goose
  g = Goose()
  
  for link in links:
    url = "https://en.wikipedia.org" + link
    article = g.extract(url=url)
    
    # Files are stores in a separate folder named "Wikipedia-Pages"
    filename = "Wikipedia-Pages/" + link[6:]
    
    f = open(filename, 'w')
    f.write(article.cleaned_text.encode('ascii', 'ignore'))
    f.close()

  ```
  
