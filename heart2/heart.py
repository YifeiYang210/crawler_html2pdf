# -*- coding:utf-8 -*-
import codecs
import re

import jieba.analyse
import matplotlib.pyplot as plt
import requests
from scipy.misc import imread
from wordcloud import WordCloud

__author__ = 'liuzhijun'

headers = {
    "Host": "m.weibo.cn",
    "Referer": "https://weibo.com/u/5282704047",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) "
                  "Version/9.0 Mobile/13B143 Safari/601.1",
}


def clean_html(raw_html):
    pattern = re.compile(r'<.*?>|转发微博|//:|Repost|，|？|。|、|分享图片|回复@.*?:|//@.*')
    text = re.sub(pattern, '', raw_html)
    return text


url = "https://m.weibo.cn/api/container/getIndex"
params = {"uid": "{uid}",
          "luicode": "10000011",
          "featurecode": "20000320",
          "type": "uid",
          "value": "5282704047",
          "containerid": "{containerid}",
          "page": "{page}"}


def fetch_data(uid=None, container_id=None):
    """
    抓取数据，并保存到CSV文件中
    :return:
    """
    page = 0
    total = 1218  #tongtong_total
    blogs = []
    for i in range(0, total // 10):
        params['uid'] = uid
        params['page'] = str(page)
        params['containerid'] = container_id
        res = requests.get(url, params=params, headers=headers)
        cards = res.json().get("data").get("cards")

        for card in cards:
            # 每条微博的正文内容
            if card.get("card_type") == 9:
                text = card.get("mblog").get("text")
                text = clean_html(text)
                blogs.append(text)
        page += 1
        print("抓取第{page}页，目前总共抓取了 {count} 条微博".format(page=page, count=len(blogs)))
        with codecs.open('weibo2.txt', 'w', encoding='utf-8') as f:
            f.write("\n".join(blogs))


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    s = "hsl(255, 0%%, %d%%)" % 0
    print(s)
    return s


def generate_image():
    data = []
    jieba.analyse.set_stop_words("./stopwords.txt")

    with codecs.open("weibo2.txt", 'r', encoding="utf-8") as f:
        for text in f.readlines():
            data.extend(jieba.analyse.extract_tags(text, topK=20))
        data = " ".join(data)
        mask_img = imread('./tongtong4.jpg', flatten=True)
        wordcloud = WordCloud(
            font_path='msyh.ttc',
            background_color='white',
            mask=mask_img
        ).generate(data)
        plt.title(u"tongtong_weibo")
        plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3),
                   interpolation="bilinear")
        # mask_img = imread('./logo.jpg', flatten=True)
        #
        # wordcloud = WordCloud(font_path='/Library/Fonts/Songti.ttc',
        #                       background_color="white",
        #                       max_words=80,
        #                       mask=mask_img
        #                       ).generate(data)
        # plt.figure(figsize=(9, 6))
        # plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")

        plt.imshow(wordcloud, interpolation="bilinear")
        # plt.axis("off")
        # plt.show()



        # wordcloud = WordCloud(
        #     font_path='/Library/Fonts/Songti.ttc',
        #     background_color='white',
        #     mask=mask_img
        # ).generate(data)
        # plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3),
        #            interpolation="bilinear")
        plt.axis('off')
        plt.savefig('./heart4.jpg', dpi=1600)


if __name__ == '__main__':
    # fetch_data("5282704047", "1076035282704047")  # tongtong_uid, tongtong_containerid
    generate_image()
