from pyspark import SparkConf, SparkContext
import re 

def main(sc):
    textFile = sc.textFile("/user/root/A2/shakespeare_100.txt")
    wordList = textFile.flatMap(lambda line: line.split()) 
    #remove all puntuations using re.sub
    filterList = wordList.map(lambda word: re.sub(r'[^\w\s]','',word.lower().strip()))
    wordCount = filterList.map(lambda word: (word,1))
    wordsWithTotalCount = wordCount.reduceByKey(lambda v1, v2: v1+v2)
    Dict = wordsWithTotalCount.collectAsMap()
    print(len(Dict))


if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext.getOrCreate()
    # spark = ps.sql.SparkSession.builder.getOrCreate()
    main(sc)
    sc.stop()