from urllib import request

goog_url = 'https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv'

def download_stock_data(csv_url):
    # connect to the url
    response = request.urlopen(csv_url)
    csv = response.read()
    # all the data read from url will be converted to String
    csv_str = str(csv)
    # break the line
    lines = csv_str.split("\\n")
    # where to save the file
    dest_url = r'goog.csv'
    # open the file and write it
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)