from models import LogDb, session
import datetime
import os
import subprocess


def create_text_file():
    subprocess.call(["echo", "Hello"])
    now = datetime.datetime.now()
    output_dir = '/home/opicq/AnandaInvestorScript/Output'
    file_name = now.strftime("%Y-%m-%d_%H-%M-%S.txt")

    output_file = os.path.join(output_dir, file_name)
    try:
        with open(output_file, 'w') as f:
            f.write(str(now))
    except Exception as e:
        error_str = "ERROR : " + str(e)
        subprocess.call(["echo", error_str])
    subprocess.call(["echo", "Bye"])


def daily_check():
    subprocess.call(["echo", "Hello"])
    try:
        new_log_db = LogDb(project='Ananda Investor Script',
                           task='Daily Check',
                           issue='NA',
                           description='Daily record in DB',
                           msg_type='Success')
        session.add(new_log_db)
        session.commit()
    except Exception as e:
        error_str = "ERROR : " + str(e)
        subprocess.call(["echo", error_str])
    subprocess.call(["echo", "Bye"])


if __name__ == '__main__':
    daily_check()
