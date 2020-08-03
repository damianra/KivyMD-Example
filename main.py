from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import requests

from kivymd.toast import toast



class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Home = Home()
        Builder.load_file('main.kv')
        wid = Screen(name='home')
        wid.add_widget(self.Home)
        self.add_widget(wid)


class Home(BoxLayout):
    def __init__(self, **kwargs):
        super(Home, self).__init__()
        self.price = .0
        self.btc_price()


    def btc_price(self):
        r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false')
        data = []
        if r.status_code == 200:
            json = r.json()
            for j in json:
                data.append(j)
        self.ids.pricelbl.text = '1 BTC = ' + str(data[0]['current_price']) + ' USD'
        self.price = data[0]['current_price']
        print(self.price)

    def btc_convert(self):
        cant = float(self.ids.btctext.text)
        total = cant * self.price
        toast(str(total))

class MainApp(MDApp):
    title = 'BTC Convert'

    def build(self):

        return MainWid()


if __name__ == '__main__':
    app = MainApp()
    app.run()