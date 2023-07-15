import streamlit as st
import plotly.express as px
import pandas as pd
from lib.df_functions import load_data_filterd_parquet
from lib.app_functions import return_condition, create_list_options, anos_prediccion
from lib.statistics_functions import simple_forecast_statsmodel, simple_forecast_sickit_learn


if __name__ == '__main__':

    st.set_page_config(page_title="Modelo Predictivo Basico", page_icon="📊")
    st.markdown("# Modelo Predictivo Basico")
    st.sidebar.header("Modelo Predictivo Basico")
    st.sidebar.markdown("""
            Proyecto desarrollado por:
            * [Damian Mariescurrena](mailto:damianmariescurrena@gmail.com)
            * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
            """)
    
    # URL del archivo
    #url = 'https://github.com/EmaGianna/FAO_Data_analysis/raw/main/file/FAO_filtered.parquet'
    df = st.session_state["key"]
    
    st.markdown("""
                En esta seccion de la web, podra realizar un filtro de datos. Ademas, podra seleccionar del despleglable un año  
                a fin de realizar una prediccion del crecimiento de emision de GHG.
                """)
    
    
    st.subheader("Selecciones los filtros deseados")
    list_areas, list_prod, list_elem, list_ano, list_fuente = create_list_options(df)
    area = st.multiselect('Elija Area/Pais: ', list_areas, list_areas[0])
    producto = st.multiselect('Elija Producto: ', list_prod, list_prod[0])
    elemento = st.multiselect('Elija un gas/elemento: ', list_elem, list_elem[0])
    ano = st.multiselect('Elija un año: ', list_ano, list_ano[:2])
    condition = return_condition('df',area, producto, elemento, ano)
    
    df_subset_fao = df[eval(condition)].reset_index(drop=True)
    st.dataframe(df_subset_fao)
   
    if len(ano) >=2:
        list_ano_pred = tuple(anos_prediccion(df_subset_fao))
        anio = st.selectbox('Elija un año a futuro para ver prediccion: ', list_ano_pred)
        tab_labels = df_subset_fao['AREA'].unique().tolist()
        tabs = st.tabs(tab_labels)
        
        
        for label, tab in zip(tab_labels, tabs):
            df_subset_fao_aux = df_subset_fao[df_subset_fao['AREA']==label]
            with tab:
                df_predicciones = pd.DataFrame()
                for elem in df_subset_fao_aux['ELEMENTO'].unique().tolist():
                  for prod in df_subset_fao_aux['PRODUCTO'].unique().tolist():
                    df_predicciones_aux = df_subset_fao_aux[(df_subset_fao_aux['AREA']==label) & (df_subset_fao_aux['ELEMENTO']==elem) & (df_subset_fao_aux['PRODUCTO']==prod)]
                    if len(df_predicciones_aux)> 0:
                      df_predicciones_aux = simple_forecast_statsmodel(df_predicciones_aux, anio)
                      df_predicciones = pd.concat([df_predicciones, df_predicciones_aux], axis=0).reset_index(drop=True)
        
                df_final_with_stats = pd.concat([df_subset_fao_aux, df_predicciones], axis=0).sort_values(by=['AREA','PRODUCTO','ELEMENTO'], ascending=False).reset_index(drop=True)
                st.dataframe(df_final_with_stats)

                fig_bar = px.bar(df_final_with_stats
                             , x='ANO'
                             , y='VALOR'
                             ,color="ANO"
                             ,color_continuous_scale='Blues'
                             ,labels={'ANO': 'Año', 'VALOR': 'Emisiones en miles de toneladas'}
                             ,title=f'Proyeccion de emisiones futuras de {elemento} en {label}'
                            )
                st.plotly_chart(fig_bar)

                fig_treemap = px.treemap(df_final_with_stats,
                                 path=['ELEMENTO','AREA','PRODUCTO','ANO'],
                                 values='VALOR',
                                 color='VALOR',
                                 color_continuous_scale='Blues',
                                 title=f'Mapa de calor de emisiones futuras de {elemento} en {label}'
                                 )
                st.plotly_chart(fig_treemap)
    else:
        st.error('Debe elegir al menos 2 años del combo de años', icon="🚨")