from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_forget_install_component_request import ServiceForgetInstallComponentRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    component_id: str,
    *,
    body: ServiceForgetInstallComponentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/installs/{install_id}/components/{component_id}/forget".format(
            install_id=quote(str(install_id), safe=""),
            component_id=quote(str(component_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StderrErrResponse | bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceForgetInstallComponentRequest,
) -> Response[StderrErrResponse | bool]:
    """forget an install component

     # Forget Install Component

    Permanently forget (soft delete) an install component from the system. This operation marks the
    install component as deleted while preserving the record for audit purposes.

    ## Use Cases

    - Remove a component that is no longer needed from an install
    - Clean up failed or orphaned install components
    - Prepare for reinstalling a component from scratch

    ## Important Notes

    - This is a **soft delete** operation - the record is marked as deleted but remains in the database
    - The component will no longer appear in API responses or dashboard views
    - Associated resources (terraform state, deploys, etc.) are preserved via soft delete
    - This operation is **irreversible** via the API
    - To restore, database-level operations would be required

    ## Prerequisites

    - Install must exist and belong to the authenticated organization
    - Component must exist for the specified install
    - User must have appropriate permissions for the install's organization
    - Component must be removed from the app configuration (sync required)

    ## Behavior

    1. Validates install exists and belongs to org
    2. Validates install component exists
    3. Validates component is not in the app configuration
    4. Soft deletes the install component record
    5. Cascades soft delete to associated resources (via GORM associations)
    6. Sends event loop signal for any cleanup workflows
    7. Returns success response

    ## Validation

    Before forgetting an install component, the system validates that the component no longer exists in
    the app configuration. If the component is still in the app config, the request will fail with a
    user-friendly error message.

    **To resolve this error:**

    1. Remove the component from your `nuon.yaml` file
    2. Run `nuon apps sync` to update the app configuration
    3. Retry the forget operation

    ## Related Endpoints

    - `DELETE /v1/installs/{install_id}` - Delete entire install
    - `POST /v1/installs/{install_id}/forget` - Forget entire install
    - `POST /v1/installs/{install_id}/components/{component_id}/teardown` - Teardown component
    infrastructure

    Args:
        install_id (str):
        component_id (str):
        body (ServiceForgetInstallComponentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | bool]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceForgetInstallComponentRequest,
) -> StderrErrResponse | bool | None:
    """forget an install component

     # Forget Install Component

    Permanently forget (soft delete) an install component from the system. This operation marks the
    install component as deleted while preserving the record for audit purposes.

    ## Use Cases

    - Remove a component that is no longer needed from an install
    - Clean up failed or orphaned install components
    - Prepare for reinstalling a component from scratch

    ## Important Notes

    - This is a **soft delete** operation - the record is marked as deleted but remains in the database
    - The component will no longer appear in API responses or dashboard views
    - Associated resources (terraform state, deploys, etc.) are preserved via soft delete
    - This operation is **irreversible** via the API
    - To restore, database-level operations would be required

    ## Prerequisites

    - Install must exist and belong to the authenticated organization
    - Component must exist for the specified install
    - User must have appropriate permissions for the install's organization
    - Component must be removed from the app configuration (sync required)

    ## Behavior

    1. Validates install exists and belongs to org
    2. Validates install component exists
    3. Validates component is not in the app configuration
    4. Soft deletes the install component record
    5. Cascades soft delete to associated resources (via GORM associations)
    6. Sends event loop signal for any cleanup workflows
    7. Returns success response

    ## Validation

    Before forgetting an install component, the system validates that the component no longer exists in
    the app configuration. If the component is still in the app config, the request will fail with a
    user-friendly error message.

    **To resolve this error:**

    1. Remove the component from your `nuon.yaml` file
    2. Run `nuon apps sync` to update the app configuration
    3. Retry the forget operation

    ## Related Endpoints

    - `DELETE /v1/installs/{install_id}` - Delete entire install
    - `POST /v1/installs/{install_id}/forget` - Forget entire install
    - `POST /v1/installs/{install_id}/components/{component_id}/teardown` - Teardown component
    infrastructure

    Args:
        install_id (str):
        component_id (str):
        body (ServiceForgetInstallComponentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | bool
    """

    return sync_detailed(
        install_id=install_id,
        component_id=component_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceForgetInstallComponentRequest,
) -> Response[StderrErrResponse | bool]:
    """forget an install component

     # Forget Install Component

    Permanently forget (soft delete) an install component from the system. This operation marks the
    install component as deleted while preserving the record for audit purposes.

    ## Use Cases

    - Remove a component that is no longer needed from an install
    - Clean up failed or orphaned install components
    - Prepare for reinstalling a component from scratch

    ## Important Notes

    - This is a **soft delete** operation - the record is marked as deleted but remains in the database
    - The component will no longer appear in API responses or dashboard views
    - Associated resources (terraform state, deploys, etc.) are preserved via soft delete
    - This operation is **irreversible** via the API
    - To restore, database-level operations would be required

    ## Prerequisites

    - Install must exist and belong to the authenticated organization
    - Component must exist for the specified install
    - User must have appropriate permissions for the install's organization
    - Component must be removed from the app configuration (sync required)

    ## Behavior

    1. Validates install exists and belongs to org
    2. Validates install component exists
    3. Validates component is not in the app configuration
    4. Soft deletes the install component record
    5. Cascades soft delete to associated resources (via GORM associations)
    6. Sends event loop signal for any cleanup workflows
    7. Returns success response

    ## Validation

    Before forgetting an install component, the system validates that the component no longer exists in
    the app configuration. If the component is still in the app config, the request will fail with a
    user-friendly error message.

    **To resolve this error:**

    1. Remove the component from your `nuon.yaml` file
    2. Run `nuon apps sync` to update the app configuration
    3. Retry the forget operation

    ## Related Endpoints

    - `DELETE /v1/installs/{install_id}` - Delete entire install
    - `POST /v1/installs/{install_id}/forget` - Forget entire install
    - `POST /v1/installs/{install_id}/components/{component_id}/teardown` - Teardown component
    infrastructure

    Args:
        install_id (str):
        component_id (str):
        body (ServiceForgetInstallComponentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | bool]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceForgetInstallComponentRequest,
) -> StderrErrResponse | bool | None:
    """forget an install component

     # Forget Install Component

    Permanently forget (soft delete) an install component from the system. This operation marks the
    install component as deleted while preserving the record for audit purposes.

    ## Use Cases

    - Remove a component that is no longer needed from an install
    - Clean up failed or orphaned install components
    - Prepare for reinstalling a component from scratch

    ## Important Notes

    - This is a **soft delete** operation - the record is marked as deleted but remains in the database
    - The component will no longer appear in API responses or dashboard views
    - Associated resources (terraform state, deploys, etc.) are preserved via soft delete
    - This operation is **irreversible** via the API
    - To restore, database-level operations would be required

    ## Prerequisites

    - Install must exist and belong to the authenticated organization
    - Component must exist for the specified install
    - User must have appropriate permissions for the install's organization
    - Component must be removed from the app configuration (sync required)

    ## Behavior

    1. Validates install exists and belongs to org
    2. Validates install component exists
    3. Validates component is not in the app configuration
    4. Soft deletes the install component record
    5. Cascades soft delete to associated resources (via GORM associations)
    6. Sends event loop signal for any cleanup workflows
    7. Returns success response

    ## Validation

    Before forgetting an install component, the system validates that the component no longer exists in
    the app configuration. If the component is still in the app config, the request will fail with a
    user-friendly error message.

    **To resolve this error:**

    1. Remove the component from your `nuon.yaml` file
    2. Run `nuon apps sync` to update the app configuration
    3. Retry the forget operation

    ## Related Endpoints

    - `DELETE /v1/installs/{install_id}` - Delete entire install
    - `POST /v1/installs/{install_id}/forget` - Forget entire install
    - `POST /v1/installs/{install_id}/components/{component_id}/teardown` - Teardown component
    infrastructure

    Args:
        install_id (str):
        component_id (str):
        body (ServiceForgetInstallComponentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | bool
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            component_id=component_id,
            client=client,
            body=body,
        )
    ).parsed
