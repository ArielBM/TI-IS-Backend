import paramiko
from paramiko import Transport, SFTPClient
from dotenv import load_dotenv
import os

def transfer_files(file_to_transfer, name_of_file):
    load_dotenv()

    sftp_host = os.getenv('SFTP_HOST')
    sftp_port = int(os.getenv('SFTP_PORT'))
    sftp_user = os.getenv('SFTP_USER')
    sftp_pass = os.getenv('SFTP_PASSWORD')

    remote_file_path = f'./{name_of_file}'
    transport = None
    sftp = None

    try:
        transport = Transport((sftp_host, sftp_port))
        transport.connect(username=sftp_user, password=sftp_pass)

        sftp = SFTPClient.from_transport(transport)

        sftp.put(file_to_transfer, remote_file_path)
        print(f"Archivo {file_to_transfer} cargado exitosamente a {remote_file_path}")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
    finally:
        if sftp:
            sftp.close()
        if transport:
            transport.close()