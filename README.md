# vrm-flask-ui

Frontend–Backend Route Map & API Priority

This document provides a single source of truth for frontend routes, reusable UI components, and API priorities so backend teams know what to build first.

Login page : http://127.0.0.1:5000/login
Purpose: User Authentication
Priority: High
Dashboard Page: http://127.0.0.1:5000/dashboard
purpose:KPIs, counts, alerts
Priority: High
Review : http://127.0.0.1:5000/reviews
purpose: Assessments waiting for review Priority: High
Remediation: http://127.0.0.1:5000/remediations
http://127.0.0.1:5000/remediation/1
http://127.0.0.1:5000/remediation/2
http://127.0.0.1:5000/remediation/1/response
http://127.0.0.1:5000/remediation/2/response
Purpose: open remediation item
Priority: Medium
Renewal: http://127.0.0.1:5000/renewals
Purpose: Upcoming and overdue renewals
Priority: Medium 
reports: http://127.0.0.1:5000/reports
Purpose: Export reports
Priority: Low 
assessments: http://127.0.0.1:5000/assessments
http://127.0.0.1:5000/assessments/1
http://127.0.0.1:5000/assessments/2
http://127.0.0.1:5000/assessments/3
templates: http://127.0.0.1:5000/templates/create

2. Reusable UI Components

Component       	Used On            	    Backend Dependency

Sidebar       	All pages                	Role-based access
Topbar	        All pages                 	Logged-in user info
Global          Search	Header	           Search API
Status Badges    All lists              	 Standard status values
Data Tables       Lists	                    Pagination & sorting
Empty State	      All lists                	Empty response handling
Action Buttons	   Lists                	  ID-based routes


3. Standard Status Values (Exact)

Backend must return only these values (case & spacing must match):

Assigned

In Progress

Submitted

Under Review

Remediation

Approved

Rejected


> Frontend badge colors depend on these exact strings



