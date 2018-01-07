# -*- coding: utf-8 -*-
"""
LRC's time format parser: MM:SS.mm
"""
import re
from datetime import time

from pylrc.lrcexc import InvalidTimeString
from pylrc.comparablemixin import ComparableMixin
from pylrc.compat import str, basestring

class TimeItemDescriptor(object):
    # pylint: disable-msg=R0903
    def __init__(self, ratio, super_ratio=0):
        self.ratio = int(ratio)
        self.super_ratio = int(super_ratio)

    def _get_ordinal(self, instance):
        if self.super_ratio:
            return instance.ordinal % self.super_ratio
        return instance.ordinal

    def __get__(self, instance, klass):
        if instance is None:
            raise AttributeError
        return self._get_ordinal(instance) // self.ratio

    def __set__(self, instance, value):
        part = self._get_ordinal(instance) - instance.ordinal % self.ratio
        instance.ordinal += value * self.ratio - part


class LRCTime(ComparableMixin):
    TIME_PATTERN = '%02d:%02d.%02d'
    TIME_REPR = 'LRCTime(%d, %d, %d)'
    RE_TIME_SEP = re.compile(r'\:|\.|\,')
    RE_INTEGER = re.compile(r'^(\d+)')
    SECONDS_RATIO = 1000
    MINUTES_RATIO = SECONDS_RATIO * 60

    minutes = TimeItemDescriptor(MINUTES_RATIO)
    seconds = TimeItemDescriptor(SECONDS_RATIO, MINUTES_RATIO)
    milliseconds = TimeItemDescriptor(1, SECONDS_RATIO)

    def __init__(self, minutes=0, seconds=0, milliseconds=0):
        """
        LRCTime(minutes, seconds, milliseconds)

        All arguments are optional and have a default value of 0.
        """
        super(LRCTime, self).__init__()
        self.ordinal = minutes * self.MINUTES_RATIO \
                     + seconds * self.SECONDS_RATIO \
                     + milliseconds

    def __repr__(self):
        return self.TIME_REPR % tuple(self)

    def __str__(self):
        if self.ordinal < 0:
            # Represent negative times as zero
            return str(LRCTime.from_ordinal(0))
        return self.TIME_PATTERN % tuple(self)

    def _compare(self, other, method):
        return super(LRCTime, self)._compare(self.coerce(other), method)

    def _cmpkey(self):
        return self.ordinal

    def __add__(self, other):
        return self.from_ordinal(self.ordinal + self.coerce(other).ordinal)

    def __iadd__(self, other):
        self.ordinal += self.coerce(other).ordinal
        return self

    def __sub__(self, other):
        return self.from_ordinal(self.ordinal - self.coerce(other).ordinal)

    def __isub__(self, other):
        self.ordinal -= self.coerce(other).ordinal
        return self

    def __mul__(self, ratio):
        return self.from_ordinal(int(round(self.ordinal * ratio)))

    def __imul__(self, ratio):
        self.ordinal = int(round(self.ordinal * ratio))
        return self

    @classmethod
    def coerce(cls, other):
        """
        Coerce many types to LRCTime instance.
        Supported types:
          - str/unicode
          - int/long
          - datetime.time
          - any iterable
          - dict
        """
        if isinstance(other, LRCTime):
            return other
        if isinstance(other, basestring):
            return cls.from_string(other)
        if isinstance(other, int):
            return cls.from_ordinal(other)
        if isinstance(other, time):
            return cls.from_time(other)
        try:
            return cls(**other)
        except TypeError:
            return cls(*other)

    def __iter__(self):
        yield self.minutes
        yield self.seconds
        yield self.milliseconds

    def shift(self, *args, **kwargs):
        """
        shift(minutes, seconds, milliseconds)

        All arguments are optional and have a default value of 0.
        """
        if 'ratio' in kwargs:
            self *= kwargs.pop('ratio')
        self += self.__class__(*args, **kwargs)

    @classmethod
    def from_ordinal(cls, ordinal):
        """
        int -> LRCTime corresponding to a total count of milliseconds
        """
        return cls(milliseconds=int(ordinal))

    @classmethod
    def from_string(cls, source):
        """
        str/unicode(MM:SS.mm) -> LRCTime corresponding to serial
        raise InvalidTimeString
        """
        items = cls.RE_TIME_SEP.split(source)
        if len(items) != 3:
            raise InvalidTimeString
        return cls(*(cls.parse_int(i) for i in items))

    @classmethod
    def parse_int(cls, digits):
        try:
            return int(digits)
        except ValueError:
            match = cls.RE_INTEGER.match(digits)
            if match:
                return int(match.group())
            return 0

    @classmethod
    def from_time(cls, source):
        """
        datetime.time -> LRCTime corresponding to time object
        """
        return cls(minutes=source.minute,
            seconds=source.second, milliseconds=source.microsecond // 1000)

    def to_time(self):
        """
        Convert LRCTime instance into a pure datetime.time object
        """
        return time(0, self.minutes, self.seconds,
                    self.milliseconds * 1000)
