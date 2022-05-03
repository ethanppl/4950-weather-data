import zipfile

for month in range(7, 9):
    monthString = "%02d" % (month,)
    for day in range(1, 32):
        # print(day)
        dayString = "%02d" % (day,)
        date = "2021-" + monthString + "-" + dayString
        path_to_zip_file = "data/" + "2021" + monthString + dayString + ".zip"

        directory_to_extract_to = "data-unzipped/"

        print("2021" + monthString + dayString)

        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)
