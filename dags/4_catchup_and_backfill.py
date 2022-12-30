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
    dag_id="catchup_and_backfill",
    description="catchup_and_backfill",
    start_date=dt.datetime(2022,12,20), # catchup=True airflow will automatically run the flow once for each day missed
    schedule_interval="@daily",
    default_args=args,
    catchup=True
)
def taskflow_dag():
    
    b0 = BashOperator(
        task_id="bash0",
        bash_command="echo hello world"
    )

    b0



taskflow_dag()


# if catchup is false, or we want to manually backfill, run the following bash:
"""
docker ps #find the container ID for the scheduler
docker exec -it 4e2d0c84d345 bash # login to the airflow scheduler
airflow dags backfill -s 2022-12-01 -e 2022-12-10 catchup_and_backfill #start, end, dag_id
exit #exit airflow scheduler
"""