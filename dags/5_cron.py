import datetime as dt

from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator


args = {
    "owner": "jrstats",
    "retries": 5,
    "retry_delay": dt.timedelta(minutes=2)
}




@dag(
    dag_id="cron",
    description="cron",
    start_date=dt.datetime(2022,12,19), # catchup=True airflow will automatically run the flow once for each day missed
    schedule_interval="0 3 * * TUE,FRI",
    default_args=args,
    catchup=True
)
def taskflow_dag():
    
    b0 = BashOperator(
        task_id="bash0",
        bash_command="echo hello world"
    )

taskflow_dag()
