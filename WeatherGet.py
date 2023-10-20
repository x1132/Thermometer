from pyowm import OWM

# 藉由這個類別取得天氣資料
class Weathers():
    def __init__(self, owm_api_key):
        self._owm_api_key = owm_api_key
        self._owm = None
        self._mgr = None

    # 唯讀屬性
    @property
    def mgr(self):
        self._owm = OWM(self._owm_api_key)
        self._mgr = self._owm.weather_manager()
        return self._mgr

    def get_data(self, city_name):
        observation = self.mgr.weather_at_place(city_name)
        weather_data = observation.weather
        return weather_data

def main():
    api_key = 'your_owm_api_key'
    city_name = 'Tokyo,JP'
    weather_data = Weathers(api_key).get_data(city_name)
    print(type(weather_data))
    print(weather_data)
    print(weather_data.detailed_status)
    print(weather_data.temperature('celsius'))

# 當這個程式作為模組被運行時，不會執行以下內容
# 避免 Module 中的部分程式碼在「被引入」時執行
if __name__ == '__main__':
    main()
