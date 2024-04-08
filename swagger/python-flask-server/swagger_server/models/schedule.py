# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Schedule(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, guard_id: str=None, time: datetime=None, location_id: str=None):  # noqa: E501
        """Schedule - a model defined in Swagger

        :param id: The id of this Schedule.  # noqa: E501
        :type id: str
        :param guard_id: The guard_id of this Schedule.  # noqa: E501
        :type guard_id: str
        :param time: The time of this Schedule.  # noqa: E501
        :type time: datetime
        :param location_id: The location_id of this Schedule.  # noqa: E501
        :type location_id: str
        """
        self.swagger_types = {
            'id': str,
            'guard_id': str,
            'time': datetime,
            'location_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'guard_id': 'guardId',
            'time': 'time',
            'location_id': 'locationId'
        }
        self._id = id
        self._guard_id = guard_id
        self._time = time
        self._location_id = location_id

    @classmethod
    def from_dict(cls, dikt) -> 'Schedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Schedule of this Schedule.  # noqa: E501
        :rtype: Schedule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Schedule.

        The unique identifier of the schedule.  # noqa: E501

        :return: The id of this Schedule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Schedule.

        The unique identifier of the schedule.  # noqa: E501

        :param id: The id of this Schedule.
        :type id: str
        """

        self._id = id

    @property
    def guard_id(self) -> str:
        """Gets the guard_id of this Schedule.

        The unique identifier of the guard.  # noqa: E501

        :return: The guard_id of this Schedule.
        :rtype: str
        """
        return self._guard_id

    @guard_id.setter
    def guard_id(self, guard_id: str):
        """Sets the guard_id of this Schedule.

        The unique identifier of the guard.  # noqa: E501

        :param guard_id: The guard_id of this Schedule.
        :type guard_id: str
        """
        if guard_id is None:
            raise ValueError("Invalid value for `guard_id`, must not be `None`")  # noqa: E501

        self._guard_id = guard_id

    @property
    def time(self) -> datetime:
        """Gets the time of this Schedule.

        The scheduled start time, with conflict checks.  # noqa: E501

        :return: The time of this Schedule.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this Schedule.

        The scheduled start time, with conflict checks.  # noqa: E501

        :param time: The time of this Schedule.
        :type time: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def location_id(self) -> str:
        """Gets the location_id of this Schedule.

        The unique identifier of the location, referencing the Location schema.  # noqa: E501

        :return: The location_id of this Schedule.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id: str):
        """Sets the location_id of this Schedule.

        The unique identifier of the location, referencing the Location schema.  # noqa: E501

        :param location_id: The location_id of this Schedule.
        :type location_id: str
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id
