import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from lib.df_functions import load_data
from lib.app_functions import return_condition, create_list_options, agrupation

if __name__ == '__main__':

    st.set_page_config(page_title="Analisis y Graficas", page_icon="📈")
    st.markdown("# Analisis y Graficas")
    st.sidebar.header("Analisis y Graficas")
    st.sidebar.markdown("""
            Proyecto desarrollado por:
            * [Damian Mariescurrena](mailto:damianmariescurrena@gmail.com)
            * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
            """)
    
    extract_path = "/tmp/emisiones"
    df = load_data(f'{extract_path}/Emisiones_Totales_S_Todos_los_Datos_Normalizado.csv')
    
    st.markdown(
     """
        En la paresente seccion podra realizar las siguientes acciones:  
        
       * Exploración Inicial de Datos.
       * Exploración en base a los filtros aplicados.

     """)
    
    st.header("Exploración Inicial")
    st.markdown("""
                Exploracion inicial por pais para ver como se encuentra la distribución  
                de las emisiones por cada area dentro de un mapa
                """)

    df_temp_fao= df[(df['ANO']>=2000)]
    df_agrup_area=df_temp_fao.groupby(['AREA'])[['VALOR']].sum().reset_index()

    fig = go.Figure(go.Choropleth(
        locations = df_agrup_area['AREA'],
        locationmode = "country names",
        z = df_agrup_area['VALOR'],
        text = df_agrup_area['AREA'],
        colorscale = 'blues',
        autocolorscale = False,
        reversescale = True,
        marker_line_color = '#efefef',
        marker_line_width = 0.7,
        #colorbar_ticksuffix = '%',
        colorbar_title = 'Emisiones',
        )
    )
    fig.update_layout(
        title_text = 'Emisiones acumuladas por País',
        showlegend = False,
        geo = dict(
            scope = 'world',
            resolution = 50,
            projection_type = 'equirectangular',
            showcoastlines = True,
            showocean = True,
            showcountries = True,
            oceancolor = '#eaeaea',
            lakecolor = '#000000',
            coastlinecolor = '#dadada'
        )
    )
    st.plotly_chart(fig)


    st.header("Exploración en base a los filtros aplicados")
    
    st.subheader("Selecciones los filtros deseados")
    list_areas, list_prod, list_elem, list_ano, list_fuente = create_list_options(df)
    area = st.multiselect('Elija Area/Pais: ', list_areas, list_areas[0])
    producto = st.multiselect('Elija Producto: ', list_prod, list_prod[0])
    elemento = st.multiselect('Elija un gas/elemento: ', list_elem, list_elem[0])
    condition = return_condition('df',area, producto, elemento)
    
    df_subset_fao = df[eval(condition)].reset_index(drop=True)
    st.dataframe(df_subset_fao)

    # Creo las tabs para cada pais
    tab_labels = df_subset_fao['AREA'].unique().tolist()
    tabs = st.tabs(tab_labels)
    for label, tab in zip(tab_labels, tabs):
        with tab:
            # Visualizaciones en distintos gráficos para ver distribuciones
            for elem in df_subset_fao['ELEMENTO'].unique().tolist():
                for prod in df_subset_fao['PRODUCTO'].unique().tolist():
                    df_subset_fao_area = df_subset_fao[(df_subset_fao['AREA']==label) & (df_subset_fao['ELEMENTO']==elem) & (df_subset_fao['PRODUCTO']==prod)]
                    if len(df_subset_fao_area) > 0:
                        st.info(f'Graficas para el filtro: {label}, {elem}, {prod}', icon="ℹ️")
                        # Matriz de correlación
                        correlation_matrix = df_subset_fao_area.corr(numeric_only=True)
                        fig_corr = px.imshow(correlation_matrix, color_continuous_scale='YlGnBu', title=f'Matriz de Correlación de {label} \nElemento: {elem} \nProducto: {prod}')
                        st.plotly_chart(fig_corr)
                        # Gráfico de contorno
                        fig_contour = px.scatter(df_subset_fao_area, x='ANO', y='VALOR', opacity=1, color='VALOR', title=f'Gráfico de Contorno de {label} \nElemento: {elem} \nProducto: {prod}')
                        st.plotly_chart(fig_contour)
                        # Gráfico scatter lmplot
                        fig_scatter = px.scatter(df_subset_fao_area, x='ANO', y='VALOR', trendline='ols', title=f'Gráfico Scatter de {label} \nElemento: {elem} \nProducto: {prod}')
                        st.plotly_chart(fig_scatter)
                    else:
                        st.warning(f'No hay datos a graficar para la combinacion de filtro: {label}, {elem}, {prod}', icon="⚠️")
