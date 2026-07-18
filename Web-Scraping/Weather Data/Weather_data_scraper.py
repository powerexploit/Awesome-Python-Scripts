from bs4 import BeautifulSoup as bs
import requests

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"

def get_weather(url):
	# setting the seesion details.
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    soup = bs(html.text, "html.parser")
    data = {}
    data['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    data['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    data['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    data['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    data['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    data['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    data['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    # complete week's weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        day_name = day.find("div", attrs={"class": "QrNVmd Z1VzSb"}).attrs['aria-label']
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        max_temp = temp[0].text
        min_temp = temp[2].text
        next_days.append({"name":day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
     
     
    data['next_days'] = next_days
    return data

if __name__ == "__main__":
    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
    DATA = get_weather(URL)
    print("Region", DATA["region"],"Now:", DATA["dayhour"])
    print(f"Temperature now: {DATA['temp_now']}°C")
    print("Current Weather:", DATA['weather_now'])
    print("Precipitation:", DATA["precipitation"])
    print("Humidity:", DATA["humidity"])
    print("Wind:", DATA["wind"])
    print("UPCOMING WEEK:")
    for dayweather in DATA["next_days"]:
        print("\n*", dayweather["name"], "*")
        print("Description:", dayweather["weather"])
        print(f"temperature->Max :{dayweather['max_temp']}°C,Min:{dayweather['min_temp']}°C")
