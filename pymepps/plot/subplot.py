#!/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 10.01.17

Created for pymepps

@author: Tobias Sebastian Finn, tobias.sebastian.finn@studium.uni-hamburg.de

    Copyright (C) {2017}  {Tobias Sebastian Finn}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# System modules
import abc
import logging

# External modules
import matplotlib.pyplot as plt

# Internal modules


logger = logging.getLogger(__name__)


class Subplot(object):
    def __init__(self, *args, **kwargs):
        self.ax = plt.subplot(*args, **kwargs)

    def __getattr__(self, item):
        return getattr(self.ax, item)

    def _extract_data(self, data):
        return data

    def plot_method(self, data, method='plot', *args, **kwargs):
        extracted_data = self._extract_data(data)
        getattr(self.ax, method)(*extracted_data, *args, **kwargs)
        return self
