# -*- coding: utf-8 -*-
from robot.libraries.BuiltIn import BuiltIn
import datetime


class _TextKeywords():

    @property
    def s2l(self):
        return BuiltIn().get_library_instance('Selenium2Library')

    def _compare_base(self, a, b, sign='==', no_error=False):
        """Checks relations between a and b.
        By default checks if elements are equal and throws exception when they are not.
        Can return value (True/False) if no_error=True.
        """
        s2l = self.s2l
        if sign == ">":
            if a > b:
                return True
            else:
                s2l._info('{0} is not greater than {b}'.format(a,b))
                if no_error is False:
                    raise AssertionError()
                return False
        elif sign == ">=":
            if a >= b:
                return True
            else:
                s2l._info('{0} is not equal or greater than {b}'.format(a, b))
                if no_error is False:
                    raise AssertionError()
                return False
        elif sign == "==":
            if a == b:
                return True
            else:
                s2l._info('{0} is not equal to {b}'.format(a, b))
                if no_error is False:
                    raise AssertionError()
                return False
        elif sign == "<":
            if a < b:
                return True
            else:
                s2l._info('{0} is not less than {b}'.format(a, b))
                if no_error is False:
                    raise AssertionError()
                return False
        elif sign == "<=":
            if a <= b:
                return True
            else:
                s2l._info('{0} is not equal or less than {b}'.format(a, b))
                if no_error is False:
                    raise AssertionError()
                return False

        elif sign == "!=":
            if a != b:
                return True
            else:
                s2l._info('{0} is not equal or greater than {b}'.format(a, b))
                if no_error is False:
                    raise AssertionError()
                return False
        else:
            s2l._info('it is not possible to '.format(sign))
            if no_error is False:
                raise AssertionError()
            return False

    def compare(self, a, b, sign='=='):
        return self._compare_base(a, b, sign, no_error=False)

    def compare_no_error(self, a, b, sign):
        return self._compare_base(a, b, sign, no_error=True)

    def get_inner_text(self, locator):
        s2l = self.s2l
        element = s2l._element_find(locator, True, True)
        return element.text

    def expected_text(self, expected_text, locator):
        """Checks if element found by locator contains expected text.
        """
        text = self.get_inner_text(locator)
        return self.compare(text, expected_text)

    def is_sorted(self, elements_list, asc=True, time_format=''):
        """ Checks if list of elements (strings, numbers) is sorted ascending. Set asc=False to check if a list is sorted in descending oder.
        It is possible to check if dates are sorted, but time_format parameter should be provided.
        example time_format: "%Y-%m-%d", "%d.%m.%Y"
        """
        s2l = self.s2l
        if time_format is not '':
            #example time_format: "%Y-%m-%d", "%d.%m.%Y"
            elements_list = [datetime.datetime.strptime(ts, time_format) for ts in elements_list]

        sorted_list = sorted(elements_list)

        if asc is False:
            sorted_list.reverse()

        for index, item in enumerate(sorted_list):
            print index, item
            if elements_list[index] != item:
                s2l._info('list is not sorted')
                raise AssertionError()
