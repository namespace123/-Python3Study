# -*- coding:utf-8 -*-
from xml.parsers.expat import ParserCreate

weather_dict = {}  # 定义天气字典
which_day = 0  # 哪一天


# 定义解析类 这三个函数在廖雪峰老师xml这一节中介绍了
# 包括三个主要函数：start_element(),end_element(),char_data()
class WeatherSaxHandler(object):
    def start_element(self, name, attrs):  # 定义start_element函数
        global weather_dict, which_day

        if name == 'yweather:location':  # 判断并获取XML文档中地理位置信息
            weather_dict['city'] = attrs['city']  # 将本行XML代码中'city'属性值赋予字典weather_dict中的'city'
            weather_dict['country'] = attrs['country']  # 执行结束后此时，weather_dict={'city':'Beijing','country'='China'}

        if name == 'yweather:forecast':  # 同理获取天气预测信息
            which_day += 1  # 第一天天气，获取气温、天气
            if which_day == 1:
                weather_today = {'text': attrs['text'],
                           'low': int(attrs['low']),
                           'high': int(attrs['high'])
                           }
                weather_dict['today'] = weather_today  # 此时weather_dict出现二维字典
            # weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}}

            elif which_day == 2:    # 第二天相关信息
                weather_today = {
                    'text': attrs['text'],
                    'low': int(attrs['low']),
                    'high': int(attrs['high'])
                }
                weather_dict['tomorrow'] = weather_today
    # weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}, 'tomorrow': {'text': 'Sunny', 'low': 21, 'high': 34}}

    def end_element(self, name):    # end_element函数
        pass

    def char_data(self, text):   # char_data函数
        pass

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return weather_dict


# XML文档，输出结果的数据来源
# 将XML文档赋值给data

data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
# 实例化类
weather = parse_weather(data)
# 检查条件是否为True
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == 20, weather['today']['low']
assert weather['today']['high'] == 33, weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
# 打印到屏幕
print('Weather:', str(weather))

