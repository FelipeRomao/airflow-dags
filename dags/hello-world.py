from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval=None,
          start_date=datetime(2024,3,5), catchup=False)

t1 = BashOperator(task_id='tsk1', bash_command='sleep 5', dag=dag)
t2 = BashOperator(task_id='tsk2', bash_command='sleep 5', dag=dag)
t3 = BashOperator(task_id='tsk3', bash_command='sleep 5', dag=dag)

t1 >> t2 >> t3