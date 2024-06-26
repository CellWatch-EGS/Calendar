# coding: utf-8

"""
    Prison Guard Scheduling API

    This API manages the schedules of prison guards, ensuring a guard cannot be scheduled to be in two places at the same time. It supports querying schedules by guard ID and location name.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def schedules_get(self, **kwargs):  # noqa: E501
        """Get a list of all schedules  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Schedule]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.schedules_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def schedules_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of all schedules  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Schedule]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/schedules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Schedule]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_guard_guard_id_get(self, guard_id, **kwargs):  # noqa: E501
        """Get schedules by guard ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_guard_guard_id_get(guard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guard_id: (required)
        :return: list[Schedule]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_guard_guard_id_get_with_http_info(guard_id, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_guard_guard_id_get_with_http_info(guard_id, **kwargs)  # noqa: E501
            return data

    def schedules_guard_guard_id_get_with_http_info(self, guard_id, **kwargs):  # noqa: E501
        """Get schedules by guard ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_guard_guard_id_get_with_http_info(guard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guard_id: (required)
        :return: list[Schedule]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['guard_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_guard_guard_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'guard_id' is set
        if ('guard_id' not in params or
                params['guard_id'] is None):
            raise ValueError("Missing the required parameter `guard_id` when calling `schedules_guard_guard_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'guard_id' in params:
            path_params['guardId'] = params['guard_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/schedules/guard/{guardId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Schedule]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_location_location_name_get(self, location_name, **kwargs):  # noqa: E501
        """Get schedules by location name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_location_location_name_get(location_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str location_name: (required)
        :return: list[Schedule]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_location_location_name_get_with_http_info(location_name, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_location_location_name_get_with_http_info(location_name, **kwargs)  # noqa: E501
            return data

    def schedules_location_location_name_get_with_http_info(self, location_name, **kwargs):  # noqa: E501
        """Get schedules by location name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_location_location_name_get_with_http_info(location_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str location_name: (required)
        :return: list[Schedule]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_location_location_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_name' is set
        if ('location_name' not in params or
                params['location_name'] is None):
            raise ValueError("Missing the required parameter `location_name` when calling `schedules_location_location_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_name' in params:
            path_params['locationName'] = params['location_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/schedules/location/{locationName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Schedule]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_post(self, body, **kwargs):  # noqa: E501
        """Create a new schedule  # noqa: E501

        Creates a new schedule entry for a guard, checking for conflicts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def schedules_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new schedule  # noqa: E501

        Creates a new schedule entry for a guard, checking for conflicts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `schedules_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/schedules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_schedule_id_delete(self, schedule_id, **kwargs):  # noqa: E501
        """Delete a schedule by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_id_delete(schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str schedule_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_schedule_id_delete_with_http_info(schedule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_schedule_id_delete_with_http_info(schedule_id, **kwargs)  # noqa: E501
            return data

    def schedules_schedule_id_delete_with_http_info(self, schedule_id, **kwargs):  # noqa: E501
        """Delete a schedule by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_id_delete_with_http_info(schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str schedule_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_schedule_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params or
                params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `schedules_schedule_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/schedules/{scheduleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_schedule_id_get(self, schedule_id, **kwargs):  # noqa: E501
        """Get a specific schedule by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_id_get(schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str schedule_id: (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_schedule_id_get_with_http_info(schedule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_schedule_id_get_with_http_info(schedule_id, **kwargs)  # noqa: E501
            return data

    def schedules_schedule_id_get_with_http_info(self, schedule_id, **kwargs):  # noqa: E501
        """Get a specific schedule by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_id_get_with_http_info(schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str schedule_id: (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_schedule_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params or
                params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `schedules_schedule_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/schedules/{scheduleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Schedule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_schedule_id_put(self, body, schedule_id, **kwargs):  # noqa: E501
        """Update a schedule by ID  # noqa: E501

        Updates an existing schedule, checking for conflicts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_id_put(body, schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: (required)
        :param str schedule_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_schedule_id_put_with_http_info(body, schedule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_schedule_id_put_with_http_info(body, schedule_id, **kwargs)  # noqa: E501
            return data

    def schedules_schedule_id_put_with_http_info(self, body, schedule_id, **kwargs):  # noqa: E501
        """Update a schedule by ID  # noqa: E501

        Updates an existing schedule, checking for conflicts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_schedule_id_put_with_http_info(body, schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: (required)
        :param str schedule_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'schedule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_schedule_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `schedules_schedule_id_put`")  # noqa: E501
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params or
                params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `schedules_schedule_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/schedules/{scheduleId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedules_switch_post(self, body, **kwargs):  # noqa: E501
        """Switch a schedule between two guards  # noqa: E501

        Allows the swapping of a specific schedule from one guard to another.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_switch_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SchedulesSwitchBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.schedules_switch_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.schedules_switch_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def schedules_switch_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Switch a schedule between two guards  # noqa: E501

        Allows the swapping of a specific schedule from one guard to another.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedules_switch_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SchedulesSwitchBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedules_switch_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `schedules_switch_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/schedules/switch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
