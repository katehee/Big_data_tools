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
  comp_df = temp_df.toDF(header.split('\t'))

  #round2 to dataframe 
  round_df = spark.read.csv('/user/root/A2/rounds2.csv', header=True, inferSchema=True)
  # round_df.show()

  #join two dataframe 
  master_frame = comp_df.join(round_df, F.lower(comp_df.permalink) == F.lower(round_df.company_permalink), "inner")
  master_frame = master_frame.select(['funding_round_type', 'raised_amount_usd'])
  mean_df = master_frame.groupby("funding_round_type").agg(F.mean(F.col("raised_amount_usd")).alias('mean'))
  mean_df.show()  # df showing mean of each department 
  #filter investment type in the range of 5M to 15M raised_amount_usd. 
  mean_df.filter((mean_df.mean >= 5000000) & (mean_df.mean <= 15000000)).show(truncate=False)

if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext.getOrCreate()
    spark = ps.sql.SparkSession.builder.getOrCreate()
    main(sc)
    sc.stop()