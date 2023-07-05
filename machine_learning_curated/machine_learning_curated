import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs


def sparkAggregate(
    glueContext, parentFrame, groups, aggs, transformation_ctx
) -> DynamicFrame:
    aggsFuncs = []
    for column, func in aggs:
        aggsFuncs.append(getattr(SqlFuncs, func)(column))
    result = (
        parentFrame.toDF().groupBy(*groups).agg(*aggsFuncs)
        if len(groups) > 0
        else parentFrame.toDF().agg(*aggsFuncs)
    )
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node step trainer trusted
steptrainertrusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-dawood/Step_trainer_trusted2/"],
        "recurse": True,
    },
    transformation_ctx="steptrainertrusted_node1",
)

# Script generated for node Drop Fields
DropFields_node1688597750049 = DropFields.apply(
    frame=steptrainertrusted_node1,
    paths=[
        "right_email",
        "right_phone",
        "right_shareWithResearchAsOfDate",
        "right_registrationDate",
        "right_lastUpdateDate",
        "right_user",
        "right_birthDay",
        "right_customerName",
        "right_serialNumber",
    ],
    transformation_ctx="DropFields_node1688597750049",
)

# Script generated for node Aggregate
Aggregate_node1688597795267 = sparkAggregate(
    glueContext,
    parentFrame=DropFields_node1688597750049,
    groups=[
        "serialNumber",
        "right_y",
        "right_timeStamp",
        "sensorReadingTime",
        "right_x",
        "right_z",
    ],
    aggs=[["distanceFromObject", "sum"]],
    transformation_ctx="Aggregate_node1688597795267",
)

# Script generated for node machine_learning_curated
machine_learning_curated_node1688597809699 = (
    glueContext.write_dynamic_frame.from_options(
        frame=Aggregate_node1688597795267,
        connection_type="s3",
        format="json",
        connection_options={
            "path": "s3://stedi-dawood/machine_learning_curated/",
            "partitionKeys": [],
        },
        transformation_ctx="machine_learning_curated_node1688597809699",
    )
)

job.commit()
