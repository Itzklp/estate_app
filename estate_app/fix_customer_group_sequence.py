# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe

def fix_customer_group_sequence():
    customer_groups = frappe.get_all("Customer", fields=["name", "customer_group"], order_by="customer_group, name")
    
    group_sequences = {}
    
    for customer in customer_groups:
        group_name = customer["customer_group"]
        
        if group_name not in group_sequences:
            group_sequences[group_name] = []
        
        group_sequences[group_name].append(customer["name"])
    
    for group_name, customers in group_sequences.items():
        expected_sequence = 1
        for customer_name in customers:
            expected_group_id = f"{group_name}-{expected_sequence}"
            frappe.db.set_value("Customer", customer_name, "custom_custom_customer_group_id", expected_group_id)
            expected_sequence += 1
    
    frappe.db.commit()
    frappe.logger().info("Customer group sequences have been checked and updated successfully.")
