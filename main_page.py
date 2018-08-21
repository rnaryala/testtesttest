class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self._search_form = None

    @property
    def search_form(self):
        from search_form import SearchForm
        if self._search_form is None:
            self._search_form = SearchForm(self.driver)
        return self._search_form

    def open(self, url):
        self.driver.get(url)
