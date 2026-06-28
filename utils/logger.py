import logging
import os

os.makedirs("logs", exist_ok=True) #FileExistsError

logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s - %(message)s',
    force= True    
)
logger = logging.getLogger(__name__)