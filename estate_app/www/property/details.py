import frappe

def get_context(context):
    context.details = frappe.get_doc("Property",frappe.form_dict.docname)
    x = frappe.get_doc("Property",frappe.form_dict.docname)
    context.agent = frappe.get_doc("Agent",x.property_agent)
    return context