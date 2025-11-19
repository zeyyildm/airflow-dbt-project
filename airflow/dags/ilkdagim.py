from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import sys
import os

scripts_path = '/opt/airflow/scripts'
if os.path.exists(scripts_path):
    sys.path.append(scripts_path)
else:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../scripts'))

from data_processor import process_data, validate_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 11, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='DAG-1',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Veri işleme ve temizleme DAG\'ı',
)


start = DummyOperator(task_id='start', dag=dag)

process_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag
)

validate_task = PythonOperator(
    task_id='validate_data',
    python_callable=validate_data,
    dag=dag
)

ilk_task = PostgresOperator(
    task_id='delete_past',
    postgres_conn_id = 'postgres_default',
    sql = """
        DELETE FROM users
        WHERE signup_date < NOW() - INTERVAL '360 days';
    """,
    dag = dag
)

end = DummyOperator(task_id='end', dag=dag)

start >> process_task >> validate_task >> ilk_task >> end

