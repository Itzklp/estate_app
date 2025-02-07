# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from estate_app.send_welcome import sendmail

class Property(Document):
    def validate(self):
        if self.property_type == 'Apartment':
            for i in self.amenity_list:
                if i.amenity_name == "outdoor kitchen":
                    frappe.throw(f"The Property Type {self.property_type} Cannot Contain Amenity Named {i.amenity_name}")
        
        if self.property_price and self.discount > 0:
            self.grand_total = self.property_price - (self.property_price * (self.discount / 100))
            self.grand_total_gst = self.grand_total + (self.grand_total * 0.18) 
        else:
            self.grand_total = self.property_price

    def after_insert(self):
        if self.property_agent: 
            agent_doc = frappe.get_doc("Agent", self.property_agent)
            agent_email = agent_doc.email  

            if agent_email:
                msg = f"""
                    Hello {agent_doc.agent_name},<br><br>
                    A new property has been added on your behalf. Below are the details:<br>
                    - Property Name: {self.property_name}<br>
                    - Property Type: {self.property_type}<br>
                    - Property Status: {self.status}<br>
                    - Property Price: &#8377;{self.property_price}<br>
                    - Property Discount: {self.discount}<br>
                    - Grand Total: &#8377;{self.grand_total}<br><br>
                    Thank you for using our services!<br><br>
                    Best regards,<br>
                    Your Estate Team
                """
                sendmail(self, [agent_email], msg, 'New Property Added', None)
            else:
                frappe.throw("The agent does not have an email address set.")
        else:
            frappe.throw("No agent is linked to this property.")