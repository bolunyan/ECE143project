def getTexts(driver, URL):
    driver.get(URL)
    time.sleep(5)
    elements = driver.find_elements_by_class_name('mw-collapsible-text')
    for element in elements:
        element.click()
    page = driver.page_source
    soup = Soup(page)
    desiredText = soup.findAll('table')
    captions = []
    for num, table in enumerate(desiredText):
        try:
            captions.append(table.find('caption').contents[0])
        except:
            captions.append('No Caption: %d' %num)
    return (captions, desiredText)