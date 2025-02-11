import frappe

def before_save(doc, method):
    if doc.customer_primary_address:
        frappe.msgprint("Customer details updated as primary address is selected!", alert=True)