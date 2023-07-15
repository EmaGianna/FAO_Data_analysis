import streamlit as st

if __name__ == '__main__':

    st.set_page_config(page_title="Conclusiones", page_icon="📝")
    st.markdown("# Conclusiones")
    st.sidebar.header("Conclusiones")
    st.sidebar.markdown("""
            Proyecto desarrollado por:
            * [Damian Mariescurrena](mailto:damianmariescurrena@gmail.com)
            * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
            """)

    st.markdown(
        """
        **Respecto a las conclusiones, cabe mencionar que han sido expuestas en base a los criterios de los analistas  
        y los analisis previamente realizados.**
        
        1. Se puede apreciar a traves de los analisis de correlacion, analisis de dispersion y las distintas graficas,  
        que las emisiones fueron en crecimiento  año tras año, en practicamente todas las agrupaciones correspondientes  
        a los paises del mundo, gases y productos (esto se puede visualizar al seleccionar el pais o paises de interes).

        2. A nivel mundial en el podio de los 5 paises que mas emiten gases efecto invernadero se encuentra  
        liderado por China y China Continental, EEUU, India y Rusia.
        
        3. A nivel mundial en el podio de los 5 paises que menos emiten gases efecto invernadero se encuentra  
        liderado por República Centroafricana, Bhután, Sáhara Occidental y Guam.
        
        4. De acuerdo al resultado que se visualiza en el modelo predictivo desarrollado, podemos afirmar,  
        que de continuarse con el nivel de emisiones actuales, la progresion de emisiones futuras, continuara  
        en franco crecimiento.

        5. Respecto a los productos que mas emiten GHG a nivel global se pueden enumerar los siguientes:  
        la Energía, Sistemas agroalimentarios, Emisiones en tierras agrícolas, IPCC Agricultura, AFOLU.
        
        6. Se puede apreciar que las Emisiones de mayor volumen a nivel global son las siguientes:  
        Emisiones (CO2eq) (AR5), Emisiones (CO2), Emisiones (CO2eq) proveniente de CH4 (AR5),Emisiones (CO2eq) proveniente de N2O (AR5).

        """
    )