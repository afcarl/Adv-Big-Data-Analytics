# Advanced Big Data Analytics

##Homework 1

###Questions
1. Download and Install Spark. Learn how to use it.

2. Download Wikipedia dataset. Extract about 100 pages (items) based on your own interest. You may use snowball method to crawl a few related/linked pages. Create TF-IDF of each page.

3. Use Twitter Streaming API to receive real-time twitter data. Collect 30 mins of Twitter data on 5 companies using keyword=xxx (e.g., ibm). Consider all Twitter data from a company is one document. Create TF-IDF of each company’s tweets in that 30 minutes.

4. Use Yahoo Finance to receive the Stock price data. Collect 30 mins of Finance data on 5 companies, one value per minute. Use the outlier function to display outliers that are large than two standard deviation.

###Setup
1. First setup and run a virtual environment using the command:
  ```bash
  $ virtualenv hw1
  $ source hw1/bin/activate
  ```

2. Install all the libraries in the virtual environment from the
`requirements.txt` file using the command:
  ```bash
  $ pip install -r requirements.txt
  ```
###Solution
 - [Wikipedia TF-IDF](https://github.com/bahuljain/Adv-Big-Data-Analytics/tree/master/Wikipedia-TF-IDF)
 - [Twitter TF-IDF](https://github.com/bahuljain/Adv-Big-Data-Analytics/tree/master/Twitter-TF-IDF)
 - [Yahoo Finance](https://github.com/bahuljain/Adv-Big-Data-Analytics/tree/master/Yahoo-Finance)
