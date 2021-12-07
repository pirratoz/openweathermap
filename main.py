from tkinter import *
from datetime import datetime
import requests
import json

api_key = "0075cffc13c9d03e5e57b530abeca534"


def create_window():

    def get_weather():
        city_name = text_input.get()
        q = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")
        json_q, text_q = q.json(), q.text
        a = [city, weather, temperature, wind, country, dtime1, dtime2]
        b = ["Город: ", "Погода: ", "Температура: ", "Ветер: ", "Страна: ", "Восход: ", "Закат: "]
        [n.config(text=t) for n, t in zip(a, b)]
        if "city not found" in text_q:
            success_msg.config(text="Cтатус: Ошибка, город не найден")
            success_output.config(text="Ответ сервера:\n" + text_q)
        elif json_q["cod"] == 200:
            success_msg.config(text="Cтатус: Успех")
            success_output.config(text="Ответ сервера:\n" + json.dumps(json_q, indent=3))
            city.config(text=f'Город: {json_q["name"]}')
            weather.config(text=f'Погода: {json_q["weather"][0]["main"]}')
            temperature.config(text=f'Температура: {json_q["main"]["temp_min"]} °C')
            wind.config(text=f'Ветер: {json_q["wind"]["speed"]} м/c')
            country.config(text=f'Страна: {json_q["sys"]["country"]}')
            dtime1.config(text=f'Восход: {datetime.fromtimestamp(json_q["sys"]["sunrise"])}')
            dtime2.config(text=f'Закат: {datetime.fromtimestamp(json_q["sys"]["sunset"])}')
        else:
            success_msg.config(text="Cтатус: Ошибка, запрос не принят")
            success_output.config(text="Ответ сервера:\n" + text_q)

    window = Tk()
    window.title('Weather by Pavel Trushin'), window.geometry("600x800")
    success_msg, success_output = Label(text="Cтатус: Информация ещё не получена"), Label()
    success_output.place(x=300,y=20), success_msg.place(x=0, y=20)
    country, city, weather, temperature, wind, dtime1, dtime2 = Label(text="Страна: "), Label(text="Город: "),\
                                                                Label(text="Погода: "), Label(text="Температура: "),\
                                                                Label(text="Ветер: "), Label(text="Восход: "), \
                                                                Label(text="Закат: ")
    [n.place(x=0, y=x) for x, n in zip(range(60, 220, 20), [country, city, weather, temperature, wind, dtime1, dtime2])]
    text_input = Entry(width=48)
    text_input.place(x=0, y=250)
    Button(text="Запросить погоду", width=40, command=get_weather).place(x=0, y=270)
    window.mainloop()


if __name__ == "__main__":
    create_window()
