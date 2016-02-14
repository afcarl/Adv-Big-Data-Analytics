from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
import re


if __name__== "__main__":
    sc = SparkContext(appName = "PythonWordCount")

    documents = sc.wholeTextFiles("Wikipedia-Pages/").values().map(lambda doc: re.split('\W+', doc))

    hashingTF = HashingTF()

    tf = hashingTF.transform(documents)

    tf.cache()
    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)

    tfidf.saveAsTextFile("tf-idf-output")
