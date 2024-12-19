import logging

from airflow.decorators import dag, task
import pendulum


@dag(
    dag_id="hello_kubernetes",
    dag_display_name="Hello Kubernetes",
    schedule_interval=None,
    start_date=pendulum.datetime(2024, 1, 1),
    catchup=False,
    default_args={"owner": "airflow", }
)
def hello_kubernetes():
    @task
    def hello() -> str:
        return "Hello"

    @task
    def kubernetes(greeting: str):
        logging.info(f"{greeting}, Kubernetes")

    t=hello_kubernetes()
    kubernetes(hello())

hello_kubernetes()