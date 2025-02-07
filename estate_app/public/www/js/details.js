document.querySelector("#contact-agent").addEventListener('click',
    ()=>{
        let email = document.querySelector("#email").value
        let name = document.querySelector("#name").value
        let property = document.querySelector("#property-name").textContent

        let d = new frappe.ui.Dialog({
            title: 'Enter details',
            fields: [
                {
                    label: 'First Name',
                    fieldname: 'first_name',
                    fieldtype: 'Data'
                },
                {
                    label: 'Last Name',
                    fieldname: 'last_name',
                    fieldtype: 'Data'
                },
                {
                    label: 'Message',
                    fieldname: 'msg',
                    fieldtype: 'Small Text'
                }
            ],
            size: 'small', 
            primary_action_label: 'Submit',
            primary_action(values) {
                values.agent_email = email;
                values.property = property
                console.log(values);
                frappe.call({
                    method:"estate_app.api.contactAgent",
                    args: values,
                    callback:function(r){
                        console.log(r);
                        frappe.msgprint({
                            title:__("Notification"),
                            indicator: 'green',
                            message: __(r.message)
                        });
                    }
                })
                d.hide();    
            }
        });
        
        d.show();
    })