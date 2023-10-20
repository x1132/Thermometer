import time
from WeatherGet import Weathers
from line_notification import notify

TIME = 10
# 用來記錄使用者的Line權杖、取得天氣情報的API、城市。
users_data = [{
    "owm_api_key": "your_owm_api_key",
    "line_token": "your_line_token",
    "city_name": "your_city_name"
}]

def main():
    while True:
        for user_data in users_data:
            # 建立一個天氣類別
            weather_station = Weathers(user_data.get('owm_api_key'))
            # 取得使用者設定的城市
            weather_data = weather_station.get_data(user_data.get('city_name'))
            # notify方法會發送通知並回傳狀況代碼
            status_code = notify(user_data.get('line_token'), weather_data.temperature('celsius'))
            print(status_code)
        # 每過多少時間傳送一次通知
        time.sleep(TIME)

# 避免 Module 中的部分程式碼在「被引入」時執行
if __name__ == '__main__':
    main()