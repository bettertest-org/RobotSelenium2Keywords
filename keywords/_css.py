# -*- coding: utf-8 -*-
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.color import Color


class _CssKeywords():

    @property
    def s2l(self):
        return BuiltIn().get_library_instance('Selenium2Library')

    def value_of_css_property(self, property_name, locator):
        """Returns value of property found by locator
        """
        s2l = self.s2l
        browser = s2l._current_browser()
        element = s2l._element_find(locator, True, True)
        prop_value = element.value_of_css_property(property_name)
        s2l._info('value of css property {0} : {1}'.format(property_name, prop_value))
        return prop_value

    def _color_checker(self, color_value, locator, property):
        color_value = color_value.lower().replace('hex', '', 3)
        if Color.from_string(color_value).rgba != self.value_of_css_property(property, locator):
            raise AssertionError()

    def check_color(self, color_value, locator, property='color'):
        """Checks if element found by locator has correct value
        """
        self._color_checker(color_value, locator, property)

    def check_background_color(self, color_value, locator):
        """Checks if element's background color has correct value
        """
        self.check_color(color_value, locator, 'background-color')