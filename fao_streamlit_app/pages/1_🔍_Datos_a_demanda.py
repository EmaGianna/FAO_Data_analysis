import streamlit as st
import datetime
from loguru import logger
from lib.app_functions import return_condition, create_list_options, agrupation


if __name__ == '__main__':
    
    st.set_page_config(page_title="Exploracion de Datos FAO",page_icon="🔍",)
    st.write("# Filtro y Descarga de Datos 🔍")
    st.sidebar.header("Filtro y Descarga de Datos")
    st.sidebar.markdown("""
            Proyecto desarrollado por:
            * [Damian Mariescurrena](mailto:damianmariescurrena@gmail.com)
            * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
            """)
    
    begin_time = datetime.datetime.now()

    df = st.session_state["key"]
    
    st.markdown(
     """
     # Exploracion de datos
        En la paresente web podra realizar las siguientes acciones:  
        
       * Filtrar los datos de FAO, en base a los filtros preestablecidos.
       * Realizar sumarizacion de datos en base a diferentes agrupaciones.
       
     """)

# The code block you provided is creating multiple lists (`list_areas`, `list_prod`, `list_elem`,
# `list_ano`, `list_fuente`) using the `create_list_options` function, which takes in a DataFrame
# (`df`) as input. These lists are then used as options for the `multiselect` widgets in the Streamlit
# application.


    st.subheader("Selecciones los filtros deseados")
    list_areas, list_prod, list_elem, list_ano, list_fuente = create_list_options(df)
    area = st.multiselect('Elija Area/Pais: ', list_areas, list_areas[0])
    producto = st.multiselect('Elija Producto: ', list_prod, list_prod[0])
    elemento = st.multiselect('Elija un gas/elemento: ', list_elem, list_elem[0])
    ano = st.multiselect('Elija un año: ', list_ano, list_ano[0])
    fuente = st.multiselect('Elija una fuente: ', list_fuente, list_fuente[0])
    

# The code block you provided is creating a condition string using the `return_condition` function,
# which takes in multiple parameters (`'df'`, `area`, `producto`, `elemento`, `ano`, `fuente`). This
# condition string is then evaluated using the `eval` function and used to filter the DataFrame `df`.
# The filtered DataFrame is then reset the index and assigned to the variable `df_subset`.
    condition = return_condition('df',area, producto, elemento, ano, fuente)
    try:
        df_subset = df[eval(condition)].reset_index(drop=True)
    except:
        df_subset = df
        
    st.dataframe(df_subset)

    st.download_button(
        label="Descargue los datos obtenidos con los filtros anteriores",
        data=df_subset.to_csv().encode('utf-8'),
        file_name='filtered_fao_data.csv',
        mime='text/csv',
    )

    st.subheader("Selecciones los campos por los que desea realizar una agrupacion")
    fields_list = df.columns.to_list()
    fields_list.remove('VALOR')
    fields = st.multiselect('Elija los campos para agrupar: ', fields_list, fields_list[0])
    logger.debug(f'Agrupando por {fields}.')
    df_agruped = agrupation(df, fields)
    st.dataframe(df_agruped)
    st.download_button(
        label="Descargue los datos obtenidos con los filtros anteriores",
        data=df_agruped.to_csv().encode('utf-8'),
        file_name='filtered_fao_data.csv',
        mime='text/csv',
    )

    end_time = datetime.datetime.now()
    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')
