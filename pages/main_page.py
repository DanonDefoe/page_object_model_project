from .base_page import BasePage


# Конструктор с ключевым словом super вызывает конструктор класса предка и передает ему аргументы,
# которые передали в конструктор MainPage
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
