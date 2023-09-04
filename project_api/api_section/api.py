
import pandas as pd
from sodapy import Socrata


def get_dataset_from(database_url = 'www.datos.gov.co', database_api_key = 'ch4u-f3i5', departament_to_check = 'RISARALDA', municipality_to_check = 'BALBOA', crop_to_check = 'Caña panelera/azucar', limit_of_query = 5, **dictionary_with_keyword_arguments):
    # Crear un cliente (objeto) de Socrata
    client = Socrata(database_url, None)
    
    # Lista de columnas que deseas seleccionar
    columns_to_filter_in_database = "departamento, municipio, cultivo, topografia, ph_agua_suelo_2_5_1_0, f_sforo_p_bray_ii_mg_kg, potasio_k_intercambiable_cmol_kg"
    
    # Realiza la consulta con los parámetros $select, $where y $limit
    dataset_generated = client.get(database_api_key, 
                          select=columns_to_filter_in_database, 
                          where=f"departamento = '{departament_to_check}' AND municipio = '{municipality_to_check}' AND cultivo = '{crop_to_check}'",
                          limit=limit_of_query)
    return dataset_generated

def get_dataframe_from(dataset_generated):
    dataframe_created = pd.DataFrame.from_records(dataset_generated)
    return dataframe_created

def rename_columns_of_edaphic_variables_from(dataframe_created):
    dataframe_renamed = dataframe_created.rename(columns={'ph_agua_suelo_2_5_1_0': 'pH', 'f_sforo_p_bray_ii_mg_kg': 'fosforo', 'potasio_k_intercambiable_cmol_kg': 'potasio'})
    return dataframe_renamed

def clean_columns_of_edaphic_variables_from(dataframe_renamed):
    dataframe_renamed['pH'] = pd.to_numeric(dataframe_renamed['pH'], errors='coerce')
    dataframe_renamed['fosforo'] = pd.to_numeric(dataframe_renamed['fosforo'], errors='coerce')
    dataframe_renamed['potasio'] = pd.to_numeric(dataframe_renamed['potasio'], errors='coerce')
    dataframe_cleaned = dataframe_renamed
    return dataframe_cleaned

def calculate_medians_of_edaphic_variables_from(dataframe_cleaned):
    median_ph = dataframe_cleaned['pH'].median()
    median_phosphorus = dataframe_cleaned['fosforo'].median()
    median_potassium = dataframe_cleaned['potasio'].median()
    dictionary_with_edaphic_variables = {'median_pH': median_ph, 'median_phosphorus': median_phosphorus, 'median_potassium': median_potassium}
    return dictionary_with_edaphic_variables


