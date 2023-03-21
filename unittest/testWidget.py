#!/usr/bin/python3
import unittest
from Widget import Widget

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget("The widget")
        self.assertEqual(widget.size(), (50, 50))

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), "incorrect default size")

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), "wrong size after resize")

    def tearDown(self):
        self.widget.dispose()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(SimpleWidgetTestCase())
    suite.addTest(DefaultWidgetSizeTestCase())
    return suite
