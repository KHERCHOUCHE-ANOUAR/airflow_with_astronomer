from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime



#Function to preporcess the data
def preprocess_data():
    # Add your data preprocessing code here
    print("Data Preprocessing Complete")
#Function to train the model
def train_model():
    # Add your model training code here
    print("Model Training Complete")
#Function to evaluate the model
def evaluate_model():
    # Add your model evaluation code here
    print("Model Evaluation Complete")



# Define the default arguments for the DAG
with DAG('ml_pipeline_dag',
    start_date= datetime(2025, 4, 27),
    schedule_interval= '@weekly'
)as dag:
    # Define the tasks in the DAG
    preprocess_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data,
        dag=dag,
    )

    train_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
        dag=dag,
    )

    evaluate_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
        dag=dag,
    )

    # Set the task dependencies
    preprocess_task >> train_task >> evaluate_task