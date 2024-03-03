#....................Task 14......................................
#........Implementing user defined function.......................

def hotel_cost(num_nights):                         #define function hotel_cost with 1 argument 
    return num_nights * 120                         # per_night cost of hotel is £120

def plane_cost(city_flight):                        #define function plane_cost with 1 argument
    if city_flight.capitalize() == "Paris":                      #Option for city flight with cost
        return 500
    elif city_flight.capitalize() == "London":     
        return 800
    elif city_flight.capitalize() == "India" : 
        return 1000  
    
        #else:           
            #return                                         # Use a default cost for unknown cities

def car_rental(rental_days):                          #define function car_rental with 1 argument
    return rental_days * 30                           # Replace with your desired daily cost

def holiday_cost(hotel_cost, plane_cost, car_rental):  #define function holiday cost with 3 arguments
    return hotel_cost + plane_cost + car_rental        #return total cost of holiday
while True:
    try:
            # Get user input
            city_flight = input("Enter city you're flying to: ")
            num_nights = int(input("Enter number of nights staying: "))
            rental_days = int(input("Enter number of days renting a car: "))

            # Calculate individual costs 
            hotel_cost_result = hotel_cost(num_nights)
            plane_cost_result = plane_cost(city_flight)
            car_rental_result = car_rental(rental_days)

            # Calculate total cost
            total_cost = holiday_cost(hotel_cost_result, plane_cost_result, car_rental_result)

            # Print results in a readable format
            print(f"Summary of your holiday trip:")
            print(f"  City: {city_flight}")
            print(f"  Nights staying: {num_nights}")
            print(f"  Days renting car: {rental_days}")
            print(f"  Hotel cost: {hotel_cost_result}")
            print(f"  Plane cost: {plane_cost_result}")
            print(f"  Car rental cost: {car_rental_result}")
            print(f"  Total holiday cost: {total_cost}")
    except:
            print("please enter available city")
            break