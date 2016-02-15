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
  if decoded['lang'] == 'en':
    # process the tweets
    text = decoded['text'].lower().encode('ascii', 'ignore').decode('ascii')

  ```

4. Five separate text files are created in the folder `Company-Tweets`. Based on which company the tweet is related to, the tweet is written in the respective file.

  ```python
  with open(company + "_tweets.txt", 'a') as f:
    f.write(text + '\n')
  ```
5. We now let the streaming continue for 30 minutes

  ```python
  if time.time() - self.startTime <= 1800:
    tweet = json.loads(data)
    # process and store the tweets
  ```
