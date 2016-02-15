# Twitter TF-IDF using Spark

### Steps

1. Create keys to use Twitter Streaming API. I have used tweepy, which is an easy to
use python library for accessing Twitter API. The following packages need to be
imported to start working with tweepy Streaming API.

  ```python
  from tweepy.streaming import StreamListener
  from tweepy import OAuthHandler
  from tweepy import Stream
  ```

2. Filter tweets based on track. We will now stream tweets associated with the 5
companies given in the list.

  ```python
  companyList = ["twitter", "google", "apple", "facebook", "amazon"]

  twitterStream.filter(track=companyList)
  ```
3. Tweets that are not in English language are ignored.

  ```python
  if tweet['lang'] == 'en':
      # process the tweets
    text = tweet['text'].lower().encode('ascii', 'ignore').decode('ascii')

  ```

4. Five separate text files are created in the folder `Company-Tweets`. Based on
which company the tweet is related to, the tweet is written in the respective
file.

  ```python
  with open("/Company-Tweets/" + company + "_tweets.txt", 'a') as f:
    f.write(text + '\n')
  ```
5. We now let the streaming continue for 30 minutes.

  ```python
  if time.time() - self.startTime <= 1800:
    tweet = json.loads(data)
    # process and store the tweets
  ```

6. Now that we have the dataset, we create an RDD that loads all these files and
stores them in a (key, value) pair format where key is the path of the file and
value is the contents of the file. It is important that contents of files should
not get mixed up, hence we use `wholeTextFiles` from SparkContext. Further we
need only the content and not the paths, hence we extract only values and
finally we split the text of each company's twitter data to obtain only words.

  ```python
  company_tweets = sc.wholeTextFiles("Company-Tweets/").values().map(lambda doc: re.split('\W+', doc))
  ```

7. We create Term Frequencies for each company's twitter data. This can be done
by using the `HashingTF` class from `mllib.feature` package of Spark.

  ```python
  from pyspark.mllib.feature import HashingTF

  hashingTF = HashingTF()
  tf = hashingTF.transform(company_tweets)
  ```
8. In the next and the final step we compute the IDF for every word in all the
files and scale the TF obtained in the previous step by the IDF.

  ```python
  from pyspark.mllib.feature import IDF

  tf.cache()
  idf = IDF().fit(tf)
  tfidf = idf.transform(tf)
  ```

9. Save the awesome TF-IDF result of every company's twitter data in an output
folder. Multiple files will be created based on the partitioning of the RDD.

  ```python
  tfidf.saveAsTextFile("tf-idf-output")
  ```

10. The final output is stored in the `tf-idf-output` folder. The output file
shows tf-idf vector for each company's tweets as a separate tuple. The second
entry in the tuple is the list of words (encoded using a hashing function) that
occur in that file and the third entry in the tuple is the list of tf-idf values
for those words respectively.
