# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_create_or_replace_request(
    resource_group_name: str,
    job_name: str,
    transformation_name: str,
    subscription_id: str,
    *,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2021-10-01-preview")
    )  # type: Literal["2021-10-01-preview"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "jobName": _SERIALIZER.url("job_name", job_name, "str"),
        "transformationName": _SERIALIZER.url("transformation_name", transformation_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(
    resource_group_name: str,
    job_name: str,
    transformation_name: str,
    subscription_id: str,
    *,
    if_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2021-10-01-preview")
    )  # type: Literal["2021-10-01-preview"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "jobName": _SERIALIZER.url("job_name", job_name, "str"),
        "transformationName": _SERIALIZER.url("transformation_name", transformation_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, job_name: str, transformation_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2021-10-01-preview")
    )  # type: Literal["2021-10-01-preview"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "jobName": _SERIALIZER.url("job_name", job_name, "str"),
        "transformationName": _SERIALIZER.url("transformation_name", transformation_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class TransformationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.streamanalytics.StreamAnalyticsManagementClient`'s
        :attr:`transformations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create_or_replace(
        self,
        resource_group_name: str,
        job_name: str,
        transformation_name: str,
        transformation: _models.Transformation,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Transformation:
        """Creates a transformation or replaces an already existing transformation under an existing
        streaming job.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param job_name: The name of the streaming job. Required.
        :type job_name: str
        :param transformation_name: The name of the transformation. Required.
        :type transformation_name: str
        :param transformation: The definition of the transformation that will be used to create a new
         transformation or replace the existing one under the streaming job. Required.
        :type transformation: ~azure.mgmt.streamanalytics.models.Transformation
        :param if_match: The ETag of the transformation. Omit this value to always overwrite the
         current transformation. Specify the last-seen ETag value to prevent accidentally overwriting
         concurrent changes. Default value is None.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new transformation to be created, but to prevent
         updating an existing transformation. Other values will result in a 412 Pre-condition Failed
         response. Default value is None.
        :type if_none_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Transformation or the result of cls(response)
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_replace(
        self,
        resource_group_name: str,
        job_name: str,
        transformation_name: str,
        transformation: IO,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Transformation:
        """Creates a transformation or replaces an already existing transformation under an existing
        streaming job.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param job_name: The name of the streaming job. Required.
        :type job_name: str
        :param transformation_name: The name of the transformation. Required.
        :type transformation_name: str
        :param transformation: The definition of the transformation that will be used to create a new
         transformation or replace the existing one under the streaming job. Required.
        :type transformation: IO
        :param if_match: The ETag of the transformation. Omit this value to always overwrite the
         current transformation. Specify the last-seen ETag value to prevent accidentally overwriting
         concurrent changes. Default value is None.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new transformation to be created, but to prevent
         updating an existing transformation. Other values will result in a 412 Pre-condition Failed
         response. Default value is None.
        :type if_none_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Transformation or the result of cls(response)
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_replace(
        self,
        resource_group_name: str,
        job_name: str,
        transformation_name: str,
        transformation: Union[_models.Transformation, IO],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Transformation:
        """Creates a transformation or replaces an already existing transformation under an existing
        streaming job.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param job_name: The name of the streaming job. Required.
        :type job_name: str
        :param transformation_name: The name of the transformation. Required.
        :type transformation_name: str
        :param transformation: The definition of the transformation that will be used to create a new
         transformation or replace the existing one under the streaming job. Is either a model type or a
         IO type. Required.
        :type transformation: ~azure.mgmt.streamanalytics.models.Transformation or IO
        :param if_match: The ETag of the transformation. Omit this value to always overwrite the
         current transformation. Specify the last-seen ETag value to prevent accidentally overwriting
         concurrent changes. Default value is None.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new transformation to be created, but to prevent
         updating an existing transformation. Other values will result in a 412 Pre-condition Failed
         response. Default value is None.
        :type if_none_match: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Transformation or the result of cls(response)
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-10-01-preview")
        )  # type: Literal["2021-10-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Transformation]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(transformation, (IO, bytes)):
            _content = transformation
        else:
            _json = self._serialize.body(transformation, "Transformation")

        request = build_create_or_replace_request(
            resource_group_name=resource_group_name,
            job_name=job_name,
            transformation_name=transformation_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_replace.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

            deserialized = self._deserialize("Transformation", pipeline_response)

        if response.status_code == 201:
            response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

            deserialized = self._deserialize("Transformation", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    create_or_replace.metadata = {"url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}"}  # type: ignore

    @overload
    def update(
        self,
        resource_group_name: str,
        job_name: str,
        transformation_name: str,
        transformation: _models.Transformation,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Transformation:
        """Updates an existing transformation under an existing streaming job. This can be used to
        partially update (ie. update one or two properties) a transformation without affecting the rest
        the job or transformation definition.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param job_name: The name of the streaming job. Required.
        :type job_name: str
        :param transformation_name: The name of the transformation. Required.
        :type transformation_name: str
        :param transformation: A Transformation object. The properties specified here will overwrite
         the corresponding properties in the existing transformation (ie. Those properties will be
         updated). Any properties that are set to null here will mean that the corresponding property in
         the existing transformation will remain the same and not change as a result of this PATCH
         operation. Required.
        :type transformation: ~azure.mgmt.streamanalytics.models.Transformation
        :param if_match: The ETag of the transformation. Omit this value to always overwrite the
         current transformation. Specify the last-seen ETag value to prevent accidentally overwriting
         concurrent changes. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Transformation or the result of cls(response)
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        resource_group_name: str,
        job_name: str,
        transformation_name: str,
        transformation: IO,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Transformation:
        """Updates an existing transformation under an existing streaming job. This can be used to
        partially update (ie. update one or two properties) a transformation without affecting the rest
        the job or transformation definition.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param job_name: The name of the streaming job. Required.
        :type job_name: str
        :param transformation_name: The name of the transformation. Required.
        :type transformation_name: str
        :param transformation: A Transformation object. The properties specified here will overwrite
         the corresponding properties in the existing transformation (ie. Those properties will be
         updated). Any properties that are set to null here will mean that the corresponding property in
         the existing transformation will remain the same and not change as a result of this PATCH
         operation. Required.
        :type transformation: IO
        :param if_match: The ETag of the transformation. Omit this value to always overwrite the
         current transformation. Specify the last-seen ETag value to prevent accidentally overwriting
         concurrent changes. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Transformation or the result of cls(response)
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        job_name: str,
        transformation_name: str,
        transformation: Union[_models.Transformation, IO],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Transformation:
        """Updates an existing transformation under an existing streaming job. This can be used to
        partially update (ie. update one or two properties) a transformation without affecting the rest
        the job or transformation definition.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param job_name: The name of the streaming job. Required.
        :type job_name: str
        :param transformation_name: The name of the transformation. Required.
        :type transformation_name: str
        :param transformation: A Transformation object. The properties specified here will overwrite
         the corresponding properties in the existing transformation (ie. Those properties will be
         updated). Any properties that are set to null here will mean that the corresponding property in
         the existing transformation will remain the same and not change as a result of this PATCH
         operation. Is either a model type or a IO type. Required.
        :type transformation: ~azure.mgmt.streamanalytics.models.Transformation or IO
        :param if_match: The ETag of the transformation. Omit this value to always overwrite the
         current transformation. Specify the last-seen ETag value to prevent accidentally overwriting
         concurrent changes. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Transformation or the result of cls(response)
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-10-01-preview")
        )  # type: Literal["2021-10-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Transformation]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(transformation, (IO, bytes)):
            _content = transformation
        else:
            _json = self._serialize.body(transformation, "Transformation")

        request = build_update_request(
            resource_group_name=resource_group_name,
            job_name=job_name,
            transformation_name=transformation_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("Transformation", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}"}  # type: ignore

    @distributed_trace
    def get(
        self, resource_group_name: str, job_name: str, transformation_name: str, **kwargs: Any
    ) -> _models.Transformation:
        """Gets details about the specified transformation.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param job_name: The name of the streaming job. Required.
        :type job_name: str
        :param transformation_name: The name of the transformation. Required.
        :type transformation_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Transformation or the result of cls(response)
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-10-01-preview")
        )  # type: Literal["2021-10-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Transformation]

        request = build_get_request(
            resource_group_name=resource_group_name,
            job_name=job_name,
            transformation_name=transformation_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("Transformation", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}"}  # type: ignore
