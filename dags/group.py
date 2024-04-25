from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

with DAG('group', description='Group DAG',
          schedule_interval=None,
          start_date=datetime(2024,3,5), 
          catchup=False) as dag:

    t1 = BashOperator(task_id='tsk1', bash_command='sleep 5')
    t2 = BashOperator(task_id='tsk2', bash_command='sleep 5')
    t3 = BashOperator(task_id='tsk3', bash_command='sleep 5')
    t4 = BashOperator(task_id='tsk4', bash_command='sleep 5')
    t5 = BashOperator(task_id='tsk5', bash_command='sleep 5')
    t6 = BashOperator(task_id='tsk6', bash_command='sleep 5')

    with TaskGroup('tsk_group') as tsk_group:
        t7 = BashOperator(task_id='tsk7', bash_command='sleep 5')
        t8 = BashOperator(task_id='tsk8', bash_command='sleep 5')
        t9 = BashOperator(task_id='tsk9', bash_command='sleep 5', trigger_rule='one_failed')

    t1 >> t2
    t3 >> t4
    [t2,t4] >> t5 >> t6
    t6 >> tsk_group
