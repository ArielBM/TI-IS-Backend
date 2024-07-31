import os
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
from datetime import datetime

def execute_script():
    print(f"Running script at {datetime.now()}")
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    subprocess.run(["python", script_path], cwd=os.path.dirname(script_path))

if __name__ == "__main__":
    scheduler = BlockingScheduler()

    execute_script()  # Ejecuta la primera vez inmediatamente

    scheduler.add_job(execute_script, 'interval', days=1)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
