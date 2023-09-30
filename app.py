import requests

# OpenWeatherMap API URL
API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

# get a weathe data
def get_weather_data():
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

def get_temperature(weather_data, date_time):
    for data_point in weather_data['list']:
        if data_point['dt_txt'] == date_time:
            return data_point['main']['temp']
    return None

def get_wind_speed(weather_data, date_time):
    for data_point in weather_data['list']:
        if data_point['dt_txt'] == date_time:
            return data_point['wind']['speed']
    return None

def get_pressure(weather_data, date_time):
    for data_point in weather_data['list']:
        if data_point['dt_txt'] == date_time:
            return data_point['main']['pressure']
    return None

def main():
    weather_data = get_weather_data()
    if weather_data is None:
        return

    while True:
        print("\nMenu:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(weather_data, date_time)
            if temperature is not None:
                print(f"Temperature at {date_time}: {temperature} K")
            else:
                print("Data not found for the specified date and time.")
        elif choice == '2':
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(weather_data, date_time)
            if wind_speed is not None:
                print(f"Wind Speed at {date_time}: {wind_speed} m/s")
            else:
                print("Data not found for the specified date and time.")
        elif choice == '3':
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(weather_data, date_time)
            if pressure is not None:
                print(f"Pressure at {date_time}: {pressure} hPa")
            else:
                print("Data not found for the specified date and time.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
