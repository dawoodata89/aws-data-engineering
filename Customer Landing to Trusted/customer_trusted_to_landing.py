import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Landing
CustomerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-dawood/customer_landing/"],
        "recurse": True,
    },
    transformation_ctx="CustomerLanding_node1",
)

# Script generated for node PrivacyFilter
PrivacyFilter_node1688511644843 = Filter.apply(
    frame=CustomerLanding_node1,
    f=lambda row: (not (row["shareWithResearchAsOfDate"] == 0)),
    transformation_ctx="PrivacyFilter_node1688511644843",
)

# Script generated for node Customer Trusted
CustomerTrusted_node1688511830005 = glueContext.write_dynamic_frame.from_options(
    frame=PrivacyFilter_node1688511644843,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-dawood/customer-trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="CustomerTrusted_node1688511830005",
)

job.commit()
