python3 -m venv .venv
source ./.venv/bin/activate
pip install 'apache-airflow==2.5.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
export AIRFLOW_HOME=.
airflow db init
airflow users create \
          --username admin \
          --password changeme \
          --firstname FIRST_NAME \
          --lastname LAST_NAME \
          --role Admin \
          --email james@robinson.fyi

airflow standalone
