app_name = "estate_app"
app_title = "Estate App"
app_publisher = "Kalp Dalsania"
app_description = "This is an Learning APp"
app_email = "kalpdalsania@gmail.com"
app_license = "gpl-3.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "estate_app",
# 		"logo": "/assets/estate_app/logo.png",
# 		"title": "Estate App",
# 		"route": "/estate_app",
# 		"has_permission": "estate_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/estate_app/css/estate_app.css"
# app_include_js = "/assets/estate_app/js/test.js"

# include js, css files in header of web template
# web_include_css = "/assets/estate_app/css/estate_app.css"
# web_include_js = "/assets/estate_app/js/test.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "estate_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"Task": "public/js/test.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"background_jobs" : "public/js/test.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {
    "Student" : "public/js/student_list.js",
    "Customer" : "public/js/customer_button.js",
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# sounds = [
#     {"name": "custom", "src": "/assets/app/sound/Task 2.mp4", "volume": 0.2}
# ]


# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "estate_app/public/icons.svg"

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

website_route_rules = [
    {'from_route':'/property/details/<docname>','to_route':'property/details'},
]

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "estate_app.utils.jinja_methods",
# 	"filters": "estate_app.utils.jinja_filters"
# }

# jenv = {
#     "methods": "estate_app.jinja.custom_methods.add_custom_jinja_methods_and_filters"
# }


# Installation
# ------------

before_install = "estate_app.install.before_install"
after_install = "estate_app.install.after_install"
# after_sync = "estate_app.install.after_sync"
after_migrate = "estate_app.migrate.after_migrate"
# Uninstallation
# ------------

before_uninstall = "estate_app.uninstall.before_uninstall"
after_uninstall = "estate_app.uninstall.after_uninstall"



override_email_send = "estate_app.email.send"
get_sender_details = "estate_app.email.get_sender_details"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "estate_app.utils.before_app_install"
# after_app_install = "estate_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "estate_app.utils.before_app_uninstall"
# after_app_uninstall = "estate_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "estate_app.notifications.get_notification_config"

# python module path

#extending Boot info
# extend_booti  nfo = "estate_app.boot.boot_session"


update_website_context = "estate_app.website.website_context"


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
	"Customer":{
        "before_save":"estate_app.customer.before_save",
    }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"corn":{
        "0 14 * * *":[
            "estate_app.fix_customer_group_sequence.fix_customer_group_sequence"
        ]
    }
}

# Testing
# -------

# before_tests = "estate_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "estate_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "estate_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["estate_app.utils.before_request"]
# after_request = ["estate_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["estate_app.utils.before_job"]
# after_job = ["estate_app.utils.after_job"]

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
# 	"estate_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# fixtures = [
#     "Agent",
#     "Property",
#     "Amenity Name",
#     "Property Type",
#     "Property Amenity Details"
# ]