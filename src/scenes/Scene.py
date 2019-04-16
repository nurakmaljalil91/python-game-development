import random
import string


def generate_id():
    random_number = random.randint(100, 999)
    random_string = ''.join(
        [random.choice(string.ascii_letters) for n in range(3)])
    random_id = random_string + str(random_number)
    return random_id


class Scene(object):
    def __init__(self, name):
        self.name = name
        self.tag = 'null'
        # generate id
        self.id = generate_id()

    def start(self):
        pass

    def set_tag(self, tag):
        self.tag = tag
