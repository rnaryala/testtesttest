from base_component import BaseComponent


class SearchForm(BaseComponent):
    selectors = {
        'button_search': '//input[@name="btnK"]'
    }

    # взять имя кнопки
    def get_button_name(self):
        return self.driver.find_element_by_xpath(self.selectors['button_search']).get_attribute('value')
