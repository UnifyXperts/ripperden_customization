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


import frappe
from datetime import datetime, timedelta

def delete_old_error_logs_job():
    try:
        rs = frappe.get_single("Ripperden Settings")

        if not rs.is_active:
            return

        days = int(rs.delete_logs_older_than or 0)

        if days <= 0:
            return

        cutoff_time = datetime.utcnow() - timedelta(days=days)

        frappe.db.sql("""
            DELETE FROM `tabError Log`
            WHERE creation < %s
        """, (cutoff_time,))

        frappe.db.commit()

        frappe.logger().info(f"Deleted logs older than {days} days")

    except Exception:
        frappe.log_error(frappe.get_traceback(), "Error Log Cleanup Failed")
