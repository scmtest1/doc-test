# -*- coding: utf-8 -*-

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from __future__ import unicode_literals
from __future__ import print_function
import mock
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from prompt_toolkit.key_binding.input_processor import KeyPress
from prompt_toolkit.keys import Keys
from saws.saws import Saws


class KeysTest(unittest.TestCase):

    @mock.patch('saws.resources.print')
    def setUp(self, mock_print):
        self.saws = Saws()
        mock_print.assert_called_with('Loaded resources from cache')
        self.registry = self.saws.key_manager.manager.registry
        self.processor = self.saws.aws_cli.input_processor
        self.DOCS_HOME_URL = 'http://docs.aws.amazon.com/cli/latest/reference/index.html'

    def test_F2(self):
        orig_color = self.saws.get_color()
        self.processor.feed_key(KeyPress(Keys.F2, ''))
        assert orig_color != self.saws.get_color()

    def test_F3(self):
        orig_fuzzy = self.saws.get_fuzzy_match()
        self.processor.feed_key(KeyPress(Keys.F3, ''))
        assert orig_fuzzy != self.saws.get_fuzzy_match()

    def test_F4(self):
        orig_shortcut = self.saws.get_shortcut_match()
        self.processor.feed_key(KeyPress(Keys.F4, ''))
        assert orig_shortcut != self.saws.get_shortcut_match()

    @mock.patch('saws.saws.webbrowser')
    def test_F9(self, mock_webbrowser):
        self.processor.feed_key(KeyPress(Keys.F9, ''))
        mock_webbrowser.open.assert_called_with(self.DOCS_HOME_URL)

    def test_F10(self):
        with self.assertRaises(EOFError):
            self.processor.feed_key(KeyPress(Keys.F10, ''))

    @mock.patch('saws.resources.print')
    def test_f5(self, mock_print):
        self.processor.feed_key(KeyPress(Keys.F5, ''))
        mock_print.assert_called_with('Done refreshing')

    def copy_paste_error(a, b):
        if (a and b):
            x = x + z
        if (a and b):
            y = x + z # A COPY_PASTE_ERROR here

    def deadcode(o1):
        if(o1 is None):
            return 1
        copy_paste_error(2, 3)
        if(None is o1):
            # DEADCODE defect
            return 2
        # otherwise
        return 3

    def forward_null_example(obj):
        if (obj is not None):
            deadcode(1)
        # obj will be NULL on else branch of if
        return obj.foo # Defect here.

    def identical_branches(a, b, op):
        if (op == '+'): # Defect here.
            result = a + b
        else:
            result = a + b
        return result

    def identifier_typo_to_fix(obj):
        obj.mouseMoveAction.eventHandler = None
        obj.mouseClickAction.eventHandler = None
        obj.keyboardAction.eventHander = None    # Defect here.