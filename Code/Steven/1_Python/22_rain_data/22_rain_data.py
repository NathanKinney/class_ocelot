import matplotlib.pyplot as plt
import string, re, datetime, requests

# get data from web
url = 'https://or.water.usgs.gov/non-usgs/bes/'
def get_locations():
    r = requests.get(url)
    locations = re.findall(r'\w+\.rain', r.text)
    locations.sort()
    return locations

def get_file(location):
    r = requests.get(url + location)
    return r.text

locations = get_locations()
print('\n'.join([f'{i} {location}' for i, location in enumerate(locations)]))
# i = int(input('enter a number: '))
i = int(45)

data_source_1 = get_file(locations[i])

# use regex to extract rainfall per date
rain_data = re.findall(r'(\d+-\w+-\d\d\d\d) *(\d+)', data_source_1)

def parse_date(date_str):
    date = datetime.datetime.strptime(date_str, '%d-%b-%Y')
    return (date.year, date.month, date.day)

d = {}
for i in range(len(rain_data)):
    date_1 = rain_data[i][0]
    d[parse_date(date_1)] = int(rain_data[i][1])
    # convert date to datetime
    date = datetime.datetime.strptime(date_1, '%d-%b-%Y')
    daily_total = int(rain_data[i][1])
    rain_data[i] = (date, daily_total)
    #date_rain1[i][1] = int(date_rain1[i][1])



# rows_2018 = [d[date] for date in d if date[0] == 2018]

# THE AVERAGE (OUTPUT)
# print(sum(rows_2018) / len(rows_2018))

print(d)


ten_day3 = [(date[2], d[date]) for date in d if date[0] == 2018 and date[1] == 1]

td_x = [t[0] for t in ten_day3]
td_y = [t[1] for t in ten_day3]

plt.plot(td_x, td_y)
plt.show()

# library & dataset
from matplotlib import pyplot as plt
import numpy as np

# create data
x = np.random.rand(15)
y = x + np.random.rand(15)
z = x + np.random.rand(15)
z = z * z

# Use it with a call in cmap
plt.scatter(x, y, s=z * 2000, c=x, cmap="BuPu", alpha=0.4, edgecolors="grey", linewidth=2)

# You can reverse it:
plt.scatter(x, y, s=z * 2000, c=x, cmap="BuPu_r", alpha=0.4, edgecolors="grey", linewidth=2)

# OTHER: viridis / inferno / plasma / magma
plt.scatter(x, y, s=z * 2000, c=x, cmap="plasma", alpha=0.4, edgecolors="grey", linewidth=2)

# plt.bar(td_x, td_y, 128)
# plt.show()
#
# plt.bar(td_x, td_y, 128)
# plt.show()


# print(ten_day3)

# matplotlib.pyplot.vlines(x, ymin, ymax, colors='k', linestyles='solid', label='', hold=None, data=None, **kwargs)

# print(date_rain1)

# user_input = parse_date('02-MAY-2018')

# print(date_rain1)


# date = datetime.datetime.strptime(date_rain1, '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016


# print(type(date_rain1)
