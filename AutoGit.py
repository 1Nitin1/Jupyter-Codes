import subprocess
from datetime import datetime
import logging 

logging.basicConfig(
    filename='AutoGit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

rep_path = r'C:\Users\Nitin Baranwal\OneDrive\Desktop\Data Science'

def run(cmd):
    subprocess.run(cmd,cwd=rep_path,check=True)

run(['git','add','.'])
logging.info('Changes added to staging area.')
try:
    run(['git','commit','-m',f'Auto update {datetime.now():%Y-%m-%d--%H:%M:%S}'])
    logging.info('Changes committed successfully.')
except subprocess.CalledProcessError:
    logging.info('Nothing to commit.')

run(['git','push','origin','main'])
logging.info('Changes pushed to remote repository.')