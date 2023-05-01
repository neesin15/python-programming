def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days have {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days have {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days have {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "Unsupported unit"


def validate_and_execute():
    try:
        input_number = int(days_and_unit_dict["days"])
        if input_number > 0:
            calculated_value = days_to_units(input_number, days_and_unit_dict["unit"])
            print(calculated_value)
        elif input_number == 0:
            print("You have entered a 0, please enter a valid positive number")
        else:
            print("You have entered a negative number, please enter a valid positive number")
    except ValueError:
        print("Your input is not a valid number. please enter a valid number")


input_provided = ""
while input_provided != "exit":
    input_provided = input("Enter the number of days and unit you want to convert.\n"
                          "Allowed units are hours, minutes and seconds. For e.g. 4:hours. \n"
                          "Please exit to end.\n")
    if input_provided == "exit":
      quit()
    days_and_unit = input_provided.split(":")
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute()
