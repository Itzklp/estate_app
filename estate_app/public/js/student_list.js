frappe.listview_settings['Student'] = {
    add_fields: ["stu_status"],
    get_indicator: function(doc) {
        if (doc.stu_status === "Excellent") {
            return [__("Excellent"), "green", "stu_status,=,Excellent"];
        } else if (doc.stu_status === "Failed" || doc.stu_status === "Fail") {
            return [__("Fail"), "red", "stu_status,=,Fail"];
        } else if (doc.stu_status === "Pass") {
            return [__("Pass"), "yellow", "stu_status,=,Pass"];
        }
    }
};
