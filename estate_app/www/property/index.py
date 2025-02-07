import frappe

def paginate(doctype, page=1, condition=""):
    """Fetch paginated records from the given doctype with optional filtering."""
    page = int(page) if str(page).isdigit() else 1  # Ensure page is always an integer
    prev, next = 0, 0
    query = f"""SELECT * FROM `tab{doctype}` {condition}"""
    
    # Calculate offset for pagination
    offset = max((page - 1) * 4, 0)
    
    # Fetch the current page records
    properties = frappe.db.sql(query + f" LIMIT {offset}, 4;", as_dict=True)
    
    # Check if more records exist for next page
    next_set = frappe.db.sql(query + f" LIMIT {offset + 4}, 4;", as_dict=True)

    if next_set:
        prev, next = page - 1, page + 1
    else:
        prev, next = page - 1, 0

    return {
        'properties': properties,
        'prev': prev,
        'next': next,
        'search': bool(condition.strip())  # True if condition exists
    }

def get_context(context):
    """Prepare context for rendering the property listing page with pagination and filtering."""
    filters = []
    
    # Retrieve filters safely from form_dict
    property_type = frappe.form_dict.get("property_type")
    city = frappe.form_dict.get("city")
    status = frappe.form_dict.get("status")
    page = frappe.form_dict.get("page", 1)

    # Ensure valid integer for page number
    page = int(page) if str(page).isdigit() else 1

    # Build SQL conditions dynamically
    if property_type:
        filters.append(f"property_type = '{property_type}'")
    if city:
        filters.append(f"city = '{city}'")
    if status:
        filters.append(f"status = '{status}'")

    # Combine conditions into a WHERE clause
    condition = f"WHERE {' AND '.join(filters)}" if filters else ""

    # Call pagination function
    pagination = paginate("Property", page, condition)

    # Set context variables
    context.properties = pagination.get('properties', [])
    context.prev = pagination.get('prev', 0)
    context.next = pagination.get('next', 0)
    context.search = pagination.get('search', False)

    return context
