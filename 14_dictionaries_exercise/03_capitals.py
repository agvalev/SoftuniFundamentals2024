countries = input().split(", ")
capitals = input().split(", ")

country_capital_dict = dict(zip(countries, capitals))

for c, cap in country_capital_dict.items():
    print(f"{c} -> {cap}")