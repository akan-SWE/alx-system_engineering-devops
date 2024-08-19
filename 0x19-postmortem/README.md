# Incident Report: Web Server Outage Due to Nginx Configuration Error (18-20 August 2024)

## Issue Summary

- **Duration**:
  - Start: 18-08-2024, 9:00 AM WAT
  - End: 20-08-2024, 4:00 PM WAT

- **Impact**: Our web server decided to take an unscheduled break, thanks to a Nginx configuration mishap. The load balancer tried to keep the party going, but without web-02 in the mix, web-01 was left to do all the heavy lifting—poor thing. This led to some serious sluggishness, affecting around 60% of our users, who found themselves waiting longer than usual for their content. Turns out, our users have been hitting that refresh button a lot lately, making this hiccup even more noticeable. The root cause? A well-intentioned human with a bit too much power (i.e., root access) and a penchant for wildcards accidentally wiped out the Nginx configuration file.

## Timeline

- **08:00 AM WAT, 18th August 2024:** The issue was detected. Nginx was apparently MIA.

- **09:00 AM WAT:** Our monitoring system threw up a red flag—requests to web-02 had plummeted, while web-01 was suddenly the star of the show.

- **10:00 AM WAT:** Initial efforts focused on coaxing web-02 back into action. But after some poking and prodding, it was clear that something deeper was wrong.

- **11:00 AM WAT:** A light bulb moment—someone noticed the Nginx configuration file on web-02 was conspicuously absent. Whoops.

- **12:00 PM WAT:** The DevOps team swung into action, copying the configuration from web-01 to web-02. Some manual tinkering was required because, as we know, no two servers are exactly alike.

- **04:00 PM WAT, 20th August 2024:** After some fine-tuning and a few crossed fingers, the system was back to its usual self, and Nginx was off probation.

## Root Cause and Resolution

- **Root Cause**: This one’s on us—a classic case of “I thought I was just cleaning up.” An engineer, armed with root access and a wildcard, meant to delete an old backup but ended up taking out the main Nginx configuration file instead. Lesson learned: wildcards can be wild.

- **Resolution**: The DevOps team quickly came to the rescue, copying the Nginx configuration from web-01 to web-02. Some tweaks were necessary to account for the differences between the servers, but once those were sorted out, the issue was resolved.

## Corrective and Preventative Measures

- **Backup Strategy**: We’ll be sending our Nginx configuration files on a permanent vacation to Google Cloud, where they can relax and stay safe. Automated backups will make sure they’re always ready for a quick return if needed.
- **Access Control**: From now on, root access is on a strict “need-to-know” basis. Engineers will mostly be working with non-privileged accounts to avoid any more accidental config deletions.
- **Nginx Optimization**: We’re giving Nginx a boost by increasing the number of worker processes, ensuring it can handle all those eager requests without breaking a sweat.
- **Action Items**:
  - Automate the backup of Nginx configurations to Google Cloud.
  - Configure Nginx to increase the number of worker processes to enhance performance.
