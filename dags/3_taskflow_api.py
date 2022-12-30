import datetime as dt

from airflow import DAG
from airflow.decorators import dag, task


args = {
    "owner": "jrstats",
    "retries": 5,
    "retry_delay": dt.timedelta(minutes=2)
}




@dag(
    dag_id="taskflow_api",
    description="getting started with airflow using python operators",
    start_date=dt.datetime(2022,12,29),
    schedule_interval="@daily",
    default_args=args
)
def taskflow_dag():
    
    @task()
    def hello(first_name, last_name, age):
        print(f"hello {first_name} {last_name} ({age})")

    @task()
    def hello1(names, age):
        print(f"hello {names['first_name']} {names['last_name']} ({age})")

    @task(multiple_outputs=True)
    def get_name():
        return {
            "first_name": "James",
            "last_name": "R"
        }

    @task()
    def get_age():
        return 25

    name = get_name()
    age = get_age()

    hello(name["first_name"], name["last_name"], age)
    hello1(name, age)


taskflow_dag()