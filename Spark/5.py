from pyspark import SparkConf, SparkContext
import pyspark as ps
import pyspark.sql.functions as F

def makeTuple2(line,dict_median):
    words = line.split()
    if int(words[1]) > dict_median[words[0]]: 
      return (words[0], int(words[1]))
    else: 
      return ("LowerThanMedian",0)

def makeTuple(line):
    words = line.split()
    return (words[0], int(words[1]))

def main(sc):
    #create dataframe with department salary info 
    departFile = sc.textFile("/user/root/A2/dept_salary.txt")
    ListForMedian = departFile.map(lambda line:makeTuple(line))
    header = ['dept', 'salary']
    dfForMedian = spark.createDataFrame(data=ListForMedian, schema=header)
    #find median using Quantile
    median_df = dfForMedian.groupby("dept").agg(F.expr('percentile(salary, array(0.5))')[0].alias('median'))
    median_df.show()
    #create dictionary {dept: dept_median}
    tuple_median = map(lambda row: row.asDict(), median_df.collect())
    dict_median = {median['dept']: median["median"] for median in tuple_median}
  

    medList = departFile.map(lambda line: makeTuple2(line, dict_median))
    medianCount = medList.combineByKey(lambda value: (value , 1),
                             lambda x, value: (x[0] + value, x[1] + 1),
                             lambda x, y: (x[0] + y[0], x[1] + y[1]))

    reduceCount = medianCount.map(lambda (key, (totalSum, count)): (key, count))
    # print(reduceCount)
    reduceCount.saveAsTextFile("/user/root/A2/dept_Q5")

if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext.getOrCreate()
    spark = ps.sql.SparkSession.builder.getOrCreate()
    main(sc)
    sc.stop()

    #spark-submit --master yarn --deploy-mode client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m 5.py