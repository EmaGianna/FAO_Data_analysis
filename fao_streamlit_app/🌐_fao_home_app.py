#streamlit run /opt/jpt_DataScience/Ciencia_Datos/Tp3-4/py/streamlit_app/🌐_fao_home_app.py
import streamlit as st
import datetime
from loguru import logger
from lib.df_functions import load_data_filterd_parquet

if __name__ == '__main__':


    begin_time = datetime.datetime.now()

##################################################

    st.set_page_config(page_title="Estadisticas FAO",page_icon="🌐",)

    st.write("# Poc Analisis de Datos FAO 🌐")
    
    url = 'https://github.com/EmaGianna/FAO_Data_analysis/raw/main/file/FAO_filtered.parquet'
    df = load_data_filterd_parquet(url)
    st.session_state["key"] = df
    

    with st.sidebar:
        st.sidebar.success("Selecciones la seccion a Visitar")
        st.write('Esta app es una poc de un analisis mas extenso sobre datos que provee la ONU\n \
                 en este caso en particular sobre datos de emisiones de gaases GHG provistas por\n \
                 [FAO](https://www.fao.org/faostat/es/#data/GT)')
        st.markdown("""
                    Proyecto desarrollado por:
                    * [Damian Mariescurrena](mailto:damianmariescurrena@gmail.com)
                    * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
                    """)

    st.markdown(
        """
        # Descripción del Dataset

        El Dataset [“totales de emisiones”](https://fenixservices.fao.org/faostat/static/bulkdownloads/Emisiones_Totales_S_Todos_los_Datos_(Normalizado).zip) \
        de FAOSTAT contiene las emisiones de gases de efecto invernadero generadas por los sistemas agroalimentarios.
        La información que se encuentra disponible en el archivo está representada por país y desde 1961 a 2020.

        Los campos que se incluyen en este archivo son los siguientes:

        *  **Código Ámbito:** código único del ámbito.  
        *  **Ámbito:** descripción del ámbito.  
        *  **Código área (M49):** es un código único por país.  
        *  **Área:** descripción del país.  
        *  **Código Elemento:** código único para los elementos.  
        *  **Elemento:** es la descripción de los distintos tipos de emisiones.  
        *  **Código Producto:** código único de productos.  
        *  **Producto:** descripción del producto relacionado a las distintas emisiones.  
        *  **Código año:** código único para el año.  
        *  **Año:** el número del año.  
        *  **Código fuente:** código único de la fuente de donde se obtienen los datos.  
        *  **Fuente:** descripción de la fuente de donde se obtienen los datos.  
        *  **Unidad:** unidad en la que están representados los datos.  
        *  **Valor:** corresponde al número del valor estimado u oficial.  
        *  **Símbolo:** corresponde a una codificación de si el valor es estimado u oficial.  
        *  **Descripción del Símbolo:** descripción del símbolo mencionado anteriormente.  
        *  **Nota:** comentario adicional en el caso que fuere, sobre los datos ene cuestión.  

        Dentro de los elementos que se pueden apreciar en el archivo, se incluyen los siguientes:

        *   Emisiones de Metano (CH4)
        *	Emisiones Dióxido de Carbono (CO2)
        *	Emisiones (CO2eq) (AR5)
        *	Emisiones (CO2eq) proveniente de CH4 (AR5)
        *	Emisiones (CO2eq) proveniente de F-gases (AR5)
        *	Emisiones (CO2eq) proveniente de N2O (AR5)
        *	Emisiones de Óxido Nitroso (N2O)
        *	Emisiones directas (N2O)
        *	Emisiones indirectas (N2O)

        Respecto a los os Productos que se incluyen en el Datase, se pueden mencionar los siguientes:

        *	Desechos
        *	Energía
        *	IPPU
        *	Otro
        *	Tanques de combustible internacional
        *	Consumo de alimentos en los hogares
        *	Conversión neta de bosques
        *	Cultivo del arroz
        *	Eliminación de desechos de sistemas agroalimentarios
        *	Envasado alimentario
        *	Estiércol aplicado a los suelos
        *	Estiércol depositado en las pasturas
        *	Fabricación de fertilizantes
        *	Fabricación de pesticidas
        *	Fermentación entérica
        *	Fertilizantes sintéticos
        *	Gestión del estiércol
        *	Incendios de sabana
        *	Incendios en suelos de turba
        *	Incendios forestales
        *	Uso de calor en la granja
        *	Uso de energía en la finca
        *	Otros sectores > (Lista)
        *	Quemado de residuos agrícolas
        *	Residuos agrícolas
        *	Suelos orgánicos drenados
        *	Tierras forestales
        *	Transformación de alimentos
        *	Transformación de alimentos
        *	Uso de electricidad en agrícola
        *	Venta de alimentos
        
        ## Observacion
        Por razones geopoliticas, como la aparicion y desaparicion de paises, se ha limitado el analisis
        que se vera en las siguiente paginas, al año 2000 en adelante.
        
        """
    )

###################################################

    end_time = datetime.datetime.now()
    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')