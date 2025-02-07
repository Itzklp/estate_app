// Copyright (c) 2025, Kalp Dalsania and contributors
// For license information, please see license.txt

frappe.ui.form.on("Property", {
    refresh(frm) {
        if (!frm.custom_add_address_button_added) {
            frm.add_custom_button("Add Address", () => {
                frappe.prompt("Address", (values) => {
                    console.log("Inside prompt", values);
                    if (values) { 
                        frm.set_value("property_address", values.value);
                        frm.refresh_field("property_address");
                    }
                });
            },"Actions");
            frm.add_custom_button("Find Property Types", () => {
                let x = frm.doc.property_type;
                frappe.call({
                    method: "estate_app.estate_management.doctype.property.api.checkPropertyTypes",
                    args: { 'property_type': x },
                    callback: function(r) {
                        console.log(r.message);
                        if (r.message && r.message.length > 0) {
                            let properties = r.message;
                            let formattedData = '<table border="1" style="border-collapse: collapse;">';
                            formattedData += '<tr><th>Property Name</th><th>Property Type</th></tr>';
            
                            properties.forEach(function(property) {
                                formattedData += `<tr><td>${property.property_name}</td><td>${property.property_type}</td></tr>`;
                            });
            
                            formattedData += '</table>';
                            frappe.msgprint({
                                title: 'Property Types',
                                message: formattedData,
                                indicator: 'green'
                            });
                        } else {
                            frappe.msgprint({
                                title: 'No Properties Found',
                                message: 'No properties of this type were found.',
                                indicator: 'yellow'
                            });
                        }
                    }
                });
            }, "Actions");             
        }
    }
});

frappe.ui.form.on("amenity_list", {
    amenity_name(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        check_amenities_duplicate(frm, row, cdt, cdn);
    }
});

function check_amenities_duplicate(frm, row, cdt, cdn) {
    let duplicate = false;

    frm.doc.amenity_list.forEach(item => {
        if (item.amenity_name && row.idx !== item.idx && row.amenity_name === item.amenity_name) {
            duplicate = true;
        }
    });

    if (duplicate) {
        frm.set_value(cdt, cdn, "amenity_name", "");
        frappe.throw("Duplicate amenities not allowed");
    }
}
