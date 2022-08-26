import time

import schedule
import secret_keys
import vk
import telebot
import data


def find_by_key(iterable, key, value):
    for index, dict_ in enumerate(iterable):
        # print(index, dict_)
        if key in dict_ and dict_[key] == value:
            return (index, dict_)


def get_new_posts(vk_api, domain, count=10):
    posts = vk_api.wall.get(domain=domain, count=count)['items'][::-1]
    new_posts = select_new_posts(posts, data.get_last_posts()[domain])
    if len(new_posts) > 0:
        data.update_last_posts(domain, new_posts[-1]['id'])
    return new_posts


def select_new_posts(posts, last_post):
    index, obj = find_by_key(posts, 'id', last_post)
    new_posts = posts[index+1:]
    return new_posts


def send_telegram(public_name, body, domain, from_id, id):
    url = 'https://vk.com/' + str(domain) + '?w=wall' + str(from_id) + '_' + str(id)
    bot = telebot.TeleBot(secret_keys.tg_bot_token)
    # text = '<b>' + public_name + '</b>\n' + body.split('\n \n')[0] + '\n' + url
    text = '<b>Новый пост в ' + public_name + '</b>\n' + url
    bot.send_message(chat_id=secret_keys.channel_id, text=text, parse_mode='html')


def check_new_posts(vk_api):
    for d in data.publics:
        domain = d
        posts = get_new_posts(vk_api, domain)
        for p in posts:
            send_telegram(data.publics_names[domain], p['text'], domain, p['from_id'], p['id'])
        if len(posts) > 0:
            print('added new ' + str(len(posts)) + ' posts from ' + domain)
        time.sleep(5)


def main():
    token = secret_keys.vk_token
    vk_api = vk.API(access_token=token, v='5.131')
    # check_new_posts(vk_api)
    schedule.every(10).minutes.do(check_new_posts(vk_api))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
