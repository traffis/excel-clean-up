from selenium import webdriver

# open and use chrome as webdriver
driver = webdriver.Chrome()


def login(username, password):
    """Log into website and loads table"""
    driver.get("https://" + username + ":" + password
               + "") # this would be the website to login to
    driver.find_element_by_css_selector("#cmdGet").click()  # click get button


def get_table():
    """Gets table of webpage"""
    table = driver.find_elements_by_xpath("//*[@id=\"dgListView_DIV\"]/table/tbody/tr")
    return table


def get_records():
    """Gets range of records"""
    records = driver.find_element_by_xpath(
        "//*[@id=\"primaryDiv\"]/table[4]/tbody/tr[1]/td/table/tbody/tr/td[1]").text.split()
    return records


def get_tickets():
    """Gets the ticket information from table"""
    ticket_pairs = {}

    while True:
        table = get_table()

        for i in range(len(table)):
            # gets work order number and ticket description
            work_order = driver.find_element_by_id("dgListView_" + str(i) + "_1").text
            ticket_description = driver.find_element_by_id("dgListView_" + str(i) + "_2").text.split()

            # determine if ticket is request or incident and get ticket number if available
            if "Request" in ticket_description:
                ticket_type = ticket_description.index("Request")
                ticket_number = ticket_description[ticket_type + 1]

            elif "Incident" in ticket_description:
                ticket_type = ticket_description.index("Incident")
                ticket_number = ticket_description[ticket_type + 1]

            else:
                ticket_number = "N/A"

            ticket_pairs[work_order] = ticket_number

        # check if last page
        records = get_records()
        if records[3] == records[5]:
            break

        # click next page button
        driver.find_element_by_css_selector("#cmdNext").click()

    driver.quit()
    return ticket_pairs
