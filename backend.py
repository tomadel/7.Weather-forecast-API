import requests

API_KEY = "d610392fc9529e3ac3fbc794fb7016f0"

def get_data(place, forecast_days=None, weather_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if weather_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if weather_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return data

if __name__ == "__main__":
    get_data(place="Tokyo", forecast_days=3, weather_type="Temperature")