def get_parameters_to_query_in_database():
    departament_to_check = input("Department: ").upper()
    municipality_to_check = input("Municipality: ").upper()
    crop_to_check = input("Crop: ").capitalize()
    limit_of_query = int(input("Limit of query: "))
    dictionary_with_keyword_arguments = {'departament_to_check': departament_to_check,
                                         'municipality_to_check': municipality_to_check,
                                         'crop_to_check': crop_to_check,
                                         'limit_of_query': limit_of_query}
    return dictionary_with_keyword_arguments

def show_dataframe_from(dataframe_renamed):
    print(dataframe_renamed)

def show_medians_of_edaphic_variables_from(median_ph, median_phosphorus, median_potassium):
    print("\nMedians of edaphic variables of the crop:\n")
    print(f"Median of pH: {median_ph}")
    print(f"Median of phosphorus (fosforo): {median_phosphorus}")
    print(f"Median of potassium (potasio): {median_potassium}")
