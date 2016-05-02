# -*- coding: utf-8 -*-
"""
Created on 23.04.16
Created for FcstSystem

@author: Tobias Sebastian Finn, tobias.sebastian.finn@studium.uni-hamburg.de

    Copyright (C) {2016}  {Tobias Sebastian Finn}

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
import os
import json

# External modules
import datetime

# Internal modules
import pyMepps

__version__ = "0.1"


class System(object):
    def __init__(self, config=None):
        """
        The system represents the forecasting system with its components.
        The system starts every component of the forecasting system,
        like the stations and the models.
        Args:
            config (str): path to the config file
        #    name (str): name of the forecasting system
        #    stations (list): list with pyMepps.station instances
        #    models (list): list with pyMepps.model instances
        #    forecasts (list): list with pyMepps.forecast instances
        #    verifications (list): list with pyMepps.verification instances
        #    plots (list): list with pyMepps.plot instances
        #    logger (pyMepps.log): initialized pyMepps.log.logger instance

        Attributes:
            name (str): name of the forecasting system
            base_path (str): base path of the system
            stations (list): list with pyMepps.station instances
            models (list): list with pyMepps.model instances
            forecasts (list): list with pyMepps.forecast instances
            verifications (list): list with pyMepps.verification instances
            plots (list): list with pyMepps.plot instances
            base_logger (pyMepps.log): initialized pyMepps.log.logger_template
            logger (pyMepps.log): initialized pyMepps.log.logger
            date (datetime.datetime): the starting date of the system in UTC
        """
        self.name = ""
        self.stations = []
        self.models = []
        self.forecasts = []
        self.verifications = []
        self.plots = []
        self.base_path = ""
        self.data_path = ""
        self.plot_path = ""
        self.base_logger = None
        self.logger = None
        self.date = datetime.datetime.utcnow()
        if os.path.isfile(config):
            self.readConfig(config)

    def readConfig(self, config_path):
        """
        readConfig reads a config file for the forecasting system.

        Args:
            config_path (str): path to the config file
        """
        with open(config_path) as f:
            data = json.load(f)
        if "name" in data:
            self.name = data["name"]
        if "base_path" in data:
            self.base_path = data["base_path"]
        if "data_path" in data:
            self.data_path = self.joinBasePath(self.base_path,
                                               data["data_path"])
        else:
            self.data_path = os.path.join(self.base_path, "data")
        if "plot_path" in data:
            self.plot_path = self.joinPath(self.base_path,
                                           data["plot_path"])
        else:
            self.plot_path = os.path.join(self.base_path, "graphs")

        # read the logger
        if "log" in data and data["log"]["logger"]:
            if "path" in data["log"]:
                log_path = self.joinPath(self.base_path,
                                         data["log"]["path"])
            else:
                log_path = os.path.join(self.base_path, "logs")
            self.base_logger = pyMepps.log.LoggerTemplate(log_path,
                                                          data["log"]["file_name"])
            self.logger = self.base_logger.createLogger("system")

        #read the component configs
        if "components_config" in data:
            configs = data["components_config"]
            if "base_path" in configs:
                config_path = self.joinPath(self.base_path,
                                            configs["base_path"])
            else:
                config_path = os.path.join(self.base_path, "configs")
            if "station" in configs:
                station_path = self.joinPath(config_path, configs["station"])
                with open(station_path) as f:
                    station_config = json.load(f)
                    for station in station_config:
                        self.stations.append()


    @staticmethod
    def joinPath(base_path, join_path):
        """
        If join_path is an absolute path the method returns the path, else
        the return path will be the base path plus the join path

        Args:
            base_path (str): the base path
            join_path (str): path which should be joined to the base path

        Returns:
            path (str): the absolute path
        """
        if os.path.isabs(join_path):
            path = join_path
        else:
            path = os.path.join(base_path, join_path)
        return path

    def start(self):
        """
        start starts the forecasting system. Every component of the forecasting
        system is also started in this method.
        """
        pass
