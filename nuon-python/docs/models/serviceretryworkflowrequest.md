# ServiceRetryWorkflowRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `operation`                                              | *Optional[str]*                                          | :heavy_minus_sign:                                       | Retry indicates whether to retry the current step or not |
| `step_id`                                                | *Optional[str]*                                          | :heavy_minus_sign:                                       | StepID is the ID of the step to start the retry from     |
| `workflow_id`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |