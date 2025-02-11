frappe.listview_settings['Customer'] = {
    onload(listview){
        listview.page.add_inner_button(__('Click Me'), function() {
            frappe.msgprint(__('I Am Clicked'));
        }, "Custom Button"); 
    }
}