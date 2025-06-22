import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox, simpledialog
from admin import Admin
from customer_account import CustomerAccount

class BankSystem:
    def __init__(self, root):
        self.root = root
        self.accounts = []
        self.admins = []
        self.load_data()
        self.logged_in_admin = None
        self.customer_bg = tk.PhotoImage(file="customer_bg.png")  # Initialize customer background
        self.staff_bg = tk.PhotoImage(file="staff_bg.png")  # Initialize staff background
        self.create_home_screen()

    def load_data(self):
        account_no = 1234
        # Creating sample customer accounts
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00, account_type="Current", interest_rate=0.02, overdraft_limit=500)
        self.accounts.append(customer_1)

        account_no += 1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00, account_type="Saving", interest_rate=0.03, overdraft_limit=1000)
        self.accounts.append(customer_2)

        account_no += 1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00, account_type="Current", interest_rate=0.015, overdraft_limit=200)
        self.accounts.append(customer_3)

        account_no += 1
        customer_4 = CustomerAccount("Ali", "Abdallah", ["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00, account_type="Saving", interest_rate=0.05, overdraft_limit=1500)
        self.accounts.append(customer_4)

        account_no += 1
        customer_5 = CustomerAccount("Emma", "Johnson", ["23", "Baker Street", "London", "NW1 6XE"], account_no, 12500.00, account_type="Current", interest_rate=0.02, overdraft_limit=800)
        self.accounts.append(customer_5)

        account_no += 1
        customer_6 = CustomerAccount("Michael", "Brown", ["7", "Victoria Road", "Manchester", "M14 4PR"], account_no, 3500.00, account_type="Saving", interest_rate=0.04, overdraft_limit=1200)
        self.accounts.append(customer_6)

        account_no += 1
        customer_7 = CustomerAccount("Sophia", "Garcia", ["12", "Park Lane", "Leeds", "LS1 4DJ"], account_no, 8500.00, account_type="Current", interest_rate=0.015, overdraft_limit=600)
        self.accounts.append(customer_7)

        account_no += 1
        customer_8 = CustomerAccount("James", "Wilson", ["3", "High Street", "Bristol", "BS1 2AW"], account_no, 200.00, account_type="Saving", interest_rate=0.06, overdraft_limit=2000)
        self.accounts.append(customer_8)

        # Creating sample admin accounts
        admin_1 = Admin("Rajeev", "Perli", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True, True)
        self.admins.append(admin_1)

        admin_2 = Admin("Cathy", "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False, False)
        self.admins.append(admin_2)

    def create_home_screen(self):
        self.clear_screen()
        self.root.title("Quantum Hub Banking")
        
        # Background image
        self.bg_image = tk.PhotoImage(file="main_page.png")
        bg_label = tk.Label(self.root, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Header
        header_frame = tk.Frame(self.root, bg="#1a237e", height=100)
        header_frame.pack(fill="x", pady=(0, 20))
        tk.Label(header_frame, text="Quantum Banking Hub", 
                font=("Roboto", 28, "bold"), bg="#1a237e", fg="#ffffff").pack(pady=20)
        
        # Selection buttons
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=50)
        
        tk.Button(button_frame, text="Staff Portal", font=("Roboto", 16), 
                command=self.staff_portal_screen, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=15, padx=20)
                
        tk.Button(button_frame, text="Client Portal", font=("Roboto", 16), 
                command=self.client_portal_screen, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=15, padx=20)
                
        tk.Button(button_frame, text="Close Application", font=("Roboto", 16), 
                command=self.root.quit, bg="#c62828", fg="#ffffff", 
                activebackground="#d32f2f", width=20, bd=0).pack(pady=15, padx=20)

    def create_header(self, title):
        header_frame = tk.Frame(self.root, bg="#1a237e", height=100)
        header_frame.pack(fill="x", pady=(0, 20))
        
        # Using 'Segoe UI' which is a modern Windows system font
        tk.Label(header_frame, text=title, 
                font=("Segoe UI", 28, "bold"), 
                bg="#1a237e", fg="#ffffff").pack(pady=20)

    def staff_portal_screen(self):
        self.clear_screen()
        
        # Background image
        bg_label = tk.Label(self.root, image=self.staff_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("Staff login")
        
        login_frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        login_frame.pack(pady=30)
        
        tk.Label(login_frame, text="Access ID", font=("Roboto", 14), bg="#ffffff", fg="#1a237e").pack(pady=5)
        self.username_entry = tk.Entry(login_frame, font=("Roboto", 14), bd=2, relief=tk.GROOVE, bg="#f5f5f5", fg="#1a237e", insertbackground="#1a237e")
        self.username_entry.pack(pady=5, ipady=5, ipadx=10)

        tk.Label(login_frame, text="Security Key", font=("Roboto", 14), bg="#ffffff", fg="#1a237e").pack(pady=5)
        self.password_entry = tk.Entry(login_frame, show="*", font=("Roboto", 14), bd=2, relief=tk.GROOVE, bg="#f5f5f5", fg="#1a237e", insertbackground="#1a237e")
        self.password_entry.pack(pady=5, ipady=5, ipadx=10)
        
        button_frame = tk.Frame(login_frame, bg="#ffffff")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Authenticate", font=("Roboto", 14, "bold"), 
                command=self.verify_admin_login, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=15, bd=0, padx=10, pady=5).pack(side=tk.LEFT, padx=10)
                
        tk.Button(button_frame, text="Return", font=("Roboto", 14, "bold"), 
                command=self.create_home_screen, bg="#757575", fg="#ffffff", 
                activebackground="#9e9e9e", width=15, bd=0, padx=10, pady=5).pack(side=tk.LEFT, padx=10)

    def verify_admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        for admin in self.admins:
            if admin.get_username() == username and admin.get_password() == password:
                self.logged_in_admin = admin
                self.show_admin_dashboard()
                return
        
        messagebox.showerror("Login Failed", "Invalid credentials")
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.username_entry.focus_set()
        self.logged_in_admin = None  # Explicitly reset login state

    def show_admin_dashboard(self):
        self.clear_screen()
        
        # Background image
        bg_label = tk.Label(self.root, image=self.staff_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
        self.create_header(f"Quantum Admin Console: {self.logged_in_admin.get_first_name()} {self.logged_in_admin.get_last_name()}")
        
        # Main action buttons frame - single column layout
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=20)
        
        # Grouped operation buttons
        tk.Button(button_frame, text="Customer Operations", font=("Roboto", 14), 
                command=self.show_client_operations, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="Banking Services", font=("Roboto", 14), 
                command=self.show_bank_services, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="Edit Profile", font=("Roboto", 14), 
                command=self.edit_admin_profile_screen, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)

        # Sign out button
        tk.Button(button_frame, text="Sign Out", font=("Roboto", 14),
                command=self.logout_admin, bg="#c62828", fg="#ffffff",
                activebackground="#d32f2f", width=20, bd=0).pack(pady=20)

    def show_client_operations(self):
        self.clear_screen()
        
        # Background image
        bg_label = tk.Label(self.root, image=self.staff_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("Client Operations")
        
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Client Search", font=("Roboto", 14), 
                command=self.search_customer_screen, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="View Client Records", font=("Roboto", 14), 
                command=self.show_all_customers, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="Close Account", font=("Roboto", 14), 
                command=self.delete_customer_account_screen, bg="#c62828", fg="#ffffff", 
                activebackground="#d32f2f", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="Back to Dashboard", font=("Roboto", 14),
                command=self.show_admin_dashboard, bg="#757575", fg="#ffffff",
                activebackground="#9e9e9e", width=20, bd=0).pack(pady=20)

    def show_bank_services(self):
        self.clear_screen()
        
        # Background image
        bg_label = tk.Label(self.root, image=self.staff_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("Bank Services")
        
        button_frame = tk.Frame(self.root, bg="")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Funds Transfer", font=("Roboto", 14), 
                command=self.initiate_transfer_screen, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="Generate Analytics", font=("Roboto", 14), 
                command=self.generate_report_screen, bg="#3949ab", fg="#ffffff", 
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="Back to Dashboard", font=("Roboto", 14),
                command=self.show_admin_dashboard, bg="#757575", fg="#ffffff",
                activebackground="#9e9e9e", width=20, bd=0).pack(pady=20)

    def logout_admin(self):
        self.logged_in_admin = None
        self.create_home_screen()

    def logout_customer(self):
        self.logged_in_customer = None
        self.create_home_screen()

    # CUSTOMER FUNCTIONS
    def client_portal_screen(self):
        self.clear_screen()
        self.root.title("Customer Login")
        
        # Background image
        self.bg_image = tk.PhotoImage(file="main_page.png")
        bg_label = tk.Label(self.root, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        main_frame = tk.Frame(self.root, bg="")
        main_frame.configure(bg="")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_frame = tk.Frame(main_frame, bg="#1a237e", height=80)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        tk.Label(header_frame, text="Customer Login", 
                font=("Roboto", 20, "bold"), bg="#1a237e", fg="#ffffff").pack(pady=20)
        
        # Login form
        form_frame = tk.Frame(main_frame, bg="#ffffff", padx=20, pady=20)
        form_frame.pack()
        
        tk.Label(form_frame, text="Account Number:", 
                font=("Roboto", 14), bg="#ffffff", fg="#1a237e").grid(row=0, column=0, sticky="e", pady=10)
        self.cust_account_no_entry = tk.Entry(form_frame, font=("Roboto", 14), bg="#ffffff", fg="#1a237e", insertbackground="#1a237e")
        self.cust_account_no_entry.grid(row=0, column=1, pady=10, padx=10)
        
        tk.Label(form_frame, text="Password:", 
                font=("Roboto", 14), bg="#ffffff", fg="#1a237e").grid(row=1, column=0, sticky="e", pady=10)
        self.cust_password_entry = tk.Entry(form_frame, show="*", font=("Roboto", 14), bg="#ffffff", fg="#1a237e", insertbackground="#1a237e")
        self.cust_password_entry.grid(row=1, column=1, pady=10, padx=10)
        
        button_frame = tk.Frame(main_frame, bg="", padx=20, pady=20)
        button_frame.pack()
        
        tk.Button(button_frame, text="Login", font=("Roboto", 14, "bold"),
                command=self.verify_client_login, bg="#3949ab", fg="#ffffff",
                activebackground="#5c6bc0", width=15, bd=0, padx=10, pady=5).pack(pady=10)
                
        tk.Button(button_frame, text="Back", font=("Roboto", 14, "bold"),
                command=self.create_home_screen, bg="#757575", fg="#ffffff",
                activebackground="#9e9e9e", width=15, bd=0, padx=10, pady=5).pack(pady=10)

    def verify_client_login(self):
        account_no = self.cust_account_no_entry.get()
        password = self.cust_password_entry.get()
        
        try:
            account_no = int(account_no)
            for customer in self.accounts:
                if customer.get_account_no() == account_no:
                    # Check if password matches the default "key123"
                    if password == "key123":
                        self.logged_in_customer = customer
                        self.show_customer_dashboard()
                        return
                    else:
                        messagebox.showerror("Login Failed", "Incorrect password")
                        return
        except ValueError:
            pass
            
        messagebox.showerror("Login Failed", "Invalid account number or password")
        self.cust_account_no_entry.delete(0, tk.END)
        self.cust_password_entry.delete(0, tk.END)
        self.cust_account_no_entry.focus_set()

    def show_fund_operations(self):
        """Show the fund operations menu for customers"""
        self.clear_screen()
        
        # Background image
        bg_label = tk.Label(self.root, image=self.customer_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("Fund Operations")
        
        button_frame = tk.Frame(self.root, bg="", padx=20, pady=20)
        button_frame.pack(fill=tk.X)
        
        tk.Button(button_frame, text="Deposit", font=("Roboto", 14),
                command=self.customer_deposit, bg="#3949ab", fg="#ffffff",
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="Withdraw", font=("Roboto", 14),
                command=self.customer_withdraw, bg="#3949ab", fg="#ffffff",
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="View Balance", font=("Roboto", 14),
                command=self.customer_show_balance, bg="#3949ab", fg="#ffffff",
                activebackground="#5c6bc0", width=20, bd=0).pack(pady=10)
                
        # Add back button at bottom of screen
        back_frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        back_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        tk.Button(back_frame, text="Back to Dashboard", font=("Roboto", 14),
                command=self.show_customer_dashboard, bg="#757575", fg="#ffffff",
                activebackground="#9e9e9e", width=20, bd=0).pack(pady=20)

    def show_customer_dashboard(self, customer=None):
        self.clear_screen()
        if customer:
            self.logged_in_customer = customer
        self.root.title(f"Customer Account - {self.logged_in_customer.get_full_name()}")
        
        # Background image
        self.customer_bg = tk.PhotoImage(file="customer_bg.png")
        bg_label = tk.Label(self.root, image=self.customer_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Header
        header_frame = tk.Frame(self.root, bg="#1a237e", height=80)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        tk.Label(header_frame, text=f"Quantum Client Portal - {self.logged_in_customer.get_full_name()}", 
                font=("Segoe UI", 20, "bold"), bg="#1a237e", fg="#ffffff").pack(pady=20)
        
        # Account info - centered in window
        info_frame = tk.Frame(self.root, bg="#ffffff")
        info_frame.pack(fill=tk.BOTH, expand=True)
        
        # Center container frame
        center_container = tk.Frame(info_frame, bg="#ffffff")
        center_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        tk.Label(center_container, text=f"Account Number: {self.logged_in_customer.get_account_no()}",
                font=("Roboto", 14), bg="#ffffff", fg="#1a237e", justify="center").pack(pady=5, fill="x")
                
        tk.Label(center_container, text=f"Balance: £{self.logged_in_customer.get_balance():.2f}",
                font=("Roboto", 14), bg="#ffffff", fg="#1a237e", justify="center").pack(pady=5, fill="x")
                
        tk.Label(center_container, text=f"Account Type: {self.logged_in_customer.get_account_type()}",
                font=("Roboto", 14), bg="#ffffff", fg="#1a237e", justify="center").pack(pady=5, fill="x")
        
        # Action buttons grouped into categories
        button_frame = tk.Frame(self.root, bg="", padx=20, pady=20)
        button_frame.pack(fill=tk.X)

        # Fund Operations button
        tk.Button(button_frame, text="Fund Operations", font=("Roboto", 14),
                command=self.show_fund_operations, bg="", fg="#ffffff",
                activebackground="#5c6bc0", highlightbackground="#3949ab",
                width=20, bd=0, relief=tk.FLAT).pack(pady=10)
        
        # Self Details button        
        tk.Button(button_frame, text="Self Details", font=("Roboto", 14),
                command=self.show_self_details, bg="", fg="#ffffff",
                activebackground="#5c6bc0", highlightbackground="#3949ab",
                width=20, bd=0, relief=tk.FLAT).pack(pady=10)
                
        tk.Button(button_frame, text="Sign Out", font=("Roboto", 14),
                command=self.logout_customer, bg="", fg="#ffffff",
                activebackground="#d32f2f", highlightbackground="#c62828",
                width=20, bd=0, relief=tk.FLAT).pack(pady=10)

    def customer_deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:", parent=self.root)
        if amount is not None:
            try:
                self.logged_in_customer.deposit(amount)
                messagebox.showinfo("Success", f"Deposited £{amount:.2f}\nNew balance: £{self.logged_in_customer.get_balance():.2f}")
                self.show_customer_dashboard()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def customer_withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:", parent=self.root)
        if amount is not None:
            try:
                self.logged_in_customer.withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew £{amount:.2f}\nNew balance: £{self.logged_in_customer.get_balance():.2f}")
                self.show_customer_dashboard()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def customer_show_balance(self):
        messagebox.showinfo("Account Balance", 
                          f"Current Balance: £{self.logged_in_customer.get_balance():.2f}\n"
                          f"Available: £{self.logged_in_customer.get_balance() + self.logged_in_customer.get_overdraft_limit():.2f}")

    def customer_update_details(self):
        self.clear_screen()
        self.root.title("Update Account Details")
        
        # Background image
        bg_label = tk.Label(self.root, image=self.customer_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        main_frame = tk.Frame(self.root, bg="#f8f9fa")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_frame = tk.Frame(main_frame, bg="#1a237e", height=80)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        tk.Label(header_frame, text="Update Account Details", 
                font=("Segoe UI", 20, "bold"), bg="#1a237e", fg="white").pack(pady=20)
        
        # Form
        form_frame = tk.Frame(main_frame, bg="#f8f9fa", padx=20, pady=20)
        form_frame.pack()
        
        tk.Label(form_frame, text="First Name:", 
                font=("Roboto", 14), bg="#f8f9fa", fg="#7986CB").grid(row=0, column=0, sticky="e", pady=5)
        self.first_name_entry = tk.Entry(form_frame, font=("Roboto", 14))
        self.first_name_entry.insert(0, self.logged_in_customer.get_first_name())
        self.first_name_entry.grid(row=0, column=1, pady=5, padx=10)
        
        tk.Label(form_frame, text="Last Name:", 
                font=("Roboto", 14), bg="#f8f9fa", fg="#7986CB").grid(row=1, column=0, sticky="e", pady=5)
        self.last_name_entry = tk.Entry(form_frame, font=("Roboto", 14))
        self.last_name_entry.insert(0, self.logged_in_customer.get_last_name())
        self.last_name_entry.grid(row=1, column=1, pady=5, padx=10)
        
        tk.Label(form_frame, text="Address:", 
                font=("Roboto", 14), bg="#f8f9fa", fg="#7986CB").grid(row=2, column=0, sticky="e", pady=5)
        self.address_entry = tk.Entry(form_frame, font=("Roboto", 14))
        self.address_entry.insert(0, ", ".join(self.logged_in_customer.get_address()))
        self.address_entry.grid(row=2, column=1, pady=5, padx=10)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg="#f8f9fa", padx=20, pady=20)
        button_frame.pack()
        
        # Buttons frame with Save and Back buttons
        button_frame = tk.Frame(main_frame, bg="#f8f9fa", padx=20, pady=20)
        button_frame.pack()
        
        save_btn = tk.Button(button_frame, text="Save Changes", font=("Roboto", 14),
                command=lambda: self.save_customer_details(self.logged_in_customer), bg="#26C6DA", fg="white",
                activebackground="#9CCC65", width=15, bd=0)
        save_btn.pack(side=tk.LEFT, padx=10)
        save_btn.bind("<Return>", lambda e: self.save_customer_details())
                
        tk.Button(button_frame, text="Back", font=("Roboto", 14),
                command=self.show_customer_dashboard, bg="#95a5a6", fg="white",
                activebackground="#7f8c8d", width=15, bd=0).pack(side=tk.LEFT, padx=10)

    def save_customer_details(self, customer=None):
        # If no customer specified, use logged in customer
        if customer is None:
            customer = self.logged_in_customer
            
        # Get field values
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        address = self.address_entry.get().strip()
        
        # Validate fields
        if not first_name:
            messagebox.showerror("Error", "First name cannot be empty")
            return
        if not last_name:
            messagebox.showerror("Error", "Last name cannot be empty")
            return
        if not address:
            messagebox.showerror("Error", "Address cannot be empty")
            return
            
        try:
            # Update customer details
            customer.update_first_name(first_name)
            customer.update_last_name(last_name)
            
            # Handle address - split by comma and strip whitespace
            address_parts = [part.strip() for part in address.split(",")]
            if len(address_parts) < 4:
                raise ValueError("Address must include street number, street, city, and postcode separated by commas")
                
            customer.update_address(address_parts)
            
            messagebox.showinfo("Success", "Account details updated successfully")
            self.show_customer_dashboard()
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid address format: {str(e)}\nPlease enter as: house number, street, city, postcode")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update details: {str(e)}")

    def show_self_details(self):
        """Show customer details screen with options to view or edit details"""
        self.clear_screen()
        
        # Background image
        bg_label = tk.Label(self.root, image=self.customer_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("My Account Details")
        
        # Main container for centering
        main_frame = tk.Frame(self.root, bg="#ffffff")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Centered content frame
        center_frame = tk.Frame(main_frame, bg="#ffffff")
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Customer details labels
        details = [
            ("Full Name:", self.logged_in_customer.get_full_name()),
            ("Account Number:", str(self.logged_in_customer.get_account_no())),
            ("Account Type:", self.logged_in_customer.get_account_type()),
            ("Balance:", f"£{self.logged_in_customer.get_balance():.2f}"),
            ("Interest Rate:", f"{self.logged_in_customer.get_interest_rate()*100:.2f}%"),
            ("Overdraft Limit:", f"£{self.logged_in_customer.get_overdraft_limit():.2f}"),
            ("Address:", ', '.join(self.logged_in_customer.get_address()))
        ]
        
        for i, (label, value) in enumerate(details):
            tk.Label(center_frame, text=label, font=("Roboto", 14), 
                   bg="#ffffff", fg="#1a237e").grid(row=i, column=0, sticky="e", pady=5, padx=10)
            tk.Label(center_frame, text=value, font=("Roboto", 14), 
                   bg="#ffffff", fg="#1a237e").grid(row=i, column=1, sticky="w", pady=5, padx=10)
        
        # Button frame centered at bottom
        button_frame = tk.Frame(main_frame, bg="#ffffff")
        button_frame.pack(side=tk.BOTTOM, pady=20)
        
        tk.Button(button_frame, text="Edit Details", font=("Roboto", 14),
                command=self.customer_update_details, bg="#3949ab", fg="#ffffff",
                activebackground="#5c6bc0", width=15, bd=0).pack(side=tk.LEFT, padx=10)
                
        tk.Button(button_frame, text="Back", font=("Roboto", 14),
                command=self.show_customer_dashboard, bg="#757575", fg="#ffffff",
                activebackground="#9e9e9e", width=15, bd=0).pack(side=tk.LEFT, padx=10)

    def customer_show_full_details(self):
        details = (
            f"Full Name: {self.logged_in_customer.get_full_name()}\n"
            f"Account Number: {self.logged_in_customer.get_account_no()}\n"
            f"Account Type: {self.logged_in_customer.get_account_type()}\n"
            f"Balance: £{self.logged_in_customer.get_balance():.2f}\n"
            f"Interest Rate: {self.logged_in_customer.get_interest_rate()*100:.2f}%\n"
            f"Overdraft Limit: £{self.logged_in_customer.get_overdraft_limit():.2f}\n"
            f"Address: {', '.join(self.logged_in_customer.get_address())}"
        )
        messagebox.showinfo("Account Details", details)

    def search_customer_screen(self):
        self.clear_screen()
        
        if not self.logged_in_admin:
            messagebox.showerror("Error", "Not logged in as admin")
            self.create_home_screen()
            return
            
        # Transparent background to show background image
        bg_label = tk.Label(self.root, image=self.staff_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("Client Search")
        
        search_frame = tk.Frame(self.root, bg="")
        search_frame.configure(bg="")
        search_frame.pack(pady=30)
        
        tk.Label(search_frame, text="Enter Client's Last Name", font=("Segoe UI", 14), bg="#7986CB", fg="#ecf0f1").pack(pady=5)
        self.customer_last_name_entry = tk.Entry(search_frame, font=("Segoe UI", 14), bd=2, relief=tk.FLAT)
        self.customer_last_name_entry.pack(pady=5, ipady=5)
        
        button_frame = tk.Frame(search_frame, bg="#7986CB")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Search", font=("Segoe UI", 14), 
                command=self.search_customer, bg="#26C6DA", fg="white", 
                activebackground="#9CCC65", width=15, bd=0).pack(side=tk.LEFT, padx=10)
                
        tk.Button(button_frame, text="Back", font=("Segoe UI", 14), 
                command=self.show_admin_dashboard, bg="#7f8c8d", fg="white", 
                activebackground="#95a5a6", width=15, bd=0).pack(side=tk.LEFT, padx=10)

    def search_customer(self):
        last_name = self.customer_last_name_entry.get()
        for customer in self.accounts:
            if customer.get_last_name().lower() == last_name.lower():
                self.logged_in_customer = customer
                self.show_customer_dashboard()
                return

        messagebox.showerror("Customer Not Found", "No customer found with that last name.")


    def show_all_customers(self):
        """Method to show all customer records in a table"""
        self.clear_screen()
        # Background image
        bg_label = tk.Label(self.root, image=self.staff_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("Customer Records")
        
        # Create the table with font size 14
        columns = ("First Name", "Last Name", "Account No", "Balance", "Account Type", "Interest Rate", "Overdraft Limit")
        tree = ttk.Treeview(self.root, columns=columns, show="headings", height=10)
        tree.configure(style="Treeview")
        tree.pack(pady=20)

        # Define column headings
        for col in columns:
            tree.heading(col, text=col, anchor="w")

        # Add customer data to the table
        for customer in self.accounts:
            tree.insert("", "end", values=(customer.get_first_name(), customer.get_last_name(),
                                          customer.get_account_no(), f"{customer.get_balance():.2f}",
                                          customer.get_account_type(), f"{customer.get_interest_rate() * 100}%",
                                          f"{customer.get_overdraft_limit()}"))

        # Style configuration for transparent background
        style = ttk.Style()
        style.configure("Treeview", background="", fieldbackground="")
        
        # Add export button
        export_frame = tk.Frame(self.root, bg="")
        export_frame.pack(pady=10)
        tk.Button(export_frame, text="Export to File", font=("Helvetica", 14), 
                 command=self.export_customer_data, bg="#0a9396", fg="white").pack(side=tk.LEFT, padx=10)
        
        # Add back button
        tk.Button(self.root, text="Back to Admin Dashboard", font=("Helvetica", 16), 
                command=self.show_admin_dashboard, bg="#0a9396", fg="white", bd=0).pack(pady=20)

    def export_customer_data(self):
        """Export customer data to a text file"""
        try:
            with open("customer_data.txt", "w") as f:
                f.write("First Name,Last Name,Account No,Balance,Account Type,Interest Rate,Overdraft Limit\n")
                for customer in self.accounts:
                    f.write(f"{customer.get_first_name()},{customer.get_last_name()},{customer.get_account_no()},")
                    f.write(f"{customer.get_balance():.2f},{customer.get_account_type()},")
                    f.write(f"{customer.get_interest_rate() * 100}%,{customer.get_overdraft_limit()}\n")
            messagebox.showinfo("Success", "Customer data exported to customer_data.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {str(e)}")

    def show_customer_dashboard(self, customer=None):
        self.clear_screen()
        if customer:
            self.logged_in_customer = customer
            
        # Background image
        bg_label = tk.Label(self.root, image=self.customer_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header(f"Quantum Client Portal - {self.logged_in_customer.get_full_name()}")
        
        # Main container with transparent background
        dashboard_frame = tk.Frame(self.root, bg="")
        dashboard_frame.pack(pady=30)
        
        # Account info
        info_frame = tk.Frame(dashboard_frame, bg="#7986CB", padx=20, pady=20)
        info_frame.pack(fill=tk.X)
        
        tk.Label(info_frame, text=f"Account Number: {self.logged_in_customer.get_account_no()}",
                font=("Segoe UI", 14), bg="#7986CB", fg="#ecf0f1").pack(anchor="w")
                
        tk.Label(info_frame, text=f"Balance: £{self.logged_in_customer.get_balance():.2f}",
                font=("Segoe UI", 14), bg="#7986CB", fg="#ecf0f1").pack(anchor="w")
                
        tk.Label(info_frame, text=f"Account Type: {self.logged_in_customer.get_account_type()}",
                font=("Segoe UI", 14), bg="#7986CB", fg="#ecf0f1").pack(anchor="w")
        
        # Action buttons grouped into categories
        button_frame = tk.Frame(dashboard_frame, bg="", padx=20, pady=20)
        button_frame.pack(fill=tk.X)

        # Fund Operations button
        tk.Button(button_frame, text="Fund Operations", font=("Segoe UI", 14),
                command=self.show_fund_operations, bg="#26C6DA", fg="white",
                activebackground="#9CCC65", width=20, bd=0).pack(pady=10)
        
        # Self Details button        
        tk.Button(button_frame, text="Self Details", font=("Segoe UI", 14),
                command=self.show_self_details, bg="#26C6DA", fg="white",
                activebackground="#9CCC65", width=20, bd=0).pack(pady=10)
                
        tk.Button(button_frame, text="Sign Out", font=("Segoe UI", 14),
                command=self.logout_customer, bg="#7f8c8d", fg="white",
                activebackground="#95a5a6", width=20, bd=0).pack(pady=10)

    def select_customer(self):
        last_name = simpledialog.askstring("Select Customer", "Enter last name:", parent=self.root)
        if last_name:
            for customer in self.accounts:
                if customer.get_last_name().lower() == last_name.lower():
                    return customer
            messagebox.showerror("Error", "Customer not found")
        return None

    def deposit_funds(self, customer):
        if customer is None:
            customer = self.select_customer()
        if not customer:
            return
        # Ask the user for the deposit amount
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit", parent=self.root)
        
        if amount:  # Check if a valid amount was entered
            if amount <= 0:  # Ensure the amount is positive
                messagebox.showerror("Error", "Deposit amount must be positive.")
            else:
                customer.deposit(amount)  # Call the deposit method of the customer
                messagebox.showinfo("Success", f"Deposited {amount} into {customer.get_first_name()}'s account.")

    def withdraw_funds(self, customer):
        if customer is None:
            customer = self.select_customer()
        if not customer:
            return
            
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw", parent=self.root)
        if amount and amount > 0:
            try:
                customer.withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew {amount} from account")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Invalid amount")


    def view_balance(self, customer):
        messagebox.showinfo("Balance", f"Your current balance is: {customer.get_balance()}")

    def view_customer_details(self, customer):
        details = f"Name: {customer.get_first_name()} {customer.get_last_name()}\nAddress: {', '.join(customer.get_address())}"
        messagebox.showinfo("Customer Details", details)

    def edit_customer_details(self, customer):
        self.clear_screen()
        self.create_header(f"Edit Customer: {customer.get_first_name()} {customer.get_last_name()}")
        
        # Create fields to edit customer details
        tk.Label(self.root, text="First Name", font=("Helvetica", 16)).pack(pady=10)
        self.first_name_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.first_name_entry.insert(0, customer.get_first_name())
        self.first_name_entry.pack(pady=10)

        tk.Label(self.root, text="Last Name", font=("Helvetica", 16)).pack(pady=10)
        self.last_name_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.last_name_entry.insert(0, customer.get_last_name())
        self.last_name_entry.pack(pady=10)

        tk.Label(self.root, text="Address", font=("Helvetica", 16)).pack(pady=10)
        self.address_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.address_entry.insert(0, ', '.join(customer.get_address()))
        self.address_entry.pack(pady=10)

        tk.Button(self.root, text="Save Changes", font=("Helvetica", 16), command=lambda: self.save_customer_details(customer), bg="#6F4F28", fg="white").pack(pady=10)
        tk.Button(self.root, text="Back", font=("Segoe UI", 14), command=lambda: self.show_customer_dashboard(customer), bg="#6c757d", fg="white", activebackground="#495057", width=20, bd=0, padx=10, pady=5).pack(pady=10)
        
    def save_customer_details(self, customer):
        # Fetch the updated details from the entry fields
        new_first_name = self.first_name_entry.get()
        new_last_name = self.last_name_entry.get()
        new_address = self.address_entry.get().split(', ')

        # Set the updated details to the customer object
        customer.update_first_name(new_first_name)
        customer.update_last_name(new_last_name)
        customer.update_address(new_address)
        
        # Display a success message
        messagebox.showinfo("Success", "Customer details updated successfully.")

        # Refresh the customer dashboard to reflect the updated details
        self.show_customer_dashboard(customer)

    def delete_customer_account_screen(self):
        self.clear_screen()
        self.create_header("Delete Customer Account")
        tk.Label(self.root, text="Enter Customer's Last Name", font=("Helvetica", 16), bg="#7986CB").pack(pady=10)
        self.delete_last_name_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.delete_last_name_entry.pack(pady=10)

        tk.Button(self.root, text="Delete", font=("Helvetica", 18), command=self.delete_customer_account, bg="#6F4F28", fg="white").pack(pady=20)
        tk.Button(self.root, text="Back to Admin Dashboard", font=("Helvetica", 18), command=self.show_admin_dashboard, bg="#6F4F28", fg="white").pack(pady=10)

    def delete_customer_account(self):
        last_name = self.delete_last_name_entry.get()
        for customer in self.accounts:
            if customer.get_last_name().lower() == last_name.lower():
                confirm = messagebox.askyesno("Confirm Deletion", 
                    f"Are you sure you want to delete {customer.get_first_name()} {customer.get_last_name()}'s account?")
                if confirm:
                    self.accounts.remove(customer)
                    messagebox.showinfo("Success", "Customer account deleted successfully.")
                    self.show_admin_dashboard()
                return

        messagebox.showerror("Error", "No customer found with that last name.")

    def initiate_transfer_screen(self):
        self.clear_screen()
        
        # Background image
        bg_label = tk.Label(self.root, image=self.staff_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("Initiate Fund Transfer")
        
        # Main container with transparent background
        transfer_frame = tk.Frame(self.root, bg="")
        transfer_frame.pack(pady=30)
        
        tk.Label(transfer_frame, text="Enter Sender's Account No", font=("Segoe UI", 14), bg="#7986CB", fg="#ecf0f1").pack(pady=5)
        self.sender_account_entry = tk.Entry(transfer_frame, font=("Segoe UI", 14), bd=2, relief=tk.FLAT)
        self.sender_account_entry.pack(pady=5, ipady=5)

        tk.Label(transfer_frame, text="Enter Receiver's Account No", font=("Segoe UI", 14), bg="#7986CB", fg="#ecf0f1").pack(pady=5)
        self.receiver_account_entry = tk.Entry(transfer_frame, font=("Segoe UI", 14), bd=2, relief=tk.FLAT)
        self.receiver_account_entry.pack(pady=5, ipady=5)

        tk.Label(transfer_frame, text="Enter Amount to Transfer", font=("Segoe UI", 14), bg="#7986CB", fg="#ecf0f1").pack(pady=5)
        self.transfer_amount_entry = tk.Entry(transfer_frame, font=("Segoe UI", 14), bd=2, relief=tk.FLAT)
        self.transfer_amount_entry.pack(pady=5, ipady=5)

        # Transfer buttons with blue palette
        button_frame = tk.Frame(transfer_frame, bg="#7986CB")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Transfer", font=("Segoe UI", 14), 
                command=self.transfer_funds, bg="#26C6DA", fg="white", 
                activebackground="#9CCC65", width=15, bd=0).pack(side=tk.LEFT, padx=10)
                
        tk.Button(button_frame, text="Back to Dashboard", font=("Segoe UI", 14), 
                command=self.show_admin_dashboard, bg="#7f8c8d", fg="white", 
                activebackground="#95a5a6", width=15, bd=0).pack(side=tk.LEFT, padx=10)

    def transfer_funds(self):
        sender_account_no = self.sender_account_entry.get()
        receiver_account_no = self.receiver_account_entry.get()
        amount = self.transfer_amount_entry.get()

        # Validate inputs
        if not sender_account_no or not receiver_account_no or not amount:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            amount = float(amount)
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return

        # Find accounts
        sender_account = next((acc for acc in self.accounts if str(acc.get_account_no()) == sender_account_no), None)
        receiver_account = next((acc for acc in self.accounts if str(acc.get_account_no()) == receiver_account_no), None)

        if not sender_account or not receiver_account:
            messagebox.showerror("Error", "One or both accounts not found")
            return

        # Check sufficient funds (including overdraft)
        if sender_account.get_balance() - amount < -sender_account.get_overdraft_limit():
            messagebox.showerror("Error", "Transfer exceeds available funds and overdraft limit")
            return

        # Perform transfer
        try:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
            
            # Show success popup with details
            messagebox.showinfo(
                "Transfer Successful",
                f"Transferred £{amount:.2f}\n\n"
                f"From: {sender_account.get_full_name()} (Acc# {sender_account_no})\n"
                f"New Balance: £{sender_account.get_balance():.2f}\n\n"
                f"To: {receiver_account.get_full_name()} (Acc# {receiver_account_no})\n"
                f"New Balance: £{receiver_account.get_balance():.2f}"
            )
            
            # Clear form fields
            self.sender_account_entry.delete(0, tk.END)
            self.receiver_account_entry.delete(0, tk.END)
            self.transfer_amount_entry.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Transfer Failed", str(e))

    def generate_report_screen(self):
        """Method to generate a comprehensive management report in table format"""
        self.clear_screen()
        self.create_header("Management Analytics")

        # Calculate report metrics
        total_customers = len(self.accounts)
        total_balance = sum(customer.get_balance() for customer in self.accounts)
        
        # Calculate interest by account type
        interest_by_type = {}
        for customer in self.accounts:
            if customer.get_balance() > 0:  # Only positive balances earn interest
                acc_type = customer.get_account_type()
                interest = customer.get_balance() * customer.get_interest_rate()
                interest_by_type[acc_type] = interest_by_type.get(acc_type, 0) + interest
        
        total_interest = sum(interest_by_type.values())
        
        # Calculate overdrafts
        overdrawn_accounts = []
        total_overdrafts = 0
        for customer in self.accounts:
            if customer.get_balance() < 0:
                overdrawn_accounts.append(customer)
                total_overdrafts += abs(customer.get_balance())

        # Modern styling
        self.root.configure(bg="#f5f5f5")
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Summary table
        summary_label = tk.Label(main_frame, text="Bank Summary", font=("Roboto", 16, "bold"), bg="#f5f5f5", fg="#1a237e")
        summary_label.pack(pady=(0, 10))
        
        summary_table = ttk.Treeview(main_frame, columns=("Metric", "Value"), show="headings", height=5)
        summary_table.heading("Metric", text="Metric")
        summary_table.heading("Value", text="Value")
        summary_table.column("Metric", width=200, anchor="w")
        summary_table.column("Value", width=150, anchor="e")
        
        # Add data to summary table
        summary_table.insert("", "end", values=("Total Customers", total_customers))
        summary_table.insert("", "end", values=("Total Deposits", f"£{total_balance:,.2f}"))
        summary_table.insert("", "end", values=("Annual Interest Payable", f"£{total_interest:,.2f}"))
        summary_table.insert("", "end", values=("Overdrawn Accounts", len(overdrawn_accounts)))
        summary_table.insert("", "end", values=("Total Overdrafts", f"£{total_overdrafts:,.2f}"))
        
        summary_table.pack(fill="x", padx=20, pady=10)
        
        # Interest by account type table
        if interest_by_type:
            interest_label = tk.Label(main_frame, text="Interest by Account Type", font=("Roboto", 16, "bold"), bg="#f5f5f5", fg="#1a237e")
            interest_label.pack(pady=(20, 10))
            
            interest_table = ttk.Treeview(main_frame, columns=("Account Type", "Interest"), show="headings", height=len(interest_by_type))
            interest_table.heading("Account Type", text="Account Type")
            interest_table.heading("Interest", text="Annual Interest")
            interest_table.column("Account Type", width=200, anchor="w")
            interest_table.column("Interest", width=150, anchor="e")
            
            for acc_type, interest in interest_by_type.items():
                interest_table.insert("", "end", values=(acc_type, f"£{interest:,.2f}"))
            
            interest_table.pack(fill="x", padx=20, pady=10)
        
        # Overdrawn accounts table
        if overdrawn_accounts:
            overdraft_label = tk.Label(main_frame, text="Overdrawn Accounts", font=("Roboto", 16, "bold"), bg="#f5f5f5", fg="#1a237e")
            overdraft_label.pack(pady=(20, 10))
            
            overdraft_table = ttk.Treeview(main_frame, columns=("Customer", "Account", "Overdraft"), show="headings", height=min(5, len(overdrawn_accounts)))
            overdraft_table.heading("Customer", text="Customer Name")
            overdraft_table.heading("Account", text="Account No")
            overdraft_table.heading("Overdraft", text="Overdraft Amount")
            overdraft_table.column("Customer", width=200, anchor="w")
            overdraft_table.column("Account", width=100, anchor="center")
            overdraft_table.column("Overdraft", width=150, anchor="e")
            
            for customer in overdrawn_accounts:
                overdraft_table.insert("", "end", values=(
                    f"{customer.get_first_name()} {customer.get_last_name()}",
                    customer.get_account_no(),
                    f"£{abs(customer.get_balance()):,.2f}"
                ))
            
            overdraft_table.pack(fill="x", padx=20, pady=10)
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg="#f5f5f5")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Export Report", font=("Roboto", 14),
                command=lambda: self.export_report(
                    total_customers,
                    total_balance,
                    interest_by_type,
                    len(overdrawn_accounts),
                    total_overdrafts,
                    overdrawn_accounts
                ),
                bg="#3949ab", fg="white", activebackground="#5c6bc0", width=20, bd=0).pack(side=tk.LEFT, padx=10)
                
        tk.Button(button_frame, text="Back to Dashboard", font=("Roboto", 14),
                command=self.show_admin_dashboard, bg="#757575", fg="white",
                activebackground="#9e9e9e", width=20, bd=0).pack(side=tk.LEFT, padx=10)

    def export_report(self, customers, balance, interest_by_type, overdrafts, total_overdraft, overdrawn_accounts=None):
        """Export the management report to a text file"""
        try:
            with open("management_report.txt", "w") as f:
                # Header
                f.write("="*60 + "\n")
                f.write("BANK MANAGEMENT REPORT".center(60) + "\n")
                f.write("="*60 + "\n\n")
                
                # Summary
                f.write(f"{'Total Customers:':<30}{customers:>30}\n")
                f.write(f"{'Total Deposits:':<30}£{balance:>29,.2f}\n")
                f.write(f"{'Annual Interest Payable:':<30}£{sum(interest_by_type.values()):>29,.2f}\n")
                f.write(f"{'Overdrawn Accounts:':<30}{overdrafts:>30}\n")
                f.write(f"{'Total Overdrafts:':<30}£{total_overdraft:>29,.2f}\n\n")
                
                # Interest by account type
                f.write("-"*60 + "\n")
                f.write("INTEREST BY ACCOUNT TYPE\n")
                f.write("-"*60 + "\n")
                for acc_type, interest in interest_by_type.items():
                    f.write(f"{acc_type + ':':<30}£{interest:>29,.2f}\n")
                
                # Overdrawn accounts
                if overdrawn_accounts:
                    f.write("\n" + "-"*60 + "\n")
                    f.write("OVERDRAWN ACCOUNTS\n")
                    f.write("-"*60 + "\n")
                    for customer in overdrawn_accounts:
                        f.write(
                            f"{customer.get_first_name()} {customer.get_last_name()} (Acc# {customer.get_account_no()}): "
                            f"£{abs(customer.get_balance()):,.2f}\n"
                        )
                
                f.write("\n" + "="*60 + "\n")
                
            messagebox.showinfo("Success", "Report exported to management_report.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export report: {str(e)}")

    def generate_all_customers_report(self):
        report = "\n".join([f"{customer.get_first_name()} {customer.get_last_name()} - Balance: {customer.get_balance():.2f}" for customer in self.accounts])
        messagebox.showinfo("Customer Report", report)


    def edit_admin_profile_screen(self):
        """Implement admin profile edit functionality"""
        self.clear_screen()
        
        # Background image
        bg_label = tk.Label(self.root, image=self.staff_bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_header("Edit Admin Profile")
        
        # Main container frame for centering
        main_frame = tk.Frame(self.root, bg="white")
        main_frame.pack(expand=True, fill="both", padx=50, pady=50)
        
        # Form frame centered in main frame
        form_frame = tk.Frame(main_frame, bg="white")
        form_frame.pack(expand=True)
        
        # First Name - centered
        tk.Label(form_frame, text="First Name:", font=("Helvetica", 14), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.first_name_entry = tk.Entry(form_frame, font=("Helvetica", 14))
        self.first_name_entry.insert(0, self.logged_in_admin.get_first_name())
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        
        # Last Name - centered
        tk.Label(form_frame, text="Last Name:", font=("Helvetica", 14), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.last_name_entry = tk.Entry(form_frame, font=("Helvetica", 14))
        self.last_name_entry.insert(0, self.logged_in_admin.get_last_name())
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Address - centered
        tk.Label(form_frame, text="Address:", font=("Helvetica", 14), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.address_entry = tk.Entry(form_frame, font=("Helvetica", 14))
        self.address_entry.insert(0, ', '.join(self.logged_in_admin.get_address()))
        self.address_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # Button frame centered below form
        button_frame = tk.Frame(main_frame, bg="white")
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Save Changes", font=("Helvetica", 14), 
                command=self.save_admin_profile_changes, bg="#26C6DA", fg="white", activebackground="#9CCC65").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Back to Dashboard", font=("Helvetica", 14), 
                command=self.show_admin_dashboard, bg="#26C6DA", fg="white", activebackground="#9CCC65").pack(side=tk.LEFT, padx=10)

    def save_admin_profile_changes(self):
        # Verify password before allowing changes
        password = simpledialog.askstring("Password Verification", 
                    "Enter your password to confirm changes:", 
                    show='*', parent=self.root)
        
        if password == self.logged_in_admin.get_password():
            try:
                self.logged_in_admin.set_first_name(self.first_name_entry.get())
                self.logged_in_admin.set_last_name(self.last_name_entry.get())
                self.logged_in_admin.set_address(self.address_entry.get().split(', '))
                
                # Update dashboard header to reflect changes
                self.show_admin_dashboard()
                messagebox.showinfo("Success", "Admin profile updated successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update profile: {str(e)}")
        else:
            messagebox.showerror("Error", "Incorrect password. Changes not saved.")


    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#FFFFFF")
    app = BankSystem(root)
    root.mainloop()
