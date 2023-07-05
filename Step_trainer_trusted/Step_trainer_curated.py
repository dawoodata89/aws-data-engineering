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

# Script generated for node Accelerometer trusted
Accelerometertrusted_node1688594858091 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-dawood/accelerometer_trsuted2/"],
        "recurse": True,
    },
    transformation_ctx="Accelerometertrusted_node1688594858091",
)

# Script generated for node step_trainer
step_trainer_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://stedi-dawood/Step_trainer/"], "recurse": True},
    transformation_ctx="step_trainer_node1",
)

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1688595375946 = ApplyMapping.apply(
    frame=Accelerometertrusted_node1688594858091,
    mappings=[
        ("serialNumber", "string", "right_serialNumber", "string"),
        ("z", "double", "right_z", "double"),
        ("birthDay", "string", "right_birthDay", "string"),
        ("timeStamp", "bigint", "right_timeStamp", "bigint"),
        (
            "shareWithPublicAsOfDate",
            "bigint",
            "right_shareWithPublicAsOfDate",
            "bigint",
        ),
        (
            "shareWithResearchAsOfDate",
            "bigint",
            "right_shareWithResearchAsOfDate",
            "bigint",
        ),
        ("registrationDate", "bigint", "right_registrationDate", "bigint"),
        ("customerName", "string", "right_customerName", "string"),
        ("user", "string", "right_user", "string"),
        ("y", "double", "right_y", "double"),
        ("x", "double", "right_x", "double"),
        ("email", "string", "right_email", "string"),
        ("lastUpdateDate", "bigint", "right_lastUpdateDate", "bigint"),
        ("phone", "string", "right_phone", "string"),
    ],
    transformation_ctx="RenamedkeysforJoin_node1688595375946",
)

# Script generated for node Join
Join_node1688594348027 = Join.apply(
    frame1=step_trainer_node1,
    frame2=RenamedkeysforJoin_node1688595375946,
    keys1=["serialNumber", "sensorReadingTime"],
    keys2=["right_serialNumber", "right_timeStamp"],
    transformation_ctx="Join_node1688594348027",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1688595382392 = glueContext.write_dynamic_frame.from_options(
    frame=Join_node1688594348027,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-dawood/Step_trainer_trusted2/",
        "partitionKeys": [],
    },
    transformation_ctx="StepTrainerTrusted_node1688595382392",
)

job.commit()
