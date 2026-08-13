import frappe


def execute():
    field_order = [
        "details",
        "naming_series",
        "item_code",
        "item_name",
        "item_group",
        "stock_uom",
        "brand",
        "custom_amazon_fulfillment_sku",
        "column_break0",
        "disabled",
        "allow_alternative_item",
        "is_stock_item",
        "has_variants",
        "column_break_kpmi",
        "opening_stock",
        "custom_weight_",
        "column_break_ixrh",
        "valuation_rate",
        "standard_rate",
        "custom_section_break_34raw",
        "custom_packing_box_details",
        "section_break_znra",
        "is_fixed_asset",
        "auto_create_assets",
        "is_grouped_asset",
        "asset_category",
        "asset_naming_series",
        "section_break_gjns",
        "over_delivery_receipt_allowance",
        "column_break_wugd",
        "over_billing_allowance",
        "image",
        "section_break_11",
        "description",
        "dashboard_tab",
        "inventory_section",
        "stock_levels_section",
        "stock_levels_html",
        "inventory_settings_section",
        "shelf_life_in_days",
        "end_of_life",
        "default_material_request_type",
        "valuation_method",
        "column_break_cqdk",
        "column_break1",
        "warranty_period",
        "weight_per_unit",
        "weight_uom",
        "allow_negative_stock",
        "sb_barcodes",
        "barcodes",
        "reorder_section",
        "reorder_levels",
        "serial_nos_and_batches",
        "has_batch_no",
        "create_new_batch",
        "batch_number_series",
        "has_expiry_date",
        "retain_sample",
        "sample_quantity",
        "column_break_37",
        "has_serial_no",
        "serial_no_series",

        # WooCommerce
        "custom_woocommerce_tab",
        "woocommerce_servers",

        "variants_section",
        "variant_of",
        "variant_based_on",
        "attributes",

        # Accounting tab
        "accounting",
        "section_break_wfkx",
        "item_defaults",
        "deferred_accounting_section",
        "enable_deferred_expense",
        "no_of_months_exp",
        "column_break_9s9o",
        "enable_deferred_revenue",
        "no_of_months",

        # UOM tab
        "uom_tab",
        "unit_of_measure_conversion",
        "uom_conversion_details_column",
        "uom_help_html",
        "uoms",

        # Purchasing
        "purchasing_tab",
        "purchase_uom",
        "min_order_qty",
        "safety_stock",
        "is_purchase_item",
        "purchase_details_cb",
        "lead_time_days",
        "last_purchase_rate",
        "is_customer_provided_item",
        "supplier_details",
        "delivered_by_supplier",
        "section_break_ylma",
        "supplier_items",

        # Foreign Trade
        "foreign_trade_details",
        "country_of_origin",
        "column_break_59",
        "customs_tariff_number",

        # Sales
        "sales_details",
        "sales_uom",
        "grant_commission",
        "is_sales_item",
        "column_break3",
        "max_discount",
        "customer_details",
        "customer_items",

        # Taxes
        "item_tax_section_break",
        "section_break_oilf",
        "column_break_aytr",
        "taxes",
        "section_break_fxqz",
        "purchase_tax_withholding_category",
        "column_break_ltlb",
        "sales_tax_withholding_category",

        # Quality
        "quality_tab",
        "inspection_required_before_purchase",
        "quality_inspection_template",

        # Pricing
        "pricing_tab",
        "item_prices_column",
        "column_break_pxjh",
        "prices_html",
        "inspection_required_before_delivery",

        # Manufacturing
        "manufacturing",
        "include_item_in_manufacturing",
        "is_sub_contracted_item",
        "default_bom",
        "column_break_74",
        "production_capacity",
        "customer_code",
        "column_break_vipt",
        "default_item_manufacturer",
        "default_manufacturer_part_no",
        "total_projected_qty",
    ]

    value = frappe.as_json(field_order)

    if frappe.db.exists("Property Setter", "Item-main-field_order"):
        frappe.db.set_value(
            "Property Setter",
            "Item-main-field_order",
            "value",
            value,
            update_modified=False,
        )
    else:
        frappe.get_doc({
            "doctype": "Property Setter",
            "doctype_or_field": "DocType",
            "doc_type": "Item",
            "property": "field_order",
            "property_type": "Data",
            "value": value,
        }).insert(ignore_permissions=True)

    frappe.clear_cache(doctype="Item")