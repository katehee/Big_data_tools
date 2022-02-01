from pyspark import SparkConf, SparkContext

def makeTuple(line):
    words = line.split('\t')
    return (words[1]) # word[0] permalink	word[1]name

from pyspark import SparkConf, SparkContext

def makeTuple(line):
    words = line.split('\t')
    return (words[0]) # word[0] permalink   word[1]name

def main(sc):
    textFile = sc.textFile("/user/root/A2/companies.txt")
    #remove header
    header = textFile.first()
    textFile = textFile.filter(lambda line: line != header)
    wordList = textFile.map(lambda line: makeTuple(line))  #filter out header
    wordCount = wordList.map(lambda word: (word,1))
    reducedName = wordCount.reduceByKey(lambda v1,v2: v1+v2)
    print(reducedName.count()) 


if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext.getOrCreate()
    main(sc)
    sc.stop()


#spark-submit --master yarn --deploy-mode client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m one.py
