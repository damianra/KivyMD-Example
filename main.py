from functools import partial

from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.network.urlrequest import UrlRequest

from kivymd.toast import toast



class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Home = Home()
        wid = Screen(name='home')
        wid.add_widget(self.Home)
        self.add_widget(wid)


class Home(BoxLayout):
    def __init__(self, **kwargs):
        super(Home, self).__init__()
        self.price = .0
        # self.btc_price()
        self.url_requests()

    def url_requests(self, *args):
        req = UrlRequest('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false', self.got_json)

    def got_json(self, req, result):
        for key,value in result[0].items():
            if key == 'current_price':
                self.ids.pricelbl.text = '1 BTC = ' + str(value) + ' USD'
                self.price = value


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