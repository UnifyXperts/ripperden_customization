import frappe

def calculate_and_add_running_time(doc, method=None):

    if doc.docstatus != 1:
        return

    if not doc.work_order:
        return

    work_order = frappe.get_doc("Work Order", doc.work_order)

    printing_time = work_order.custom_printing_time_in_hours_per_unit_stock_uom or 0

    if not work_order.custom_printer:
        return

    current_time = frappe.db.get_value(
        "Workstation",
        work_order.custom_printer,
        "custom_total_running_time"
    ) or 0

    # Update running time
    frappe.db.set_value(
        "Workstation",
        work_order.custom_printer,
        "custom_total_running_time",
        current_time + printing_time
    )

    frappe.msgprint(
        f"Running time updated for Workstation {work_order.custom_printer}"
    )
