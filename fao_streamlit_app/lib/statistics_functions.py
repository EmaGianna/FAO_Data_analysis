import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import pandas as pd 

def simple_forecast_statsmodel(df, futur_year):
    """
    The function `simple_forecast_statsmodel` takes a dataframe and a future year as input, performs a
    simple linear regression using the statsmodels library, and returns predictions for the specified
    future year.

    :param df: The parameter `df` is a pandas DataFrame that contains the historical data for which you
    want to make predictions. It should have the following columns:
    :param futur_year: The `futur_year` parameter is the year for which you want to make predictions.
    The function will use the existing data in the `df` DataFrame to build a model and then use that
    model to predict values for the specified future year
    :return: a DataFrame containing the predicted values for a future year, based on a simple
    forecasting model using the statsmodels library. The DataFrame includes columns for the year, value,
    area, product, element, source, unit, and symbol.
    """

    df = df.sort_values(by='ANO')
    X = df[['ANO']]
    y = df['VALOR']

    X = sm.add_constant(X)

    model = sm.OLS(y, X)
    results = model.fit()

    ultimo_año = df['ANO'].max()
    nuevos_años = pd.DataFrame({'ANO': range(ultimo_año+1, futur_year+1)})
    nuevos_años = sm.add_constant(nuevos_años)
    predicciones = results.predict(nuevos_años)

    predicciones = pd.concat([nuevos_años['ANO'], predicciones], axis=1)
    predicciones.columns = ['ANO', 'VALOR']
    predicciones['AREA'] = df['AREA'].unique().tolist()[0]
    predicciones['PRODUCTO'] = df['PRODUCTO'].unique().tolist()[0]
    predicciones['ELEMENTO'] = df['ELEMENTO'].unique().tolist()[0]
    predicciones['FUENTE'] = 'CALCULO MODELO PREDICTIVO FORECASTING'
    predicciones['UNIDAD'] = df['UNIDAD'].unique().tolist()[0]
    predicciones['SIMBOLO'] = df['SIMBOLO'].unique().tolist()[0]

    columnas_orden = df.columns.tolist()
    predicciones = predicciones.reindex(columns=columnas_orden)

    return predicciones


def simple_forecast_sickit_learn(df, futur_year):
    """
    The function `simple_forecast_sickit_learn` takes a dataframe with historical data and a future year
    as input, and uses linear regression to predict values for the future year.

    :param df: The parameter `df` is a pandas DataFrame that contains the historical data for
    forecasting. It should have the following columns:
    :param futur_year: The "futur_year" parameter represents the year for which you want to make a
    forecast. It is the year in the future for which you want to predict the value of the target
    variable
    :return: a DataFrame containing the predicted values for the specified future years, based on a
    linear regression model trained on the input DataFrame. The returned DataFrame has the same columns
    as the input DataFrame, with the addition of the predicted values for the future years.
    """

    df = df.sort_values(by='ANO')

    X = df[['ANO']]
    y = df['VALOR']

    model = LinearRegression()
    model.fit(X, y)

    ultimo_año = df['ANO'].max()
    nuevos_años = pd.DataFrame({'ANO': range(ultimo_año+1, futur_year+1)})
    predicciones = model.predict(nuevos_años)

    predicciones = pd.DataFrame({'ANO': nuevos_años['ANO'], 'VALOR': predicciones})

    predicciones['AREA'] = df['AREA'].unique().tolist()[0]
    predicciones['PRODUCTO'] = df['PRODUCTO'].unique().tolist()[0]
    predicciones['ELEMENTO'] = df['ELEMENTO'].unique().tolist()[0]
    predicciones['FUENTE'] = 'CALCULO MODELO PREDICTIVO FORECASTING'
    predicciones['UNIDAD'] = df['UNIDAD'].unique().tolist()[0]
    predicciones['SIMBOLO'] = df['SIMBOLO'].unique().tolist()[0]

    columnas_orden = df.columns.tolist()

    predicciones = predicciones.reindex(columns=columnas_orden)

    return predicciones