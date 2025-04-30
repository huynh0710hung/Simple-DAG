import os
from datetime import datetime
from profile import Profile

from cosmos import DbtDag, ProfileConfig, ProjectConfig, ExecutionConfig, ExecutionMode
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "dbt_db", "schema": "dbt_schema"}
    )
)

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dags/data_pipeline"),
    operator_args={#"install_deps": True,
                   
    },
    profile_config=profile_config,
    #execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/usr/local/bin/dbt",),
    execution_config=ExecutionConfig(execution_mode=ExecutionMode.LOCAL, 
                                     dbt_executable_path="/usr/local/bin/dbt",),
    schedule_interval="@daily",
    start_date=datetime(2025,1,4),
    catchup=False,
    dag_id="dbt_dag",
)

