from pyspark import SparkContext
from os import listdir

if __name__== "__main__":
    sc = SparkContext(appName = "StocksOutlierRemoval")

    files = [ f for f in listdir('./Stock-Prices') if '.txt' in f ]
    for f in files:
        lines = sc.textFile("Stock-Prices/" + f)
        prices = lines.map(lambda s : float(s))
        mean = prices.mean()
        stdev = prices.stdev()
        outliers = prices.filter(lambda p: abs(p - mean) > 2 * stdev)
        print "Outliers in " + f[:len(f)-4] + ": " + `outliers.collect()`
