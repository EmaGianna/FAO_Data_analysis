from unidecode import unidecode
import pandas as pd  
from loguru import logger
import streamlit as st

@st.cache_data
def load_data(path_file):
    """
    The function `load_data` loads a CSV file from a given URL, filters the data based on the year
    range, drops unnecessary columns, and converts the column names to uppercase.

    :param url_file: The `url_file` parameter is the URL or file path of the CSV file that you want to
    load into a pandas DataFrame
    :return: The function `load_data` returns a subset of a DataFrame `df_fao_subset` that has been
    loaded from a CSV file specified by the `url_file` parameter.
    """
    df = pd.read_csv(path_file, encoding='latin1')
    df_fao = df.copy()
    df_fao_subset = df_fao[(df_fao['Año'] >= 2000) & (df_fao['Año'] <=2023)].reset_index(drop=True)
    df_fao_subset = df_fao_subset.drop(columns=['Código área (M49)', 'Código área', 'Código Producto', 'Código Elemento', 'Código año', 'Código fuente', 'Nota'])
    df_fao_subset.columns = [unidecode(column).upper() for column in df_fao_subset.columns]
    logger.info(f"Dataframe df_fao_subset was created correctly. With {df_fao_subset.shape[0]} lines and {df_fao_subset.shape[1]} columns")

    return df_fao_subset

@st.cache_data
def load_data_filtered(path_file):
    """
    The function `load_data_filtered` loads a CSV file into a pandas DataFrame, creates a copy of the
    DataFrame, converts the column names to uppercase and removes any special characters, and logs the
    information about the created DataFrame.
    
    :param path_file: The `path_file` parameter is the file path of the CSV file that you want to load
    and filter the data from
    """
    df = pd.read_csv(path_file, encoding='utf-8')
    df_fao = df.copy()
    df_fao.columns = [unidecode(column).upper() for column in df_fao.columns]
    logger.info(f"Dataframe df_fao_subset was created correctly. With {df_fao.shape[0]} lines and {df_fao.shape[1]} columns")

    return df_fao

from unidecode import unidecode
import pandas as pd  
from loguru import logger
import streamlit as st

@st.cache_data
def load_data_filterd_parquet(path_file):
    """
    The function `load_data_filterd_parquet` loads a parquet file into a pandas DataFrame, converts the
    column names to uppercase, and logs the number of rows and columns in the DataFrame.
    
    :param path_file: The parameter "path_file" is the file path of the Parquet file that you want to
    load and filter
    :return: a pandas DataFrame named "df_fao" that has been loaded from a parquet file.
    """
    
    df_fao = pd.read_parquet(path_file)
    df_fao.columns = [unidecode(column).upper() for column in df_fao.columns]
    logger.info(f"Dataframe df_fao_subset was created correctly. With {df_fao.shape[0]} lines and {df_fao.shape[1]} columns")

    return df_fao
