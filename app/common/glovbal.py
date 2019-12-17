import asyncio

flink_java_path = '/flink-runtime/src/main/java/com/k2data/yangning/ailab/{class_name}.java'
flink_jar_path = '/flink-runtime/target/flink-runtime-1.0-SNAPSHOT.jar'
event_loop = asyncio.get_event_loop()

AILAB_URL = 'dev.api.kstonedata.k2/ailab-service'
operator_info_path = '/ailab/v1/raw-operators/{id}'

hook_callback = f"{AILAB_URL}/ailab/v1/jobs/status"

py_runtime_rpc_channel = 'localhost:50052'

flk_runtime_ctrl_url = 'dev.api.kstonedata.k2/flink'

DB_HOST = 'localhost'
DB_PORT = '5433'
DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_NAME = 'esf'

job_manager_host = '127.0.0.1'
job_manager_port = '8081'

job_manager_url = job_manager_host + ':' + job_manager_port

db_engine = None

xml_rpc_server = None

jinjia2_env = None
