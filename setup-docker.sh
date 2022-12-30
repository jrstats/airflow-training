curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.0/docker-compose.yaml'
# change executor from celery to local (for example)

mkdir -p ./dags ./logs ./plugins
# echo -e "AIRFLOW_UID=$(id -u)" > .env #linux only

docker compose up airflow-init

#The account created has the login airflow and the password airflow.

docker-compose up -d