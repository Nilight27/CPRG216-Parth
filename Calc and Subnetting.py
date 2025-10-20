"""
Modern Calculator with GUI and Network Subnetting
A sleek calculator application with subnet calculator built with tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import ipaddress

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator & Subnet Tool")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # Calculator state
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.result = False
        self.mode = "calculator"  # "calculator" or "subnet"
        
        # Create mode selector
        self.create_mode_selector()
        
        # Create the display
        self.create_display()
        
        # Create the buttons
        self.create_buttons()
        
        # Create subnet calculator
        self.create_subnet_calculator()
        
        # Bind keyboard events
        self.root.bind('<Key>', self.key_press)
        self.root.focus_set()
    
    def create_mode_selector(self):
        """Create mode selector buttons"""
        mode_frame = tk.Frame(self.root, bg='#2c3e50')
        mode_frame.pack(fill='x', padx=20, pady=(10, 5))
        
        self.calc_btn = tk.Button(
            mode_frame,
            text="Calculator",
            font=('Arial', 14, 'bold'),
            bg='#e74c3c',
            fg='white',
            relief='flat',
            command=self.switch_to_calculator
        )
        self.calc_btn.pack(side='left', padx=5)
        
        self.subnet_btn = tk.Button(
            mode_frame,
            text="Subnet Calculator",
            font=('Arial', 14, 'bold'),
            bg='#95a5a6',
            fg='#2c3e50',
            relief='flat',
            command=self.switch_to_subnet
        )
        self.subnet_btn.pack(side='left', padx=5)
    
    def switch_to_calculator(self):
        """Switch to calculator mode"""
        self.mode = "calculator"
        self.calc_btn.configure(bg='#e74c3c', fg='white')
        self.subnet_btn.configure(bg='#95a5a6', fg='#2c3e50')
        self.show_calculator()
    
    def switch_to_subnet(self):
        """Switch to subnet calculator mode"""
        self.mode = "subnet"
        self.calc_btn.configure(bg='#95a5a6', fg='#2c3e50')
        self.subnet_btn.configure(bg='#e74c3c', fg='white')
        self.show_subnet()
    
    def show_calculator(self):
        """Show calculator interface"""
        self.display_frame.pack(fill='x', padx=20, pady=(20, 10))
        self.button_frame.pack(fill='both', expand=True, padx=20, pady=10)
        self.subnet_frame.pack_forget()
    
    def show_subnet(self):
        """Show subnet calculator interface"""
        self.display_frame.pack_forget()
        self.button_frame.pack_forget()
        self.subnet_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
    def create_display(self):
        """Create the calculator display"""
        self.display_frame = tk.Frame(self.root, bg='#2c3e50', height=120)
        self.display_frame.pack(fill='x', padx=20, pady=(20, 10))
        self.display_frame.pack_propagate(False)
        
        # Main display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.display = tk.Label(
            self.display_frame,
            textvariable=self.display_var,
            font=('Arial', 32, 'bold'),
            bg='#34495e',
            fg='white',
            anchor='e',
            padx=20,
            pady=20
        )
        self.display.pack(fill='both', expand=True)
        
        # Secondary display for operations
        self.secondary_var = tk.StringVar()
        self.secondary_var.set("")
        
        self.secondary_display = tk.Label(
            self.display_frame,
            textvariable=self.secondary_var,
            font=('Arial', 14),
            bg='#34495e',
            fg='#bdc3c7',
            anchor='e',
            padx=20
        )
        self.secondary_display.pack(fill='x')
        
    def create_buttons(self):
        """Create calculator buttons"""
        self.button_frame = tk.Frame(self.root, bg='#2c3e50')
        self.button_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Button configuration
        button_config = {
            'font': ('Arial', 18, 'bold'),
            'relief': 'flat',
            'borderwidth': 0,
            'width': 4,
            'height': 2
        }
        
        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            ['0', None, '.', '=']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == None: # Skip the none button
                    continue
                # Determine button style
                if text in ['C', '±', '%']:
                    bg_color = '#95a5a6'
                    fg_color = '#2c3e50'
                elif text in ['÷', '×', '−', '+', '=']:
                    bg_color = '#e74c3c'
                    fg_color = 'white'
                else:
                    bg_color = '#ecf0f1'
                    fg_color = '#2c3e50'
                
                # Special handling for 0 button (span 2 columns)
                if text == '0':
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        bg=bg_color,
                        fg=fg_color,
                        command=lambda t=text: self.button_click(t),
                        **button_config
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky='nsew', padx=2, pady=2)
                elif text == '=' and j == 3:  # Rightmost equals button
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        bg=bg_color,
                        fg=fg_color,
                        command=lambda t=text: self.button_click(t),
                        **button_config
                    )
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                elif text != '=' or j != 2:  # Skip the duplicate equals
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        bg=bg_color,
                        fg=fg_color,
                        command=lambda t=text: self.button_click(t),
                        **button_config
                    )
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
        
        # Configure grid weights
        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.button_frame.grid_columnconfigure(j, weight=1)
    
    def create_subnet_calculator(self):
        """Create subnet calculator interface"""
        self.subnet_frame = tk.Frame(self.root, bg='#2c3e50')
        
        # Title
        title_label = tk.Label(
            self.subnet_frame,
            text="Network Subnet Calculator",
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=(20, 30))
        
        # Input frame
        input_frame = tk.Frame(self.subnet_frame, bg='#2c3e50')
        input_frame.pack(fill='x', padx=20, pady=10)
        
        # Network address input
        tk.Label(
            input_frame,
            text="Network Address:",
            font=('Arial', 12, 'bold'),
            bg='#2c3e50',
            fg='white'
        ).pack(anchor='w')
        
        self.network_entry = tk.Entry(
            input_frame,
            font=('Arial', 14),
            width=20,
            relief='flat',
            bd=5
        )
        self.network_entry.pack(fill='x', pady=(5, 15))
        self.network_entry.insert(0, "192.168.1.0/24")
        
        # Subnet mask or CIDR input
        mask_frame = tk.Frame(input_frame, bg='#2c3e50')
        mask_frame.pack(fill='x', pady=10)
        
        tk.Label(
            mask_frame,
            text="Subnet Mask (optional):",
            font=('Arial', 12, 'bold'),
            bg='#2c3e50',
            fg='white'
        ).pack(anchor='w')
        
        self.mask_entry = tk.Entry(
            mask_frame,
            font=('Arial', 14),
            width=20,
            relief='flat',
            bd=5
        )
        self.mask_entry.pack(fill='x', pady=(5, 15))
        
        # Calculate button
        calc_btn = tk.Button(
            input_frame,
            text="Calculate Subnet",
            font=('Arial', 14, 'bold'),
            bg='#e74c3c',
            fg='white',
            relief='flat',
            command=self.calculate_subnet,
            height=2
        )
        calc_btn.pack(fill='x', pady=20)
        
        # Results frame
        results_frame = tk.Frame(self.subnet_frame, bg='#34495e', relief='flat', bd=2)
        results_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Results title
        tk.Label(
            results_frame,
            text="Subnet Information",
            font=('Arial', 16, 'bold'),
            bg='#34495e',
            fg='white'
        ).pack(pady=10)
        
        # Results text
        self.results_text = tk.Text(
            results_frame,
            font=('Courier', 11),
            bg='#2c3e50',
            fg='white',
            relief='flat',
            bd=0,
            wrap='word'
        )
        self.results_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Scrollbar for results
        scrollbar = tk.Scrollbar(results_frame)
        scrollbar.pack(side='right', fill='y')
        self.results_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.results_text.yview)
    
    def calculate_subnet(self):
        """Calculate subnet information"""
        try:
            network_input = self.network_entry.get().strip()
            mask_input = self.mask_entry.get().strip()
            
            if not network_input:
                messagebox.showerror("Error", "Please enter a network address")
                return
            
            # Parse network address
            if '/' in network_input:
                # CIDR notation
                network = ipaddress.ip_network(network_input, strict=False)
            else:
                # IP address only, need subnet mask
                if mask_input:
                    if '.' in mask_input:
                        # Dotted decimal mask
                        network = ipaddress.ip_network(f"{network_input}/{mask_input}", strict=False)
                    else:
                        # CIDR prefix length
                        network = ipaddress.ip_network(f"{network_input}/{mask_input}", strict=False)
                else:
                    messagebox.showerror("Error", "Please provide subnet mask or use CIDR notation")
                    return
            
            # Calculate subnet information
            self.display_subnet_info(network)
            
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid network address: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def display_subnet_info(self, network):
        """Display subnet information in results text"""
        self.results_text.delete(1.0, tk.END)
        
        # Basic network information
        info = f"""
🌐 NETWORK INFORMATION
{'='*50}

Network Address:     {network.network_address}
Network Mask:        {network.netmask}
Wildcard Mask:       {network.hostmask}
CIDR Notation:       /{network.prefixlen}
Network Class:       {self.get_network_class(network)}

📊 ADDRESS CALCULATIONS
{'='*50}

Total Addresses:     {network.num_addresses:,}
Usable Hosts:        {network.num_addresses - 2:,}
First Host:          {network.network_address + 1}
Last Host:           {network.broadcast_address - 1}
Broadcast Address:   {network.broadcast_address}

🔍 BINARY REPRESENTATION
{'='*50}

Network Address:     {self.ip_to_binary(network.network_address)}
Subnet Mask:         {self.ip_to_binary(network.netmask)}
Wildcard Mask:       {self.ip_to_binary(network.hostmask)}

📈 SUBNET BREAKDOWN
{'='*50}

Network Bits:        {network.prefixlen}
Host Bits:           {32 - network.prefixlen}
Subnets Possible:    {2**(32 - network.prefixlen):,}
Hosts per Subnet:    {network.num_addresses:,}

🎯 SPECIAL ADDRESSES
{'='*50}

Network ID:          {network.network_address}
Broadcast:           {network.broadcast_address}
First Usable:        {network.network_address + 1}
Last Usable:         {network.broadcast_address - 1}

🔧 SUBNETTING EXAMPLES
{'='*50}

To create subnets with {network.num_addresses // 4} hosts each:
- Use /{network.prefixlen + 2} mask (255.255.255.192)
- Creates {2**(network.prefixlen + 2 - network.prefixlen)} subnets
- Each subnet has {network.num_addresses // 4} addresses

To create subnets with {network.num_addresses // 8} hosts each:
- Use /{network.prefixlen + 3} mask (255.255.255.224)
- Creates {2**(network.prefixlen + 3 - network.prefixlen)} subnets
- Each subnet has {network.num_addresses // 8} addresses
"""
        
        self.results_text.insert(tk.END, info)
        self.results_text.see(tk.END)

        # If user provided a target prefix in the mask entry, list subnet network addresses
        mask_text = self.mask_entry.get().strip()
        if mask_text:
            try:
                mt = mask_text
                if mt.startswith('/'):
                    mt = mt[1:]
                # convert dotted mask to prefix if needed
                if '.' in mt:
                    target_prefix = ipaddress.ip_network(f"0.0.0.0/{mt}", strict=False).prefixlen
                else:
                    target_prefix = int(mt)

                if target_prefix <= network.prefixlen:
                    self.results_text.insert(tk.END, f"\nNote: target prefix /{target_prefix} is not larger than network prefix /{network.prefixlen}; no subnets to list.\n")
                elif not (0 <= target_prefix <= 32):
                    self.results_text.insert(tk.END, f"\nNote: invalid target prefix /{target_prefix}.\n")
                else:
                    # Generate subnets at the requested prefix and list their network addresses
                    subnets = list(network.subnets(new_prefix=target_prefix))
                    total = len(subnets)
                    MAX_SHOW = 1024
                    PREVIEW = 128

                    if total == 0:
                        self.results_text.insert(tk.END, "\nNo subnets generated.\n")
                    else:
                        if total <= MAX_SHOW:
                            lines = '\n'.join(f"{s.network_address}/{s.prefixlen}" for s in subnets)
                        else:
                            first_part = '\n'.join(f"{s.network_address}/{s.prefixlen}" for s in subnets[:PREVIEW])
                            last_part = '\n'.join(f"{s.network_address}/{s.prefixlen}" for s in subnets[-PREVIEW:])
                            lines = f"{first_part}\n...\n{last_part}\n\n(Showing first {PREVIEW} and last {PREVIEW} of {total} subnets)"

                        header = f"\nALL SUBNET NETWORK ADDRESSES (/{target_prefix}) - {total} subnets\n{'='*50}\n"
                        self.results_text.insert(tk.END, header + lines + "\n")
                        self.results_text.see(tk.END)

            except Exception as e:
                self.results_text.insert(tk.END, f"\nCould not list subnet networks: {e}\n")
                self.results_text.see(tk.END)
    
    def get_network_class(self, network):
        """Determine network class"""
        first_octet = int(str(network.network_address).split('.')[0])
        if 1 <= first_octet <= 126:
            return "Class A"
        elif 128 <= first_octet <= 191:
            return "Class B"
        elif 192 <= first_octet <= 223:
            return "Class C"
        elif 224 <= first_octet <= 239:
            return "Class D (Multicast)"
        elif 240 <= first_octet <= 255:
            return "Class E (Reserved)"
        else:
            return "Unknown"
    
    def ip_to_binary(self, ip):
        """Convert IP address to binary representation"""
        octets = str(ip).split('.')
        binary_octets = [format(int(octet), '08b') for octet in octets]
        return '.'.join(binary_octets)
    
    def button_click(self, value):
        """Handle button clicks"""
        if value.isdigit():
            self.input_number(value)
        elif value == '.':
            self.input_decimal()
        elif value in ['÷', '×', '−', '+']:
            self.input_operator(value)
        elif value == '=':
            self.calculate()
        elif value == 'C':
            self.clear()
        elif value == '±':
            self.toggle_sign()
        elif value == '%':
            self.percentage()
    
    def input_number(self, num):
        """Handle number input"""
        if self.result:
            self.current = "0"
            self.result = False
        
        if self.current == "0":
            self.current = num
        else:
            self.current += num
        
        self.update_display()
    
    def input_decimal(self):
        """Handle decimal point input"""
        if self.result:
            self.current = "0"
            self.result = False
        
        if '.' not in self.current:
            self.current += '.'
            self.update_display()
    
    def input_operator(self, op):
        """Handle operator input"""
        if self.operator and not self.result:
            self.calculate()
        
        self.previous = self.current
        self.operator = op
        self.current = "0"
        self.update_secondary_display()
    
    def calculate(self):
        """Perform calculation"""
        if not self.operator or not self.previous:
            return
        
        try:
            prev = float(self.previous)
            curr = float(self.current)
            
            if self.operator == '+':
                result = prev + curr
            elif self.operator == '−':
                result = prev - curr
            elif self.operator == '×':
                result = prev * curr
            elif self.operator == '÷':
                if curr == 0:
                    self.current = "Error"
                    self.update_display()
                    return
                result = prev / curr
            
            # Format result
            if result == int(result):
                self.current = str(int(result))
            else:
                self.current = str(result)
            
            self.result = True
            self.operator = ""
            self.previous = ""
            self.update_display()
            self.update_secondary_display()
            
        except Exception:
            self.current = "Error"
            self.update_display()
    
    def clear(self):
        """Clear calculator"""
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.result = False
        self.update_display()
        self.update_secondary_display()
    
    def toggle_sign(self):
        """Toggle sign of current number"""
        if self.current != "0" and self.current != "Error":
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.update_display()
    
    def percentage(self):
        """Convert current number to percentage"""
        if self.current != "0" and self.current != "Error":
            try:
                value = float(self.current)
                result = value / 100
                if result == int(result):
                    self.current = str(int(result))
                else:
                    self.current = str(result)
                self.update_display()
            except Exception:
                self.current = "Error"
                self.update_display()
    
    def update_display(self):
        """Update main display"""
        self.display_var.set(self.current)
    
    def update_secondary_display(self):
        """Update secondary display"""
        if self.previous and self.operator:
            self.secondary_var.set(f"{self.previous} {self.operator}")
        else:
            self.secondary_var.set("")
    
    def key_press(self, event):
        """Handle keyboard input"""
        if self.mode == "subnet":
            return  # Don't handle calculator keys in subnet mode
        
        key = event.char
        
        if key.isdigit():
            self.input_number(key)
        elif key == '.':
            self.input_decimal()
        elif key in ['+', '-', '*', '/']:
            # Map keyboard operators to display operators
            operator_map = {'+': '+', '-': '−', '*': '×', '/': '÷'}
            self.input_operator(operator_map[key])
        elif key == '\r' or key == '=':  # Enter or equals
            self.calculate()
        elif key == '\b':  # Backspace
            self.backspace()
        elif key.lower() == 'c':  # Clear
            self.clear()
    
    def backspace(self):
        """Handle backspace"""
        if self.current != "0" and self.current != "Error" and not self.result:
            if len(self.current) > 1:
                self.current = self.current[:-1]
            else:
                self.current = "0"
            self.update_display()

def main():
    """Main function to run the calculator"""
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
