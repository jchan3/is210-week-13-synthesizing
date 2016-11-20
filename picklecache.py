#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Synthesizing Task 01 module"""


import os
import pickle


class PickleCache(object):
    """A PickleCache class definition."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for the PickleCache() class.

        Args:
            file_path (string, optional): A file path. Default: datastore.pkl
            autosync (bool, optional): A boolean for file sync. Default: False

        Attributes:
            __file_path (string): A pseudo-private attribute assigned to the
            constructor variable file_path.
            __data (dictionary): A pseudo-private attribute instantiated as an
            empty dictionary object.
            autosync (boolean): A non-private attribute
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """The function will save the key value pair in the __data dictionary.

        Args:
            key (string): A key value for the data dictionary.
            value (string): A value to be saved in the data dictionary.
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """A Magic Method for the PickleCache() class to return the length of
            self.__data.

        Args:
            None.

        Returns:
            integer: Returns the length of self.__data.

        Examples:
            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """A Magic Method that retrieves data from the PickleCache object and
            handlers for when data cannot be found.

        Args:
            key (string): A key value to return the requested value from
            self.__data dictionary.

        Returns:
            string: Returns the value in the self.__data dictionary.

        Examples:
            >>> print pcache['test']
            'hello'
        """
        try:
            return self.__data[key]
        except (TypeError, KeyError):
            print 'Error: Key cannot be found'

    def __delitem__(self, key):
        """A Magic Method that deletes data from the PickleCache object.

        Args:
            key (string): A key value to delete the key-value from
            self.__data dictionary.
        """
        try:
            del self.__data[key]
            if self.autosync is True:
                self.flush()
        except (TypeError, KeyError):
            print 'Error: Key cannot be found'

    def load(self):
        """A function that loads data from the filepath class attribute into the
            self.__data dictionary..

        Args:
            None.
        """
        exists = os.path.exists(self.__file_path)
        size = os.path.getsize(self.__file_path)
        if exists and size > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """A function that writes data to the filepath class attribute using the
            data in the self.__data dictionary.

        Args:
            None.
        """
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
