import requests

# OpenWeatherMap API URL
API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

# get a weather data
def getAllWeatherData():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: Unable to fetch weather data from the API.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# get a temparature by date
def getTemparatureByDate(weather_data, date_time):
    for data_point in weather_data['list']:
        if data_point['dt_txt'] == date_time:
            return data_point['main']['temp']
    return None

# get a wind spedd be date
def getWindSpeedByDate(weather_data, date_time):
    for data_point in weather_data['list']:
        if data_point['dt_txt'] == date_time:
            return data_point['wind']['speed']
    return None

# get a pressure data by date
def getAirPressureByDate(weather_data, date_time):
    for data_point in weather_data['list']:
        if data_point['dt_txt'] == date_time:
            return data_point['main']['pressure']
    return None

def main():
    weather_data = getAllWeatherData()
    if weather_data is None:
        return

# choose options to get data
    while True:
        print("\nMenu:")
        print("1. Get Temperature by date and time")
        print("2. Get Wind Speed by date and time")
        print("3. Get Pressure by date and time")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            break

        # choice get temperature

        elif choice == '1':
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = getTemparatureByDate(weather_data, date_time)
            if temperature is not None:
                print(f"Temperature at {date_time}: {temperature} Kelvin")
            else:
                print("Data not found for the specified date and time.")

        # choice to get a data of wind speed

        elif choice == '2':
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = getWindSpeedByDate(weather_data, date_time)
            if wind_speed is not None:
                print(f"Wind Speed at {date_time}: {wind_speed} meter/sec")
            else:
                print("Data not found for the specified date and time.")

        # choice to get air pressure of the perticular date
        elif choice == '3':
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = getAirPressureByDate(weather_data, date_time)
            if pressure is not None:
                print(f"Air pressure at {date_time}: {pressure} pascal")
            else:
                print("Data not found for the specified date and time.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
