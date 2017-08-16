
def main():
    velocity = 38241
    starting_distance = 16637000000
    miles_to_km_conversion = 1.609344
    miles_to_au_conversion = 0.00000000107578
    speed_of_light = 2997924.58

    velocity_per_day = velocity * 24

    number_days = input("How many days have passed since 25/09/09: ")
    number_days_int = int(number_days)
    while number_days_int < 0:
        print("Invalid Input")
        number_days_int = int(input("How many days have passed since 25/09/09: "))
    current_distance_miles = starting_distance + velocity_per_day * number_days_int
    current_distance_km = current_distance_miles * miles_to_km_conversion
    current_distance_au = current_distance_km * miles_to_au_conversion
    radio_trip = current_distance_km / speed_of_light
    radio_trip_minute = radio_trip // 60
    radio_trip_second = radio_trip % 60
    print("""The Voyager 1 is currently {:.3f} miles ({:.3f}km, {:.3f} AU) from the Sun.
    It will take {:.0f} min {:.0f} sec for it to receive a radio signal""".format(current_distance_km, current_distance_miles, current_distance_au, radio_trip_minute, radio_trip_second))

main()
