import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {"label": "Printer (Workstation)", "fieldname": "printer", "fieldtype": "Data", "width": 200},
        {"label": "Work Order", "fieldname": "work_order", "fieldtype": "Link", "options": "Work Order", "width": 180},
        {"label": "Printing Time", "fieldname": "printing_time", "fieldtype": "Float", "width": 150},
    ]


def get_data(filters):
    conditions = ""

    if filters.get("printer"):
        conditions += " AND custom_printer = %(printer)s"

    query = f"""
        SELECT 
            name AS work_order,
            custom_printer AS printer,
            custom_printing_time_in_hours_per_unit_stock_uom AS printing_time
        FROM `tabWork Order`
        WHERE docstatus < 2 {conditions}
        ORDER BY custom_printer, name
    """

    results = frappe.db.sql(query, filters, as_dict=True)

    # 🔥 GROUPING (Printer → WO → Total)
    grouped = {}
    for row in results:
        grouped.setdefault(row.printer or "No Printer", []).append(row)

    final_data = []

    for printer, rows in grouped.items():
        total = 0
        
        
        for r in rows:
            total += r.printing_time or 0

        final_data.append({
            "printer": printer,
            "work_order": "",
            "printing_time": total
        })

        # WO rows
        for r in rows:
            final_data.append({
                "printer": "",
                "work_order": r.work_order,
                "printing_time": r.printing_time
            })
            total += r.printing_time or 0



    return final_data