import frappe

def paginate(doctype, page=1, condition=""):
    page = int(page) if str(page).isdigit() else 1
    prev, next = 0, 0
    query = f"""SELECT * FROM `tab{doctype}` {condition}"""

    offset = max((page - 1) * 4, 0)

    properties = frappe.db.sql(query + f" LIMIT {offset}, 4;", as_dict=True)
    
    next_set = frappe.db.sql(query + f" LIMIT {offset + 4}, 4;", as_dict=True)

    if next_set:
        prev, next = page - 1, page + 1
    else:
        prev, next = page - 1, 0

    return {
        'properties': properties,
        'prev': prev,
        'next': next,
        'search': bool(condition.strip()) 
    }

def get_context(context):
    filters = []
    
    property_type = frappe.form_dict.get("property_type")
    city = frappe.form_dict.get("city")
    status = frappe.form_dict.get("status")
    page = frappe.form_dict.get("page", 1)

    page = int(page) if str(page).isdigit() else 1

    if property_type:
        filters.append(f"property_type = '{property_type}'")
    if city:
        filters.append(f"city = '{city}'")
    if status:
        filters.append(f"status = '{status}'")

    condition = f"WHERE {' AND '.join(filters)}" if filters else ""
    pagination = paginate("Property", page, condition)

    context.properties = pagination.get('properties', [])
    context.prev = pagination.get('prev', 0)
    context.next = pagination.get('next', 0)
    context.search = pagination.get('search', False)

    return context
