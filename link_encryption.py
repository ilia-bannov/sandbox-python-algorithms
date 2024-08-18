import hashlib
import random


class MarsURLEncoder:

    def __init__(self):
        self.links = dict()

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        # short_url = '/'.join(long_url.split('/')[:3])
        str_to_encode = '/'.join(long_url.split('/')[3:])
        hash_code = hashlib.md5(str_to_encode.encode()).hexdigest()
        while hash_code in self.links:
            # print(self.links)
            # if hash_code in self.links:
            hash_code = hash_code + str(random.randint(0, 1000))
            # print(hash_code)
        key = 'https://ma.rs/' + hash_code
        self.links[key] = long_url
        return key

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.links[short_url]


url = MarsURLEncoder()
print(url.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'))
print(url.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'))
print(url.links)
print(url.decode('https://tsup.ru/7da7ce03b96a92df1b6624a3c7e2f64a'))
