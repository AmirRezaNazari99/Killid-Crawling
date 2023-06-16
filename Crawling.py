import time

def parse_page(page, driver):
    property_details = []

    url = 'https://kilid.com/buy/tehran-region5?listingTypeId=1&location=246745&sort=DATE_DESC&page={}'.format(page)

    driver.get(url)

    time.sleep(5)

    price_elements = driver.find_elements('xpath', '//span[@class="ng-star-inserted"]')

    prices = []
    for i in range(1, len(price_elements), 3):
        prices.append(price_elements[i].text.split(" ")[0])

    location_elements = driver.find_elements('xpath', '//div[@class="address"]')
    locations = [detail.text for detail in location_elements]

    detail_elements = driver.find_elements('xpath', '//div[@class="feature"]')
    details = [detail.text.split("\n") for detail in detail_elements]

    counter = 0
    for detail in details:
        # features = detail.split("\n")
        property_detail = {
            "price": None,
            "location": None,
            "type": None,
            "size": None,
            "bedrooms": None,
            "parking": None,
        }
        property_detail["price"] = prices[counter]
        property_detail["location"] = locations[counter]
        property_detail["type"] = detail[0]
        property_detail["size"] = detail[1].split(" ")[0]
        counter += 1

        for i in detail:
            if "خوابه" in i:
                property_detail["bedrooms"] = i.split(" ")[0]

            elif "پارکینگ" in i:
                property_detail["parking"] = i.split(" ")[0]



        property_details.append(property_detail)



    return (property_details)
