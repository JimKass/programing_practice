
def main():
    oil_to_gas_conversion = 19.5
    gas_to_oil_conversion = 1/oil_to_gas_conversion
    CO2_per_gallon = 20
    energy_per_gasoline = 115000
    energy_per_ethanol = 75700
    cost_per_gallon = 3.00

    gallons_of_gasoline = float(input("Enter the amount of gasoline (in gallons): "))
    litres_of_gasoline = gallons_of_gasoline * 3.78541
    gallons_of_oil = gallons_of_gasoline * gas_to_oil_conversion
    pounds_of_C02 = gallons_of_gasoline * CO2_per_gallon
    gallons_to_energy = gallons_of_gasoline * energy_per_gasoline
    ethanol_energy = gallons_of_gasoline * energy_per_ethanol
    cost_of_gasoline = gallons_of_gasoline * cost_per_gallon

    print("""Gallons of gasoline: {:.2f} gln
    Litres of gasoline: {:.2f}
    Gallons of oil: {:.2f}
    Pounds of CO2: {:.2f}
    Creates {} BTU of energy
    Creates {} BTU of energy if ethanol
    Total cost of oil {}""".format(gallons_of_gasoline, litres_of_gasoline, gallons_of_oil, pounds_of_C02, gallons_to_energy, ethanol_energy, cost_of_gasoline))

main()