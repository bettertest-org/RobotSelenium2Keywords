# -*- coding: utf-8 -*-
from robot.libraries.BuiltIn import BuiltIn


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
            print s2l._info('it is not possible to '.format(sign))
            if no_error is False:
                raise AssertionError()
            return False

    def compare(self, a, b, sign='=='):
        return self._compare_base(a, b, sign, no_error=False)

    def compare_no_error(self, a, b, sign):
        return self._compare_base(a, b, sign, no_error=True)

    def get_inner_text(self, locator):
        """ Retrieves text value from an element found by locator
        """
        s2l = self.s2l
        s2l._info("getting text by locator '{0}'.".format(locator))
        element = s2l._element_find(locator, True, True)
        return element.text

    def expected_text(self, expected_text, locator):
        """Checks if element found by locator contains expected text.
        """
        text = self.get_inner_text(locator)
        return self.compare(text, expected_text)