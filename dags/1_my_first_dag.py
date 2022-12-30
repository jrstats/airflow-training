import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator


args = {
    "owner": "jrstats",
    "retries": 5,
    "retry_delay": dt.timedelta(minutes=2)
}


with DAG(
    dag_id="my_first_dag1_v3",
    description="getting started with airflow",
    start_date=dt.datetime(2022,12,30),
    schedule_interval="@daily",
    default_args=args
) as dag:
    
    # bash task
    task0 = BashOperator(
        task_id="first_task",
        bash_command="echo hello world"
    )

    task1 = BashOperator(
        task_id="second_task",
        bash_command="echo running after the first task"
    )

    task2 = BashOperator(
        task_id="third_task",
        bash_command="echo starting at the same time as the second task"
    )

    task0.set_downstream([task1, task2])