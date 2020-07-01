from covid import Covid


cov = Covid()
data = cov.get_data()

country = cov.get_status_by_country_name("Bolivia")
print(country)

countries = cov.list_countries()

active = cov.get_total_active_cases()
print("Total active cases: ",active)

