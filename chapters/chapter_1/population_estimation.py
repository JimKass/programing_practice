
def main():
    current_population = 307357870
    seconds_per_birth = 7
    seconds_per_death = 13
    seconds_per_immigrants = 35
    seconds_per_year = 31536000

    deaths_per_year = seconds_per_year / seconds_per_death
    births_per_year = seconds_per_year / seconds_per_birth
    immigrants_per_year = seconds_per_year / seconds_per_immigrants

    years_passed = int(input("How many years have passed: "))

    new_population = current_population + years_passed * (births_per_year + immigrants_per_year - deaths_per_year)

    print("The current population is {:.2f}".format(new_population))

main()
