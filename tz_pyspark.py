from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, array, lit

spark = SparkSession.builder.appName("example").getOrCreate()

# Создаем примерные данные для DataFrame 'products_df'
products_data = [
    (1, "product1", 1),
    (2, "product2", 2),
    (3, "product3", None),
    (4, "product4", 1),
    (5, "product5", 2)
]
products_df = spark.createDataFrame(products_data, ["id", "product_name", "category_id"])

categories_data = [
    (1, "category1"),
    (2, "category2"),
    (3, "category3")
]
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])


def get_product_category_pairs(products, categories):
    product_categories = products.join(categories, products["category_id"] == categories["category_id"], "left_outer")
    
    product_category_pairs = product_categories.select(
        col("product_name"),
        explode(array(col("category_name"))).alias("category_name")
    )
    products_without_categories = product_categories.filter(col("category_name").isNull()).select(
        col("product_name"),
        lit("").alias("category_name")
    )
    result = product_category_pairs.union(products_without_categories)

    return result

# Пример
result_df = get_product_category_pairs(products_df, categories_df)
result_df.show()
