from dagster import job, op
import logging

logger = logging.getLogger()

@op
def get_name():
    return "dagster"


@op
def hello(name: str):
    print(f"Hello, {name}!")


@job
def hello_dag():
    result = hello(get_name())
    logger.info(result)