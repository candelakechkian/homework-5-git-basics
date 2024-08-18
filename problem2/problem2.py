def date_format(date):
    year = date[6:]
    month = date[:2]
    day = date[3:5]
    formatted_date = year + '-' + month + '-' + day
    return formatted_date