Services 
---

The Services scripts are configurable services examples that perform various functions, 
which continue running on **ClearML Server**. They execute in [ClearML Agent services mode](https://clear.ml/docs/latest/docs/clearml_agent#services-mode). 

The services include: 
* [ClearML AWS Autoscaler](aws-autoscaler/aws_autoscaler.py) - Optimizes AWS EC2 instance scaling according to the budget 
  you configure.
* [Cleanup Service](cleanup/cleanup_service.py) - Deletes Archived Tasks, and their associated artifacts and debug samples, 
  based on configurable parameter criteria.
* [Monitoring Service Posting Slack Alerts](monitoring/slack_alerts.py) - Monitors Task completion / failure based on 
  configurable parameter criteria and post alerts to your Slack channel.
  