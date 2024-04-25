from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.dagrun_operator import TriggerDagRunOperator

with DAG('dag-run-dag1', description='DAG run DAG',
          schedule_interval=None,
          start_date=datetime(2024,3,5), 
          catchup=False) as dag:

    t1 = BashOperator(task_id='tsk1', bash_command='sleep 5')
    t2 = TriggerDagRunOperator(task_id='tsk2', trigger_dag_id='dag-run-dag2')    

    t1 >> t2
