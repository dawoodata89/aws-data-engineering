import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Trusted
CustomerTrusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-dawood/customer-trusted/"],
        "recurse": True,
    },
    transformation_ctx="CustomerTrusted_node1",
)

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1688586206033 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-dawood/accelerometer_landing/"],
        "recurse": True,
    },
    transformation_ctx="AccelerometerLanding_node1688586206033",
)

# Script generated for node Privacy Join
PrivacyJoin_node1688586319135 = Join.apply(
    frame1=CustomerTrusted_node1,
    frame2=AccelerometerLanding_node1688586206033,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="PrivacyJoin_node1688586319135",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=PrivacyJoin_node1688586319135,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://stedi-dawood/", "partitionKeys": []},
    transformation_ctx="AccelerometerTrusted_node3",
)

job.commit()
