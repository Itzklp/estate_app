import frappe

@frappe.whitelist()
def checkPropertyTypes(property_type=None):
    if not property_type:
        return []

    return frappe.db.sql(
        """SELECT property_name, property_type FROM `tabProperty` WHERE property_type = %s""",
        (property_type,),
        as_dict=True
    )
