app_name = "ripperden_customization"
app_title = "Ripperden Customization"
app_publisher = "sandip@unifyxperts.com"
app_description = "A custom app for ERPNext Customizations"
app_email = "sandip@unifyxperts.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ripperden_customization",
# 		"logo": "/assets/ripperden_customization/logo.png",
# 		"title": "Ripperden Customization",
# 		"route": "/ripperden_customization",
# 		"has_permission": "ripperden_customization.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ripperden_customization/css/ripperden_customization.css"
# app_include_js = "/assets/ripperden_customization/js/ripperden_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/ripperden_customization/css/ripperden_customization.css"
# web_include_js = "/assets/ripperden_customization/js/ripperden_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ripperden_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ripperden_customization/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ripperden_customization.utils.jinja_methods",
# 	"filters": "ripperden_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ripperden_customization.install.before_install"
# after_install = "ripperden_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ripperden_customization.uninstall.before_uninstall"
# after_uninstall = "ripperden_customization.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ripperden_customization.utils.before_app_install"
# after_app_install = "ripperden_customization.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ripperden_customization.utils.before_app_uninstall"
# after_app_uninstall = "ripperden_customization.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ripperden_customization.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Stock Entry": {
		"on_update": "ripperden_customization.ripperden_customization.api.api.calculate_and_add_running_time"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ripperden_customization.tasks.all"
# 	],
# 	"daily": [
# 		"ripperden_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"ripperden_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ripperden_customization.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ripperden_customization.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ripperden_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ripperden_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ripperden_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ripperden_customization.utils.before_request"]
# after_request = ["ripperden_customization.utils.after_request"]

# Job Events
# ----------
# before_job = ["ripperden_customization.utils.before_job"]
# after_job = ["ripperden_customization.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ripperden_customization.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

