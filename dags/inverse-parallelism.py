from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

with DAG('inverse-parallelism', description='Inverse Parallelism DAG',
          schedule_interval=None,
          start_date=datetime(2024,3,5), 
          catchup=False) as dag:

    t1 = BashOperator(task_id='tsk1', bash_command='sleep 5')
    t2 = BashOperator(task_id='tsk2', bash_command='sleep 5')
    t3 = BashOperator(task_id='tsk3', bash_command='sleep 5')

    [t1,t2] << t3