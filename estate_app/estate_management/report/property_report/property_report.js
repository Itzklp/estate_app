// Copyright (c) 2025, Kalp Dalsania and contributors
// For license information, please see license.txt

frappe.query_reports["Property Report"] = {
    "filters": [
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": ["Sale","Rent","Lease"],
            "default": ""
        },
        {
            "fieldname": "property_type",
            "label": "Property Type",
            "fieldtype": "Link",
            "options": "Property Type"
        },
        {
            "fieldname": "property_agent",
            "label": "Property Agent",
            "fieldtype": "Link",
            "options": "Agent"
        },
        {
            "fieldname": "min_price",
            "label": "Min Price",
            "fieldtype": "Currency"
        },
        {
            "fieldname": "max_price",
            "label": "Max Price",
            "fieldtype": "Currency"
        }
    ]
};
