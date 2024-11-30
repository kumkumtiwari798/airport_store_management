import frappe
# from frappe.core.doctype.communication.email import make

def update_shop_counts(doc, method):
    # Get the airport linked to the shop
    airport_name = doc.airport

    # Calculate total and occupied shops
    total_shop = frappe.db.count('Shop', filters={'airport': airport_name})
    occupied_shop = frappe.db.count('Shop', filters={'airport': airport_name, 'status': 'Occupied'})
    available_shop = frappe.db.count('Shop', filters={'airport': airport_name, 'status': 'Available'})

    # Update the total and occupied shop counts in the Airports doctype
    frappe.db.set_value('Airports shop Details', airport_name, 'total_shop', total_shop)
    frappe.db.set_value('Airports shop Details', airport_name, 'occupied_shop', occupied_shop)
    frappe.db.set_value('Airports shop Details', airport_name, 'available_shop', available_shop)

# In airport_store_management/api.py

# import frappe
# def print_every_minute():
#     print("The minute-based event is triggered. This will print every minute.")

# def send_rent_reminder_if_enabled():
#     # Print message to the console to confirm the event is working
#     print("Scheduled event 'send_rent_reminder_if_enabled' is running...")

#     # Fetch global configurations from Rent Settings
#     default_rent_amount = frappe.db.get_single_value('Rent Settings', 'rent_amount')
#     enable_rent_reminders = frappe.db.get_single_value('Rent Settings', 'rent_reminders')

#     # Check if rent reminders are enabled
#     if enable_rent_reminders:
#         send_rent_reminders_to_tenants(default_rent_amount)

# def send_rent_reminders_to_tenants(rent_amount):
#     # Get list of tenants (assuming tenants are stored in a Tenant Doctype)
#     tenants = frappe.get_all('Tenant', filters={'is_active': 1}, fields=['name', 'email'])

#     for tenant in tenants:
#         # Construct the email content
#         subject = "Rent Reminder"
#         message = f"Dear {tenant['name']},<br>Your rent of {rent_amount} is due this month. Please ensure timely payment to avoid penalties."

#         # Send email
#         make(
#             recipients=[tenant['email']],
#             subject=subject,
#             content=message,
#             send_email=True
#         )

#         # Print confirmation for each email sent
#         print(f"Sent rent reminder to {tenant['name']} at {tenant['email']}.")

# import frappe

# def send_mail():
#     recipients = [
#         'puran@navgurukul.org',
#         'kumkumtiwari23@navgurukul.org'
#     ]

#     frappe.sendmail(
#         recipients=recipients,
#         subject=frappe._('Birthday Reminder'),
#         template='birthday_reminder',
#         args=dict(
#             reminder_text="Happy Birthday",
#             birthday_persons="Kumkum",
#             message="God Bless You",
#         ),
#         header=('Birthday Reminder 🎂')
#     )
