import frappe

def get_context(context):
    # Fetch shops with status 'Available'
    context.available_shops = frappe.get_all(
        "Shop",
        filters={"status": "Available"},
        fields=["shop_number","shop_name", "tenant_name", "rent_amount","expiry_date", "area"]
    )
    for shop in context.available_shops:
        if shop.tenant_name:
            tenant_doc = frappe.get_doc("Tenant", shop.tenant_name)
            shop.tenant_real_name = tenant_doc.tenant_name  
   