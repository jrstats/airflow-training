import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator


args = {
    "owner": "jrstats",
    "retries": 5,
    "retry_delay": dt.timedelta(minutes=2)
}


def hello_world():
    print("hello world")

def hello(age, task_instance):
    first_name = task_instance.xcom_pull(task_ids="get_name", key="first_name")
    last_name = task_instance.xcom_pull(task_ids="get_name", key="last_name")
    print(f"hello {first_name} {last_name} ({age})")

def get_name(task_instance):
    # xcom maz size 48KB!
    task_instance.xcom_push(key="first_name", value="James")
    task_instance.xcom_push(key="last_name", value="R")

with DAG(
    dag_id="python_operator",
    description="getting started with airflow using python operators",
    start_date=dt.datetime(2022,12,29),
    schedule_interval="@daily",
    default_args=args
) as dag:
    
    # python task
    task0 = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )

    task1 = PythonOperator(
        task_id="task_with_args",
        python_callable=hello,
        op_kwargs={"age": 25}
    )

    task0.set_downstream(task1)


