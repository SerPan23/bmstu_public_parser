import secret_keys
import vk
import data


def get_last_post(vk_api, domain):
    return vk_api.wall.get(domain=domain, count=1)['items']


def add_new_last_id(vk_api, domain):
    post = get_last_post(vk_api, domain)[0]
    data.update_last_posts(domain, post['id'])


def main():
    token = secret_keys.vk_token
    vk_api = vk.API(access_token=token, v='5.131')
    t = [

        'profkom_bmstu',
        'bas.bmstu',
        'iu_stream',
        'profkomiubmstu',
    ]
    for i in t:
        add_new_last_id(vk_api, i)


if __name__ == "__main__":
    main()