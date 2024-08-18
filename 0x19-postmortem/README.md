# Incident Report: Web Server Outage Due to Nginx Configuration Error (18-20 August 2024)

## Issue Summary

- **Duration**:

  - Start: 18-08-2024, 9:00 AM WAT

  - End: 20-08-2024, 4:00 PM WAT

- **Impact**:

The web server experienced downtime due to an issue with the Nginx service, affecting the load balancer's ability to distribute requests to the web-02 server. As a result, web-01 was overloaded, leading to degraded performance. Approximately 60% of our users were impacted, as the majority of read requests are handled by web-02. Recent analysis showed an increase in read requests, further exacerbating the issue. The root cause was a human error that resulted in the deletion of the Nginx configuration file.

## Timeline

- **08:00 AM WAT, 18th August 2024**: The issue was detected.

- **09:00 AM WAT**: A monitoring alert was triggered due to a significant decrease in requests to web-02 and a corresponding increase on web-01.

- **10:00 AM WAT**: Initial troubleshooting focused on restarting the web-02 server, assuming it was down, but these efforts were unsuccessful.

- **11:00 AM WAT**: Upon further investigation, it was discovered that the Nginx configuration file on web-02 had been accidentally deleted.

- **12:00 PM WAT**: The DevOps team was engaged to restore the Nginx configuration file by copying it from web-01 to web-02. Manual adjustments were necessary due to differences between the servers.

- **04:00 PM WAT, 20th August 2024**: The issue was fully resolved, and the system was restored to its previous state.

## Root Cause and Resolution

- **Root Cause**: The issue was caused by a human error. An engineer intended to delete a backup of the Nginx configuration file using a wildcard in a command but accidentally deleted the main configuration file as well. As the engineer was operating as the root user, the command executed without any prompt for confirmation, leading to the deletion.

- **Resolution**: The DevOps team promptly restored the Nginx configuration by copying it from web-01 to web-02. Given that web-02 is a replica node, some manual adjustments were required to account for differences between the servers. The issue was resolved immediately after the configuration was restored.

## Corrective and Preventative Measures

- **Backup Strategy**: Implement a robust backup strategy by automating the backup of Nginx configuration files to a secure environment, such as Google Cloud. This ensures that critical configuration files are protected and can be easily restored if needed.

- **Access Control**: Limit the use of root access for routine tasks. Engineers should operate with non-privileged accounts whenever possible to minimize the risk of accidental deletions.

- **Nginx Optimization**: Optimize the Nginx configuration to improve overall performance, including increasing the number of worker processes to handle requests more efficiently.

- **Action Items**:

  - Automate the backup of Nginx configurations to Google Cloud.

  - Configure Nginx to increase the number of worker processes to enhance performance.
