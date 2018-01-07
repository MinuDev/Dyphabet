# -*- coding: utf-8 -*-
"""
LRC's lyrics parser
"""

from pylrc.lrcexc import InvalidItem, InvalidIndex
from pylrc.lrctime import LRCTime
from pylrc.comparablemixin import ComparableMixin
from pylrc.compat import str, is_py2
import re

class LRCItem(ComparableMixin):
    """
    LRCItem(index, timestamp, text)

    index -> int: index of item in file. 0 by default.
    timestamp -> LRCTime or coercible.
    text -> unicode: text content for item.
    """
    ITEM_PATTERN = str('[%s]%s\n')

    def __init__(self, index=0, timestamp=None, text=''):
        try:
            self.index = int(index)
        except (TypeError, ValueError):  # try to cast as int, but it's not mandatory
            self.index = index

        self.timestamp = LRCTime.coerce(timestamp or 0)
        self.text = str(text)

    @property
    def text_without_tags(self):
        RE_TAG = re.compile(r'<[^>]*?>')
        return RE_TAG.sub('', self.text)

    @property
    def characters_per_second(self):
        characters_count = len(self.text_without_tags.replace('\n', ''))
        try:
            return characters_count / (self.duration.ordinal / 1000.0)
        except ZeroDivisionError:
            return 0.0

    def __str__(self):
        position = ' %s' % self.position if self.position.strip() else ''
        return self.ITEM_PATTERN % (self.timestamp, self.text)
    if is_py2:
        __unicode__ = __str__

        def __str__(self):
            raise NotImplementedError('Use unicode() instead!')

    def _cmpkey(self):
        return(self.timestamp)

    def shift(self, *args, **kwargs):
        """
        shift(minutes, seconds, milliseconds, ratio)

        Add given values to the timestamp attribute.
        All arguments are optional and have a default value of 0.
        """
        self.timestamp.shift(*args, **kwargs)

    @classmethod
    def from_string(cls, source):
        return cls.from_lines(source.splitlines(True))

    @classmethod
    def from_line(cls, line, index):
        line = line.rstrip()
        match = re.match("\\[(.+)\\](.*)", line)
        timestamp, text = match.group(1), match.group(2)
        return cls(index, timestamp, text)
