import streamlit as st
from lib.df_functions import load_data_filterd_parquet


if __name__ == '__main__':

    st.set_page_config(page_title="Otros Datos de Interés", page_icon="✅")
    st.markdown("# Otros Datos de Interés")
    st.sidebar.header("Otros Datos de Interés")
    st.sidebar.markdown("""
            Proyecto desarrollado por:
            * [Damian Mariescurrena](mailto:damianmariescurrena@gmail.com)
            * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
            """)
    
    # URL del archivo
    #url = 'https://github.com/EmaGianna/FAO_Data_analysis/raw/main/file/FAO_filtered.parquet'
    df = st.session_state["key"]
    
    st.header("Otros Datos de Interés")
    
    st.markdown("""
                En esta sección de la web se encuentran otros datos de interés tomados desde el dataset suministrado por
                FAO
                """)
    
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7  = st.tabs(["Total de emisiones", "10 más emisores", "10 menos emisores", "Total de emisiones por gas",
                                              "Productos que más emiten", "Países que más emiten", "Productos que más emiten a nivel global"
                                              ])

    
    with tab1:
        st.subheader('Total de emisiones')
        total_emisiones = round(df['VALOR'].sum(),2)
        st.markdown(f'El total de emisiones a nivel global es de: {total_emisiones}')
    
    with tab2:
        # Cuales son los paises que más emiten y cuales los que menos emiten?
        df_paises_emisores = df.groupby(['AREA']).agg(cant_emisiones_x_pais=('VALOR', 'sum')).sort_values(by=['cant_emisiones_x_pais'], ascending=[False]).reset_index()
        df_paises_emisores['cant_emisiones_x_pais'] = df_paises_emisores['cant_emisiones_x_pais'].round(2)
        df_paises_emisores.columns = map(str.upper, df_paises_emisores.columns)
        st.markdown('Los 10 países con mayor nivel de emisión a nivel global son:\n')
        st.dataframe(df_paises_emisores.head(10).reset_index(drop=True))
        st.download_button(
        label="Descargue en la grilla de los 10 países mas emisores",
        data=df_paises_emisores.head(10).reset_index(drop=True).to_csv().encode('utf-8'),
        file_name='10_mas_emisores.csv',
        mime='text/csv',
        )

    with tab3:
        st.markdown('Los 10 países con menor nivel de emisión a nivel global son:\n')
        st.dataframe(df_paises_emisores.tail(10).reset_index(drop=True))
        st.download_button(
        label="Descargue en la grilla de los 10 países menos emisores",
        data=df_paises_emisores.head(10).reset_index(drop=True).to_csv().encode('utf-8'),
        file_name='10_menos_emisores.csv',
        mime='text/csv',
        )
    
    with tab4:
        df_cant_tot_x_gas = df.groupby(['ELEMENTO']).agg(cant_tot_x_gas_mundo=('VALOR', 'sum')).sort_values(by=['cant_tot_x_gas_mundo'], ascending=[False]).reset_index()
        df_cant_tot_x_gas['cant_tot_x_gas_mundo'] = df_cant_tot_x_gas['cant_tot_x_gas_mundo'].round(2)
        df_cant_tot_x_gas.columns = map(str.upper, df_cant_tot_x_gas.columns)
        st.markdown('La cantidad total de cada gas emitido a nivel mundial es:\n')
        st.dataframe(df_cant_tot_x_gas.reset_index(drop=True))
        st.download_button(
        label="Descargue el total de emisiones por gas",
        data=df_cant_tot_x_gas.reset_index(drop=True).to_csv().encode('utf-8'),
        file_name='tot_emi_x_gas.csv',
        mime='text/csv',
        )
    
    with tab5:
        df_prod_mas_emision_mundo = df.groupby(['PRODUCTO']).agg(prod_x_emision_mundo=('VALOR', 'sum')).sort_values(by=['prod_x_emision_mundo'], ascending=[False]).reset_index()
        df_prod_mas_emision_mundo['prod_x_emision_mundo'] = df_prod_mas_emision_mundo['prod_x_emision_mundo'].round(2)
        df_prod_mas_emision_mundo.columns = map(str.upper, df_prod_mas_emision_mundo.columns)
        st.markdown('La tabla siguiente muestra los productos que más GHG emiten a nivel mundial:\n')
        st.dataframe(df_prod_mas_emision_mundo.reset_index(drop=True))
        st.download_button(
        label="Descargue el los productos que más emiten a nivel global",
        data=df_prod_mas_emision_mundo.reset_index(drop=True).to_csv().encode('utf-8'),
        file_name='prod_mas_emiten_mundo.csv',
        mime='text/csv',
        )
    
    with tab6:
        df_emisiones_area = df.groupby(['AREA']).agg(EMISIONES_PAIS=('VALOR', 'sum')).sort_values(by=['EMISIONES_PAIS'], ascending=[False]).reset_index()
        st.markdown('La tabla siguiente muestra los países que más GHG emiten a nivel mundial:\n')
        st.dataframe(df_emisiones_area.reset_index(drop=True))
        st.download_button(
        label="Descargue los países que más emiten a nivel global",
        data=df_emisiones_area.reset_index(drop=True).to_csv().encode('utf-8'),
        file_name='paises_mas_emiten_mundo.csv',
        mime='text/csv',
        )
    
    
    with tab7:
        st.markdown('La tabla siguiente muestra los productos que más GHG emiten, de cada país a nivel global:\n')
        df_prod_mas_emision_x_pais_mundo = df.groupby(['PRODUCTO','AREA']).agg(prod_mas_emision_mundo_x_pais=('VALOR', 'sum')).sort_values(by=['AREA', 'PRODUCTO']).reset_index()
        df_prod_mas_emision_x_pais_mundo['prod_mas_emision_mundo_x_pais'] = df_prod_mas_emision_x_pais_mundo['prod_mas_emision_mundo_x_pais'].round(2)
        df_prod_mas_emision_x_pais_mundo_max = df_prod_mas_emision_x_pais_mundo.loc[df_prod_mas_emision_x_pais_mundo.groupby('AREA')['prod_mas_emision_mundo_x_pais'].idxmax()].reset_index(drop=True)
        df_prod_mas_emision_mundo.columns = map(str.upper, df_prod_mas_emision_mundo.columns)
        st.dataframe(df_prod_mas_emision_mundo.reset_index(drop=True))
        st.download_button(
        label="Descargue los GHG que más emite cada país",
        data=df_emisiones_area.reset_index(drop=True).to_csv().encode('utf-8'),
        file_name='mayor_ghg_emitido_x_pais.csv',
        mime='text/csv',
        )