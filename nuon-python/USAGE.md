<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_config_id="<id>")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from nuon import Nuon, models
import os

async def main():

    async with Nuon() as n_client:

        res = await n_client.actions.get_action_workflow_config_async(security=models.GetActionWorkflowConfigSecurity(
            api_key=os.getenv("NUON_API_KEY", ""),
        ), action_workflow_config_id="<id>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->