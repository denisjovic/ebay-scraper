import requests
from bs4 import  BeautifulSoup
import smtplib


def check_price():
    url = 'https://www.ebay.com/itm/Garmin-Forerunner-620-GPS-Running-Watch-Blue-Black-with-charger/113920896303?hash=item1a8636ed2f%3Ag%3Az5oAAOSwsw9doMt7&LH_BIN=1'
    header = {'User-Agert': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    response = requests.get(url)
    data = response.content
    soup = BeautifulSoup(data, 'html.parser')
    
    # grab price value
    str_price = soup.find('span', {'itemprop': 'price'}).get_text()
    # convert to float for comparison
    price = float(str_price[4:])
    
    # compare price
    if price < 70:
        send_email()

def send_email():
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    print(conn.login('your_gmail', 'your_password'))
    conn.sendmail('your_gmail', 'target_email',
                  'Subject: Price is DOWN  \n\nDear XXX, the price is below $70, buy it!! Here is the link:\n'
                  'https://www.ebay.com/itm/Garmin-Forerunner-620-GPS-Running-Watch-Blue-Black-with-charger/113920896303?hash=item1a8636ed2f%3Ag%3Az5oAAOSwsw9doMt7&LH_BIN=1')
    print('Email sent!')
    conn.quit() 


check_price()
