import requests, time, random
# from fake_useragent import UserAgent


class CFDA():
    def __init__(self):
        # self.url =  "http://125.35.6.80:8181/ftban/itownet/fwAction.do?method=getBaNewInfoPage"
        self.url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.data = {'on': 'true',
                     'page': '1',
                     'pageSize': '15',
                     'productName': '',
                     'conditionType': '1',
                     'applyname': '',
                     'applysn': ''}

    def getData(self, data):
        try:
            response = requests.post(self.url, data=data, headers=self.headers, timeout=3)
            if response.status_code == 200:
                html = response.json()
                # print(html)
                return html
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        except requests.exceptions.ConnectTimeout as e:
            print(e)
            return None

    def extractData(self, html):
        name_list = []
        try:
            for i in range(len(html['list'])):
                cfda_data = html['list'][i]['EPS_NAME']
                # print(cfda_data)
                name_list.append(cfda_data)
            return name_list
        except:
            print('!!!')
            return None

    def writeData(self, cfda_data):#写文件
        with open('CFDA.txt', 'a') as f:
            f.write(cfda_data + '\n')

    def run(self):
        for page in range(1, int(d) + 1):
            print('第{}页：'.format(str(page)))
            time.sleep(random.uniform(1, 3))
            self.data['page'] = str(page)
            one_page = self.getData(self.data)
            for i in self.extractData(one_page):
                print(i)
                self.writeData(i)
        print('任务完成')



if __name__ == '__main__':
    d = input('请输入爬取深度：')
    cfda = CFDA()
    cfda.run()
