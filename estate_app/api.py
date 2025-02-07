import frappe

from send_welcome import  sendmail


@frappe.whitelist()
def contactAgent(**args):
    doc = frappe.get_doc("Property",args.get("property"))
    msg = f"{args.get('first_name')}<br>{args.get('last_name')}<br>{args.get('message')}"
    sendmail(doc, args.get("agent_email"), msg, "Property Inquiry", attachments=None)

    return "Message sent to agent, They will responce to the earliest."