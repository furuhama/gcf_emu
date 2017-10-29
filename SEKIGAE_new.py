# -*- coding: utf-8 -*-

import json
import os
import random
import datetime
# import requests
import yaml
import holiday
import codecs

def get_today_datetime(difference):
    # herokuサーバーとの時差を修正する
    # 日本の場合は引数に 9 を入れる
    return datetime.datetime.now() + datetime.timedelta(hours = difference)

def get_weekday_as_number(date):
    # (YYYY, MM, DD)の int 形式の入力を曜日に変換
    # 年、月、日を入力することで曜日を番号で取得する
    # 月曜日=0, 火曜日=1, ... 日曜日=6
    return datetime.date(date.year, date.month, date.day).weekday()

def set_namelist(filename):
    # 読み込みたいyamlファイルの名前を引数に string で受け取り、listで出力する
    f = open(filename, 'r')
    name_lists = yaml.load(f)
    f.close()
    return name_lists

def set_todays_desk_number(desk_quantity):
    # デスクの数を受け取って、ランダムな順番に並び替えた list を返す
    default_list = list(range(1, desk_quantity + 1))
    return random.sample(default_list, desk_quantity)

def combine_name_and_desk(namelist, desk_number):
    # 2つの list を受け取って list をネストした構造にする

    # namelist の要素数が desk_number 以下の場合は availableを追加する
    if len(namelist) < len(desk_number):
        for i in range(len(desk_number) - len(namelist)):
            namelist.append('available')

    # namelist の要素数が desk_number を超えていないかチェックする
    if len(namelist) > len(desk_number):
        return "error! namelistの要素数がdesk_numberを超えています!\n(現在... namelist:{}, desk_number:{})".format(len(namelist), len(desk_number))

    nesting_list = []
    for i in range(len(namelist)):
        nesting_list.append([namelist[i], desk_number[i]])
    return nesting_list

def replace_desk_number(name_desk_list, name, place):
    # セットされた名前のリスト、リモートの人の名前と仕事場所の string を受け取って、置き換える

    # 名前だけのリストを作成
    set_namelist = []
    for i in range(len(name_desk_list)):
        set_namelist.append(name_desk_list[i][0])

    # name の人が namelist の何番目にあるか
    NAME_NUM = set_namelist.index(name)
    STORE_NUMBER = name_desk_list[NAME_NUM][1]

    # 置き換えする
    name_desk_list[NAME_NUM][1] = place

    # 最後に空いた席を available として追加
    name_desk_list.append(['available', STORE_NUMBER])

    return name_desk_list

def list_to_str(set_list):
    # listを受け取ってtext用の改行を含むstrに変換する
    str_text = ''
    for i in set_list:
        str_text += str(i[0]) + ': ' + str(i[1]) + '\n'

    return str_text

def what_day_is_it_today(daytime_arg, weeknumber):
    # 年月日と曜日に関するテキストを生成する
    WEEKNAME = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return "今日は{}年{}月{}日{}です。".format(daytime_arg.year, daytime_arg.month, daytime_arg.day, WEEKNAME[weeknumber])

def set_holiday_dict(filename, year):
    # 入力されたファイルに、入力された年の祝日リストを書き込む
    holiday_lists = []
    for i in holiday.CountryHolidays.get('JP', year):
        holiday_lists.append([str(i[0]), i[1]])

    # 辞書型に変換
    holiday_dict = dict(holiday_lists)

    # 書き込み
    with codecs.open(filename, 'w', 'utf-8') as f:
        yaml.dump(holiday_dict, f, encoding='utf-8', allow_unicode=True, default_flow_style=False)

    f.close

def load_holiday_dict(filename):
    # 同じディレクトリにある休日の辞書を読み込む
    f = open(filename, 'r')
    holiday_dict = yaml.load(f)
    f.close()
    return holiday_dict

def datetime_to_str(datetime_arg):
    # get_today_datetime で取得した値を str に変換して dict の key の検索ができる形に(最後に' 00:00:00'を足しているのもそのため)
    date_str_text = datetime_arg.strftime('%Y-%m-%d') + ' 00:00:00'
    return date_str_text

def set_todays_icon():
    # ランダムでマリオのアイコンを返す
    # mario, mario1, mario2, ... mario41
    icon_num_list = list(range(0,42))
    r = random.sample(icon_num_list, 1)
    if r[0] == 0:
        emoji = ":mario:"
    else:
        emoji = ":mario%s:" % str(r[0])

    return emoji

def send_bot_message_with_image(icon_emoji, bot_text, image_url, target_url):
    # 送る際のemoji、送りたいテキスト、添付する画像URL、対象のURL を str で受け取って送信する
    payload_dic = {
        'icon_emoji': icon_emoji,
        'text': bot_text,
        'attachments': [
            {
                'color': '#36a64f',
                'image_url': image_url
            }
        ]
    }
    requests.post(target_url, data=json.dumps(payload_dic))

def send_bot_message_without_image(icon_emoji, bot_text, target_url):
    # 送る際のemoji、送りたいテキスト、対象のURL を str で受け取って送信する
    payload_dic = {
        'icon_emoji': icon_emoji,
        'text': bot_text
    }
    requests.post(target_url, data=json.dumps(payload_dic))

### 以下は細かい定数を定義

WEEKDAY_COMMENT = "インターンは空いているところに座ろう"
HOLIDAY_COMMENT = "本日はお休みです"

if __name__ == '__main__':
    ####################################
    # 今日の日付を取得
    ####################################
    time_now = get_today_datetime(9)

    ####################################
    # 休日リストの書き換え (年が変わった時に読み込み直す)
    ####################################
    if time_now.month == 1 and time_now.date == 1:
        set_holiday_dict('holiday_lists.yaml', time_now.year)

    ####################################
    # テキスト生成部分
    ####################################
    str_time_now = datetime_to_str(datetime.date(time_now.year, time_now.month, time_now.day))
    weeknum = get_weekday_as_number(time_now)

    # 今日が祝日かどうか判定(祝日なら以降の判定は全て飛ばす)
    if str_time_now in load_holiday_dict('holiday_lists.yaml'):
        todays_text = what_day_is_it_today(time_now, weeknum) + '({})'.format(load_holiday_dict('holiday_lists.yaml')[str_time_now]) + '\n\n' + HOLIDAY_COMMENT

    # 月曜日
    elif weeknum == 0:
        name_desk_list = combine_name_and_desk(set_namelist('name_list_1.yaml'), set_todays_desk_number(15))
        todays_text = list_to_str(name_desk_list) + '\n' + what_day_is_it_today(time_now, weeknum) + '\n\n' + WEEKDAY_COMMENT
    # 火曜日、水曜日
    elif weeknum == 1 or weeknum == 2:
        name_desk_list = combine_name_and_desk(set_namelist('name_list_1.yaml'), set_todays_desk_number(15))
        # is8r さんが自宅勤務
        name_desk_list = replace_desk_number(name_desk_list, 'is8r', ':house_with_garden:')
        todays_text = list_to_str(name_desk_list) + '\n' + what_day_is_it_today(time_now, weeknum) + '\n\n' + WEEKDAY_COMMENT

    # 木曜日
    elif weeknum == 3:
        name_desk_list = combine_name_and_desk(set_namelist('name_list_2.yaml'), set_todays_desk_number(15))
        todays_text = list_to_str(name_desk_list) + '\n' + what_day_is_it_today(time_now, weeknum) + '\n\n' + WEEKDAY_COMMENT

    # 金曜日
    elif weeknum == 4:
        name_desk_list = combine_name_and_desk(set_namelist('name_list_2.yaml'), set_todays_desk_number(15))
        # shinofara さん、 eruma さんが田町勤務
        name_desk_list = replace_desk_number(name_desk_list, 'shinofara', ':tamachi:')
        name_desk_list = replace_desk_number(name_desk_list, 'eruma', ':tamachi:')
        todays_text = list_to_str(name_desk_list) + '\n' + what_day_is_it_today(time_now, weeknum) + '\n\n' + WEEKDAY_COMMENT

    # 土曜日、日曜日
    elif weeknum == 5 or weeknum == 6:
        todays_text = what_day_is_it_today(time_now, weeknum) + '\n\n' + HOLIDAY_COMMENT

    else:
        print('error')


    ####################################
    # slack への送信部分
    ####################################
    # 環境変数のロード
    # SLACK_URL = os.getenv("SLACK_URL")
    # OFFICE_IMAGE_URL = os.getenv("OFFICE_IMAGE_URL")

    # 送信
    # 休日は画像なしで送る
    if str_time_now in load_holiday_dict('holiday_lists.yaml') or weeknum == 5 or weeknum == 6:
        # send_bot_message_without_image(set_todays_icon(), todays_text, SLACK_URL)
        print(todays_text)

    # それ以外は画像ありで送る
    else :
        # send_bot_message_with_image(set_todays_icon(), todays_text, OFFICE_IMAGE_URL, SLACK_URL)
        print(todays_text)

