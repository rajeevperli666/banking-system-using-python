class Admin:
    def __init__(self, first_name, last_name, address, username, password, full_rights=False, can_delete_customer=False):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.username = username
        self.password = password
        self.full_rights = full_rights  
        self.can_delete_customer = can_delete_customer  

    def update_admin_info(self, new_first_name=None, new_last_name=None, new_address=None):
        """Update admin's personal information"""
        if new_first_name:
            self.first_name = new_first_name
        if new_last_name:
            self.last_name = new_last_name
        if new_address:
            self.address = new_address

    def change_password(self, new_password):
        """Change admin password"""
        self.password = new_password

    def has_full_rights(self):
        return self.full_rights

    def can_delete_customer_account(self):
        return self.can_delete_customer

    def get_admin_details(self):
        """Return dictionary of admin details"""
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Address": self.address,
            "Username": self.username,
            "Full Rights": self.full_rights,
            "Can Delete Customers": self.can_delete_customer
        }
    
    # Getters and Setters
    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def has_full_rights(self):
        return self.full_rights

    def set_full_rights(self, full_rights):
        self.full_rights = full_rights

    def can_delete_customer_account(self):
        return self.can_delete_customer

    def set_can_delete_customer(self, can_delete_customer):
        self.can_delete_customer = can_delete_customer
