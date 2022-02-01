from pyspark import SparkConf, SparkContext

def main(sc):
    weekdays= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    textFile = sc.textFile("/user/root/A2/shakespeare_100.txt")
    #remove any character attached to weekdays list by replace command
    wordList = textFile.flatMap(lambda line: line.replace(',',' ').replace('?',' ').replace('!',' ').replace('.',' ').replace(';',' ').split())
    #count the word occurence 
    wordCount = wordList.map(lambda word: (word,1))
    wordsWithTotalCount = wordCount.reduceByKey(lambda v1, v2: v1+v2)
    #collectAsMap to retrieve specific keyword's occurence 
    Dict = wordsWithTotalCount.collectAsMap()
    weekday_Dict = {}
    for day in weekdays: 
      weekday_Dict[day] = Dict[day]
    #reverse True to get from most frequent to least frequent 
    for key in sorted(weekday_Dict, key=weekday_Dict.get, reverse=True): 
        print((key,weekday_Dict[key]))

if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext.getOrCreate()
    main(sc)
    sc.stop()


