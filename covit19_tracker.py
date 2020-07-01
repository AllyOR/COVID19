from covid import Covid

cov = Covid()
data = cov.get_data()

specific_country = input("Enter a country: ")
country = cov.get_status_by_country_name(specific_country)
print(country)

countries = cov.list_countries()

active = cov.get_total_active_cases()
print("Global active cases: ",active)