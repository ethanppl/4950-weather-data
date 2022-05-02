import re
import requests

# https://i-lens.hk/hkweather/file_download.php?file_type=history_minute_record&file=2021-07-10
url_base = "https://i-lens.hk/hkweather/file_download.php?file_type=history_minute_record&file="

for month in range(7, 9):
    monthString = "%02d" % (month,)
    for day in range(1, 32):
        # print(day)
        dayString = "%02d" % (day,)
        date = "2021-" + monthString + "-" + dayString
        fileName = "data/" + "2021" + monthString + dayString + ".zip"
        url = url_base + date

        print(fileName)

        r = requests.get(url, allow_redirects=True)

        open(fileName, 'wb').write(r.content)
