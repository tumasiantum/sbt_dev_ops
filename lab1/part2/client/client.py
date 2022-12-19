#!/usr/bin/env python3

import urllib.request

# Подключаемся к 'http://localhost:1234/'.
fp = urllib.request.urlopen("http://localhost:1234/")

# Читаем и декодируем
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# Выводим
print(decodedContent)

# Закрываем подключение
fp.close()
