import requests
import sys

# If you want your own private_token please refer the README file for this script.
private_token = "<Your Private Token>"

while True:
    choice = input(
        "Type G for geocoding , type R for reverse geocoding and type Q to quit the script:")
    print()

    # If the user choose to perform Geocoding
    if choice.upper() == 'G':
        # Base Url for geocoding
        url = "https://us1.locationiq.com/v1/search.php"

        address = input("Input the address: ")

        # Parameters for the geocoding url
        data = {
            'key': private_token,
            'q': address,
            'format': 'json'
        }

        response = requests.get(url, params=data)

        # To run only if we get success response
        if response.status_code == 200:
            latitude = response.json()[0]['lat']
            longitude = response.json()[0]['lon']

            print(f"The latitude of the given address is: {latitude}")
            print(f"The longitude of the given address is: {longitude}")
            print()
        else:
            sys.exit("Cant find what you where looking for")

    # If the user choose to perform Reverse Geocoding
    elif choice.upper() == 'R':
        # Base Url for reverse geocoding
        url = "https://us1.locationiq.com/v1/reverse.php"

        latitude_reverse = input("Enter the latitude: ")
        longitude_reverse = input("Enter the longitude: ")

        # Parameters for the reverse geocoding url
        data = {
            'key': private_token,
            'lat': latitude_reverse,
            'lon': longitude_reverse,
            'format': 'json'
        }

        response = requests.get(url, params=data)

        # To run only if we get success response
        if response.status_code == 200:
            address = response.json()['display_name']
            print(f"The address is: {address}")
            print()
        else:
            print("Cant find what you where looking for.")

    # If the user choose to Quit the program
    elif choice.upper() == 'Q':
        sys.exit("Thanks for using the script")

    # To make sure only valid input is provided
    else:
        print("Please make a valid choice")
        print()

#Sample Input - Output:

#If you choose Geocoding:

#Address(Input): Rashtrapati Bhavan
#Latitude(Output): 28.614458
#Longitude(Output): 77.199594

#If you choose Reverse-Geocoding:

#Latitude(Input): 28.614458
#Longitude(Input): 77.199594
#Address(Output): Rashtrapati Bhavan, Rajpath, Presidential Estate, Chanakya Puri Tehsil, New Delhi, Delhi, 110004, India        
