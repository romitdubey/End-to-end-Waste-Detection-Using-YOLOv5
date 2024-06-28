import os
from pathlib import Path
import logging

#logging stirng
logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s:")

project_name = 'WasteDetectionYOLOv5'

list_of_files=[
    ".github/workflow/.gitkeep",
    "data/.getkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/component/data_ingestion.py",
    f"src/{project_name}/component/data_validation.py",
    f"src/{project_name}/component/model_trainer.py",
    f"src/{project_name}/constants/training_pipeline/__init__.py",
    f"src/{project_name}/constants/application.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/artifacts_entity.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/main_utils.py",
    f"src/{project_name}/logger/__init__.py",
    "research/trails.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")
    
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} is already exists")
