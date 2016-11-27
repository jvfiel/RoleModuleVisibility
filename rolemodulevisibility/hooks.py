# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rolemodulevisibility"
app_title = "Role Module Visibility"
app_publisher = "Bai Web and Mobile Lab"
app_description = "Hide/Unhide desktop icons per Role or Globally"
app_icon = "octicon-tools"
app_color = "white"
app_email = "happy@bai.ph"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rolemodulevisibility/css/rolemodulevisibility.css"
# app_include_js = "/assets/rolemodulevisibility/js/rolemodulevisibility.js"

# include js, css files in header of web template
# web_include_css = "/assets/rolemodulevisibility/css/rolemodulevisibility.css"
# web_include_js = "/assets/rolemodulevisibility/js/rolemodulevisibility.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rolemodulevisibility.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rolemodulevisibility.install.before_install"
# after_install = "rolemodulevisibility.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rolemodulevisibility.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rolemodulevisibility.tasks.all"
# 	],
# 	"daily": [
# 		"rolemodulevisibility.tasks.daily"
# 	],
# 	"hourly": [
# 		"rolemodulevisibility.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rolemodulevisibility.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rolemodulevisibility.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rolemodulevisibility.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rolemodulevisibility.event.get_events"
# }

