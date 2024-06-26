# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SchedulesSwitchBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, schedule_id: str=None, guard_id_from: str=None, guard_id_to: str=None):  # noqa: E501
        """SchedulesSwitchBody - a model defined in Swagger

        :param schedule_id: The schedule_id of this SchedulesSwitchBody.  # noqa: E501
        :type schedule_id: str
        :param guard_id_from: The guard_id_from of this SchedulesSwitchBody.  # noqa: E501
        :type guard_id_from: str
        :param guard_id_to: The guard_id_to of this SchedulesSwitchBody.  # noqa: E501
        :type guard_id_to: str
        """
        self.swagger_types = {
            'schedule_id': str,
            'guard_id_from': str,
            'guard_id_to': str
        }

        self.attribute_map = {
            'schedule_id': 'scheduleId',
            'guard_id_from': 'guardIdFrom',
            'guard_id_to': 'guardIdTo'
        }
        self._schedule_id = schedule_id
        self._guard_id_from = guard_id_from
        self._guard_id_to = guard_id_to

    @classmethod
    def from_dict(cls, dikt) -> 'SchedulesSwitchBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The schedules_switch_body of this SchedulesSwitchBody.  # noqa: E501
        :rtype: SchedulesSwitchBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schedule_id(self) -> str:
        """Gets the schedule_id of this SchedulesSwitchBody.

        The ID of the schedule to be switched.  # noqa: E501

        :return: The schedule_id of this SchedulesSwitchBody.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id: str):
        """Sets the schedule_id of this SchedulesSwitchBody.

        The ID of the schedule to be switched.  # noqa: E501

        :param schedule_id: The schedule_id of this SchedulesSwitchBody.
        :type schedule_id: str
        """
        if schedule_id is None:
            raise ValueError("Invalid value for `schedule_id`, must not be `None`")  # noqa: E501

        self._schedule_id = schedule_id

    @property
    def guard_id_from(self) -> str:
        """Gets the guard_id_from of this SchedulesSwitchBody.

        The ID of the guard currently assigned to the schedule.  # noqa: E501

        :return: The guard_id_from of this SchedulesSwitchBody.
        :rtype: str
        """
        return self._guard_id_from

    @guard_id_from.setter
    def guard_id_from(self, guard_id_from: str):
        """Sets the guard_id_from of this SchedulesSwitchBody.

        The ID of the guard currently assigned to the schedule.  # noqa: E501

        :param guard_id_from: The guard_id_from of this SchedulesSwitchBody.
        :type guard_id_from: str
        """
        if guard_id_from is None:
            raise ValueError("Invalid value for `guard_id_from`, must not be `None`")  # noqa: E501

        self._guard_id_from = guard_id_from

    @property
    def guard_id_to(self) -> str:
        """Gets the guard_id_to of this SchedulesSwitchBody.

        The ID of the guard to whom the schedule will be reassigned.  # noqa: E501

        :return: The guard_id_to of this SchedulesSwitchBody.
        :rtype: str
        """
        return self._guard_id_to

    @guard_id_to.setter
    def guard_id_to(self, guard_id_to: str):
        """Sets the guard_id_to of this SchedulesSwitchBody.

        The ID of the guard to whom the schedule will be reassigned.  # noqa: E501

        :param guard_id_to: The guard_id_to of this SchedulesSwitchBody.
        :type guard_id_to: str
        """
        if guard_id_to is None:
            raise ValueError("Invalid value for `guard_id_to`, must not be `None`")  # noqa: E501

        self._guard_id_to = guard_id_to
