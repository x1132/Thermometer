import requests
LINE_URL = 'https://notify-api.line.me/api/notify'

# 把文字列中需要的資料整理出來
def _enrich_message(msg):
    return str({
        'temp': msg.get('temp', 'Null'),
        'temp_max': msg.get('temp_max', 'Null'),
        'temp_min': msg.get('temp_min', 'Null'),
    })

# 呼叫API傳送通知到LINE
def notify(token, msg):
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message':_enrich_message(msg)}
    response = requests.post(LINE_URL, headers=headers, data=payload)
    return response.status_code


def main():
    line_token = 'your_line_token'
    msg = {'temp': 24.08, 'temp_max': 24.95, 'temp_min': 22.79, 'feels_like': 23.88, 'temp_kf': None}
    status_code = notify(line_token, msg)
    print(status_code)

# 避免 Module 中的部分程式碼在「被引入」時執行
if __name__ == '__main__':
    main()
