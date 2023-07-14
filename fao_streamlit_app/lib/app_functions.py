from loguru import logger

def return_condition(name_df, area_selected=False, prod_selected=False, elem_selected=False, ano_selected=False, fuente_selected=False):
    """
    The function `return_condition` takes in several boolean parameters and returns a string that
    represents a set of conditions based on the selected parameters.

    :param area_selected: A list of selected areas, defaults to False (optional)
    :param prod_selected: A list of selected products, defaults to False (optional)
    :param elem_selected: A list of selected elements, defaults to False (optional)
    :param ano_selected: A list of selected years, defaults to False (optional)
    :param fuente_selected: A list of selected sources, defaults to False (optional)
    :return: a string that represents a set of conditions based on the selected parameters.
    """
    conditions = []
    if area_selected:
        conditions.append(f"({name_df}['AREA'].isin({area_selected}))")
    if prod_selected:
        conditions.append(f"({name_df}['PRODUCTO'].isin({prod_selected}))")
    if elem_selected:
        conditions.append(f"({name_df}['ELEMENTO'].isin({elem_selected}))")
    if ano_selected:
        conditions.append(f"({name_df}['ANO'].isin({ano_selected}))")
    if fuente_selected:
        conditions.append(f"({name_df}['FUENTE'].isin({fuente_selected}))")
    logger.info(f"Condition to apply {' & '.join(conditions)}.")
    
    return " & ".join(conditions)


def create_list_options(df):
    """
    The function "create_list_options" takes a DataFrame as input and returns lists of unique values for
    the 'AREA', 'PRODUCTO', 'ELEMENTO', 'ANO', and 'FUENTE' columns.

    :param df: The parameter `df` is a pandas DataFrame that contains the data from which you want to
    create the list options. It is assumed that the DataFrame has columns named 'AREA', 'PRODUCTO',
    'ELEMENTO', 'ANO', and 'FUENTE'
    :return: a tuple containing five lists: list_areas, list_prod, list_elem, list_ano, and list_fuente.
    """
    list_areas = df['AREA'].unique().tolist()
    list_prod = df['PRODUCTO'].unique().tolist()
    list_elem = df['ELEMENTO'].unique().tolist()
    list_ano = df['ANO'].unique().tolist()
    list_fuente = df['FUENTE'].unique().tolist()
    logger.info("Conditions to apply list created.")
    return list_areas, list_prod, list_elem, list_ano, list_fuente


def agrupation(df,filters_fields):
    """
    The function `agrupation` groups a DataFrame `df` by specified fields `filters_fields` and
    calculates the sum of the 'VALOR' column, and returns the result as a new DataFrame with a column
    name based on the filters fields.
    
    :param df: The parameter `df` is a pandas DataFrame that contains the data you want to aggregate
    :param filters_fields: filters_fields is a list of fields that will be used for grouping the data in
    the dataframe
    :return: a DataFrame called `df_agg` with the aggregated values of the 'VALOR' column. If
    `filters_fields` is an empty list, the aggregation is done without grouping, and the resulting
    column is named 'VALOR_SUM_AGR_X'. If `filters_fields` is not empty, the aggregation is done by
    grouping the DataFrame by the specified fields, and the resulting column
    """

    field_name = f'VALOR_SUM_X_AGR_{"_".join(filters_fields)}'

    if filters_fields==[]:
        df_agg = df.agg(VALOR_SUM_AGR_X=('VALOR', 'sum')).sort_values(by=filters_fields).reset_index()
    else:
        df_agg = df.groupby(filters_fields).agg(VALOR_SUM_AGR_X=('VALOR', 'sum')).sort_values(by=filters_fields).reset_index()
    logger.info("Has been grouped by {filters_fields}")
    return  df_agg.rename(columns={'VALOR_SUM_AGR_X': field_name})


def anos_prediccion(df):
    maximo = max(df['ANO'].unique().tolist()) + 1
    limite_superior = 2070
    valores = []
    # Generar valores hasta alcanzar el año límite
    while (maximo + 1) <= limite_superior:
        maximo += 1
        valores.append(maximo)
    return valores


