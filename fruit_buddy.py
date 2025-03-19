import pandas as pd

# Load the CSV file into a DataFrame
file_path = '/home/dheepan/Projects/Experiments/HealthBuddy/indian_fruits_nutrition_100.csv'
df = pd.read_csv(file_path)

def query_data(key_nutrient=None, health_benefit=None, organ_benefited=None):
    # Filter the DataFrame based on the provided criteria
    filtered_df = df.copy()
    
    if key_nutrient:
        filtered_df = filtered_df[filtered_df['Key Nutrients'].str.contains(key_nutrient, case=False, na=False)]
    
    if health_benefit:
        filtered_df = filtered_df[filtered_df['Health Benefits'].str.contains(health_benefit, case=False, na=False)]
    
    if organ_benefited:
        filtered_df = filtered_df[filtered_df['Organs Benefited'].str.contains(organ_benefited, case=False, na=False)]
    
    return filtered_df

def display_results(results):
    if results.empty:
        print("No results found.")
    else:
        print(results.to_markdown(index=False))

# Example queries
key_nutrient_query = input("Enter Nutrient, eg:Vitamin E\t:")
health_benefit_query = input("Health Benefit, eg:blood pressure\t:")
organ_benefited_query = input("Organ to be benefited, eg:gut\t:")

# Query the data
results = query_data(key_nutrient=key_nutrient_query, health_benefit=health_benefit_query, organ_benefited=organ_benefited_query)

# Display the results
display_results(results)
