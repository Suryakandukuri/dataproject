from bs4 import BeautifulSoup
import pandas as pd
import requests


# initiating a final dataframe to hold all the data
mobile_data_list = []

#url from which you get
# total number of product pages is 488, as shown on flipkart but, we do not get any data after 41. hence the change in number
for i in range(1,43):
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page="+str(i)
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    mobile_names = soup.find_all("div", class_="_4rR01T")
    ratings = soup.find_all("div", class_="_3LWZlK")
    prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")

    # creating empty lists for capturing data
    list_mobile_names = []
    list_ratings = []
    list_prices = []
    
    # iterating through the params to get the text value.
    for mobile in mobile_names:
        name = mobile.get_text()
        list_mobile_names.append(name)

    for rating in ratings[:len(mobile_names)]:
        rat = rating.get_text()
        list_ratings.append(rat)

    for price in prices:
        price_value = price.get_text()
        list_prices.append(price_value)

    print("len of mobile names ", len(list_mobile_names))
    print("len of ratings ", len(list_ratings))
    print("len of prices ", len(list_prices))
    # creation of dataframe
    page_data = pd.DataFrame(
        {'mobile_name': list_mobile_names,
        'rating': list_ratings,
        'price': list_prices
        })
    
    mobile_data_list.append(page_data)

    print("completed scraping data from page", i)
    

final_data = pd.concat(mobile_data_list)
final_data = final_data.reset_index(drop=True, inplace = False)

final_data.to_csv("flipkart_mobile_data.csv", index = False)