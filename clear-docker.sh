docker-compose down -v #shut down airflow containers AND remove volumes defined in yaml

# change AIRFLOW__CORE__LOAD_EXAMPLES to 'false'

docker-compose up airflow-init

docker-compose up -d