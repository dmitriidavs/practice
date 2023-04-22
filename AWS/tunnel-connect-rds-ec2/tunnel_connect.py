import os

import paramiko
from sqlalchemy import create_engine


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=os.environ.get('EC2_ADDRESS'),
            username=os.environ.get('EC2_USERNAME'),
            key_filename=os.environ.get('PRIVATE_KEY_PATH'))

print("SSH connection established")

local_port = 5432
remote_port = 5432
remote_host = os.environ.get('REMOTE_HOST')
ssh_transport = ssh.get_transport()
ssh_channel = ssh_transport.open_channel('direct-tcpip', (remote_host, remote_port), ('localhost', local_port))

db_uri = os.environ.get('USERS_DB_CONN')
engine = create_engine(db_uri)


with engine.connect() as conn:
    conn.execute('CREATE SCHEMA IF NOT EXISTS test')
    conn.commit()

ssh_channel.close()
ssh.close()
