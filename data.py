import json

publics = [
    'bmstu1830',
    'library.bmstu',
    'studsovet_bmstu',
    'profkom_bmstu',
    'bas.bmstu',
    'iu_stream',
    'profkomiubmstu',
]

publics_names = {
    'bmstu1830': 'МГТУ им. Н.Э. Баумана',
    'library.bmstu': 'Библиотека МГТУ им. Н.Э. Баумана',
    'studsovet_bmstu': 'Студенческий совет МГТУ им. Н.Э. Баумана',
    'profkom_bmstu': 'Профсоюз студентов МГТУ им. Н.Э. Баумана',
    'bas.bmstu': 'Bauman Active Sports | BAS',
    'iu_stream': 'Факультет ИУ МГТУ им. Н. Э. Баумана',
    'profkomiubmstu': 'рофсоюз ИУ',
}


def get_last_posts():
    with open("last_posts.json", "r") as read_file:
        data = json.load(read_file)
        return data


def update_last_posts(domain, id):
    last_posts = get_last_posts()
    last_posts[domain] = id
    with open("last_posts.json", "w") as write_file:
        json.dump(last_posts, write_file)
