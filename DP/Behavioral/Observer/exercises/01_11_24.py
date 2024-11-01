# Exercise #1)
# 1. Create a WeatherData class (the Publisher) that stores temperature, humidity, and pressure. It should have methods to set_measurements() and notify_observers().
# 3. Create an Observer inteface with an update() method.
# 3. Create several observer classes, such as CurrentConditionsDisplay, StatisticsDisplay, and ForecastDisplay, each implementing the Observer interface. These
# observers will display the weather data in different formats.
# 4. Register the observers with the WeatherData class using an attach() method.
# 5. Update the weather data using the set_measurements() method. This should trigger the notify_observers() method, which in turn calls the update()
# method for each registered observer.
# 6. Each observer should display the updated weather data in its own format.
# 7. Draw a UML diagram
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, weather_data) -> None: 
        pass
class CurrentConditionsDisplay(Observer):
    def update(self, weather_data) -> None: 
        print(f"[Current Conditions] Temperature: {weather_data.temperature}°C, Humidity: {weather_data.humidity}%, Pressure: {weather_data.presure}hPa")

class StatisticsDisplay(Observer):
    def update(self, weather_data) -> None: 
        # Przykład na wyświetlanie statystyk - w rzeczywistej aplikacji moglibyśmy przechowywać historię danych
        print(f"[Statistics] Average Temperature: {weather_data.temperature}°C, Average Humidity: {weather_data.humidity}%, Average Pressure: {weather_data.presure}hPa")

class ForecastDisplay(Observer):
    def update(self, weather_data) -> None: 
        # Przykład prostej prognozy na podstawie danych ciśnienia
        forecast = "Improving weather" if weather_data.presure > 10 else "Expect more of the same"
        print(f"[Forecast] Forecast based on pressure ({weather_data.presure}hPa): {forecast}")


class WeatherData:
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.presure = 0.0

        self._observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.presure = pressure
        self.notify_observers()
    
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self)

wd = WeatherData()
wd.attach(CurrentConditionsDisplay())
wd.attach(StatisticsDisplay())
wd.attach(ForecastDisplay())

wd.set_measurements(**{
    "temperature": 25.5,
    "humidity": 40.1,
    "pressure": 11.1,
})


# Exercise #2)
# 1. Create a Stock class that stores the stock's symbol, price, and the change in
# price. It should have methods to set_price() and notify_observers().
# 2. Create an Observer interface with an update() method.
# 3. Create several observer classes, such as PriceDisplay and ChangeDisplay, each implementing the Observer interface. These observers will display
# the stock data in different formats.
# 4. Register the observers with the Stock class using an attach() method.
# 5. Update the stock data using the set_price() method. This should trigger the notify_observers() method, which in turn calls the update() method
# for each registered observer.
# 6. Each observer should display the updated stock data in its own format.
# 7. Ddraw a UML diagram.
