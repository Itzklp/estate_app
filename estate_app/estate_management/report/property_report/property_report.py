# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = getColumns()
    data = getData(filters)
    return columns, data

def getColumns():
    return [
        {
            "label": "Property Name",
            "fieldname": "property_name", 
            "fieldtype": "Data", 
            "width": 200
        },
        {
            "label": "Property Type", 
            "fieldname": "property_type", 
            "fieldtype": "Link", "options": 
            "Property Type", 
            "width": 150
        },
        {
            "label": "Property Address", 
            "fieldname": "property_address", 
            "fieldtype": "Data", 
            "width": 250
        },
        {
            "label": "Status", 
            "fieldname": "status", 
            "fieldtype": "Select", 
            "width": 120
        },
        {
            "label": "Property Description", 
            "fieldname": "property_description", 
            "fieldtype": "Small Text", 
            "width": 300
        },
        {
            "label": "Property Agent", 
            "fieldname": "property_agent", 
            "fieldtype": "Link", "options": "Agent", 
            "width": 150
        },
        {
            "label": "Property Price", 
            "fieldname": "property_price", 
            "fieldtype": "Currency", 
            "width": 150
        },
        {
            "label": "Discount (%)", 
            "fieldname": "discount", 
            "fieldtype": "Percent", 
            "width": 100
        },
        {
            "label": "Grand Total", 
            "fieldname": "grand_total", 
            "fieldtype": "Float", 
            "width": 150
        },
        {
            "label": "Grand Total with GST", 
            "fieldname": "grand_total_gst", 
            "fieldtype": "Float", 
            "width": 150
        },
    ]

def getData(filters):
    conditions = {}
    if filters:
        if filters.get("status"):
            conditions["status"] = filters.get("status")
        if filters.get("property_type"):
            conditions["property_type"] = filters.get("property_type")
        if filters.get("property_agent"):
            conditions["property_agent"] = filters.get("property_agent")
        if filters.get("min_price"):
            conditions["property_price"] = [">=", filters.get("min_price")]
        if filters.get("max_price"):
            conditions["property_price"] = ["<=", filters.get("max_price")]
    
    data = frappe.get_all(
        "Property",
        filters=conditions,
        fields=[
            "property_name", "property_type", "property_address", "status",
            "property_description", "property_agent", "property_price", "discount",
            "grand_total", "grand_total_gst"
        ],
    )
    return data
