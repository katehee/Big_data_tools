from pyspark import SparkConf, SparkContext
import pyspark as ps 
import pyspark.sql.functions as F

def main(sc):
  #companies to dataframe 
  companies = sc.textFile('/user/root/A2/companies.txt')
  header = companies.first()
  #filter out the header
  companies = companies.filter(lambda line: line != header)
  temp_df = companies.map(lambda k:k.split("\t"))
  comp_df = spark.createDataFrame(temp_df, schema = header.split('\t'))

  #round2 to dataframe 
  round_df = spark.read.csv('/user/root/A2/rounds2.csv', header=True, inferSchema=True)

  #join two dataframe 
  master_frame = round_df.join(comp_df, F.lower(round_df.company_permalink) == F.lower(comp_df.permalink))
  # master_frame.show()
  print(master_frame.count())
if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext.getOrCreate()
    spark = ps.sql.SparkSession.builder.getOrCreate()
    main(sc)
    sc.stop()
    