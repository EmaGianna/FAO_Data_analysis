import os
import shutil
import requests
import zipfile
from loguru import logger

def del_dir_path(directory_path):
    """
    The function `del_dir_path` deletes a directory and logs a message indicating whether the directory
    was successfully deleted or if it does not exist.
    
    :param directory_path: The directory path is the path of the directory that you want to delete
    """
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        logger.info(f"Directory {directory_path} was deleted.")
    else:
        logger.info(f"Directory {directory_path} don't exist.")



def download_fao_file(url, dest_path, extract_path):

    del_dir_path(extract_path)

    response = requests.get(url)
    with open(dest_path, "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(dest_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    os.remove(dest_path)

    files = os.listdir(extract_path)
    for file in files:
        if file != "Emisiones_Totales_S_Todos_los_Datos_(Normalizado).csv":
            os.remove(os.path.join(extract_path, file))
        else:
            original_path = os.path.join(extract_path, file)
            new_name = "Emisiones_Totales_S_Todos_los_Datos_Normalizado.csv"
            new_path = os.path.join(extract_path, new_name)
            os.rename(original_path, new_path)

    file = os.listdir(extract_path)
    logger.info(f"Download file {file}.")
    
