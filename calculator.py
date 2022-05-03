import tkinter as tk

large_font_style = ("Arial",40,"bold")
small_font_style = ("Arial",16)
digit_font_style = ("Arial",24)
default_font_style = ("Arial", 20)

off_white = "#F8FAFF"
white = "#ffffff"
light_blue = "#CCEDFF"
light_gray = "#f5f5f5"
label_color = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("myCalculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.total_label, self.current_label = self.create_display_labels()

        self.digits = {
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            ".":(4,1),0:(4,2)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=light_gray, fg=label_color, padx=24, font=small_font_style)
        total_label.pack(expand=True, fill="both")
        current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=light_gray, fg=label_color, padx=24, font=large_font_style)
        current_label.pack(expand=True, fill="both")
        return total_label, current_label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=light_gray)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=white, fg=label_color, font=digit_font_style, borderwidth=0, command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
    
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=off_white, fg=label_color, font=default_font_style, borderwidth=0, command=lambda x=operator:self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+= 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=off_white, fg=label_color, font=default_font_style, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=light_blue, fg=label_color, font=default_font_style, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=off_white, fg=label_color, font=default_font_style, borderwidth=0, command=self.square)
        button.grid(row=0, column= 2, sticky=tk.NSEW)
    
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=off_white, fg=label_color, font=default_font_style, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column= 3, sticky=tk.NSEW)

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_current_label(self):
        self.current_label.config(text=self.current_expression[:11])

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_current_label()
    
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_current_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_current_label()

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_current_label()
    
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_current_label()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
