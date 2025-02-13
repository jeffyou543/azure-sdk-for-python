# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from ._configuration import FrontDoorManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    EndpointsOperations,
    ExperimentsOperations,
    FrontDoorNameAvailabilityOperations,
    FrontDoorNameAvailabilityWithSubscriptionOperations,
    FrontDoorsOperations,
    FrontendEndpointsOperations,
    ManagedRuleSetsOperations,
    NetworkExperimentProfilesOperations,
    PoliciesOperations,
    PreconfiguredEndpointsOperations,
    ReportsOperations,
    RulesEnginesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class FrontDoorManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """FrontDoor Client.

    :ivar policies: PoliciesOperations operations
    :vartype policies: azure.mgmt.frontdoor.operations.PoliciesOperations
    :ivar managed_rule_sets: ManagedRuleSetsOperations operations
    :vartype managed_rule_sets: azure.mgmt.frontdoor.operations.ManagedRuleSetsOperations
    :ivar front_door_name_availability: FrontDoorNameAvailabilityOperations operations
    :vartype front_door_name_availability:
     azure.mgmt.frontdoor.operations.FrontDoorNameAvailabilityOperations
    :ivar front_door_name_availability_with_subscription:
     FrontDoorNameAvailabilityWithSubscriptionOperations operations
    :vartype front_door_name_availability_with_subscription:
     azure.mgmt.frontdoor.operations.FrontDoorNameAvailabilityWithSubscriptionOperations
    :ivar front_doors: FrontDoorsOperations operations
    :vartype front_doors: azure.mgmt.frontdoor.operations.FrontDoorsOperations
    :ivar frontend_endpoints: FrontendEndpointsOperations operations
    :vartype frontend_endpoints: azure.mgmt.frontdoor.operations.FrontendEndpointsOperations
    :ivar endpoints: EndpointsOperations operations
    :vartype endpoints: azure.mgmt.frontdoor.operations.EndpointsOperations
    :ivar rules_engines: RulesEnginesOperations operations
    :vartype rules_engines: azure.mgmt.frontdoor.operations.RulesEnginesOperations
    :ivar network_experiment_profiles: NetworkExperimentProfilesOperations operations
    :vartype network_experiment_profiles:
     azure.mgmt.frontdoor.operations.NetworkExperimentProfilesOperations
    :ivar preconfigured_endpoints: PreconfiguredEndpointsOperations operations
    :vartype preconfigured_endpoints:
     azure.mgmt.frontdoor.operations.PreconfiguredEndpointsOperations
    :ivar experiments: ExperimentsOperations operations
    :vartype experiments: azure.mgmt.frontdoor.operations.ExperimentsOperations
    :ivar reports: ReportsOperations operations
    :vartype reports: azure.mgmt.frontdoor.operations.ReportsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft
     Azure subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = FrontDoorManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.policies = PoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.managed_rule_sets = ManagedRuleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.front_door_name_availability = FrontDoorNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.front_door_name_availability_with_subscription = FrontDoorNameAvailabilityWithSubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.front_doors = FrontDoorsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.frontend_endpoints = FrontendEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.endpoints = EndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.rules_engines = RulesEnginesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.network_experiment_profiles = NetworkExperimentProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.preconfigured_endpoints = PreconfiguredEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.experiments = ExperimentsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.reports = ReportsOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "FrontDoorManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details) -> None:
        self._client.__exit__(*exc_details)
