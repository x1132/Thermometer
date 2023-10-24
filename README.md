WeatherBroadcaster.py是主程式

line_notification.py是連接LINE API方法

WeatherGet.py是創建了一個類別，用來取得天氣資料

主程式中的users_data陣列用來記錄使用者資料，TIME用來決定每隔多少時間送一次通知，接下來利用迴圈讀取使用者，並創建一個天氣類別，然後天氣類別就可以透過天氣API_KEY以及城市取得天氣資料(這邊我只取氣溫的資料)，這時候已經拿到資料了，這時候我就可以利用Python的requests請求LINE發送通知。

WeatherBroadcaster.py is the main program.

line_notification.py is a script that connects to the LINE API.

WeatherGet.py is a script that creates a class for retrieving weather data.

The main program uses the users_data array to store user information. TIME is used to determine how often notifications should be sent. The program then goes through a loop to read users' data. It creates an instance of a weather class, which can retrieve weather data (in this case, only temperature) by using the API_KEY and the city. Once the data is obtained, you can use Python's requests to send notifications to LINE.

WeatherBroadcaster.py はメインプログラムです。

line_notification.py はLINE APIに接続するスクリプトです。

WeatherGet.py は天気データを取得するためのクラスを作成するスクリプトです。

メインプログラム内の users_data 配列はユーザー情報を記録するために使用されます。TIME は通知を送信する間隔を決定します。次に、ループを使用してユーザーを読み込み、天気データを取得するクラスを作成します。この天気クラスは、Weather API_KEYと都市を使用して天気データ（ここでは気温のデータのみ）を取得します。データを取得すると、Pythonのrequestsを使用してLINEに通知を送信できます。

參考資料(Reference materials):

https://medium.com/@a4793706/python-%E5%A4%A9%E6%B0%A3%E6%92%AD%E5%A0%B1%E5%93%A1-%E5%AF%A6%E4%BD%9Cside-project%E6%8F%90%E5%8D%87%E5%AF%ABcode%E7%9A%84%E8%83%BD%E5%8A%9B-%E4%B8%8A-2a58203e9773

這個教學非常實用，有助於理解把想法具現化。(不好意思擅自附上您的連結，如果造成您的困擾，請通知我)

https://pyowm.readthedocs.io/en/latest/

https://openweathermap.org/current

https://notify-bot.line.me/doc/en/

