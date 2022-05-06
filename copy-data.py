import shutil
import os

dates = [
    [[202107], [1, 2, 3, 4, 9, 10, 11, 12, 13, 15, 16, 17, 22,
                23, 26, 27, 28]],
    [[202108], [2, 7, 17, 18, 20, 21, 22, 23, 30]]
]

for i in range(len(dates)):
    # print(dates[i][0][0])
    for day in range(len(dates[i][1])):
        dayString = "%02d" % (dates[i][1][day],)
        # print(dayString)

        dateString = "" + str(dates[i][0][0]) + str(dayString)
        print(dateString)

        src_directory = "data-unzipped/" + dateString + "/hko_" + dateString + ".csv"

        dest = "data-nonrain-hko/"

        try:
            shutil.copy(src_directory, dest)
        except IOError as io_err:
            os.makedirs(os.path.dirname(dest))
            shutil.copy(src_directory, dest)
