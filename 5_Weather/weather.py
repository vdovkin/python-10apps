import requests
import bs4


def main():
    start()
    name_city = get_city()
    html = get_html_from_web(name_city)
    report = get_weather_from_html(html)
    print("The temp in {} is {}".format(name_city, report))


def start():
    print("********************")
    print("  weather app")
    print("********************")


def get_city():
    while True:
        city = input("Please enter the city: ").strip().lower()
        if not city or not city.isalpha():
            print("Wrong input")
        else:
            return city


def get_html_from_web(name):
    url = "https://sinoptik.ua/погода-{}".format(name)
    response = requests.get(url)
    if response.status_code != 200:
        print("Wrong name of the city")
        exit()
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "lxml")
    temp = soup.find(class_="today-temp").get_text()
    return temp


if __name__ == "__main__":
    main()

