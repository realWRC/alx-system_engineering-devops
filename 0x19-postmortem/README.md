# Post Mortem Report for Site Outage

**Date:** 13th August 2024  
**Time:** 21:00hrs

## Overview
On the 13th of August 2024, at approximately 21:00hrs, our website experienced a significant outage, resulting in a "500 Internal Server Error" for all users attempting to access the site. The issue stemmed from a misconfiguration within the `wp-settings.php` file, leading to the premature termination of the Apache service. Our servers are configured using the LAMP stack, powered by PHP 5.
