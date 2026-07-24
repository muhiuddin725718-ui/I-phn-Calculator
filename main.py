import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# উইন্ডো সাইজ সেটআপ (মোবাইল ভিউ)
Window.size = (360, 640)

class CalculatorApp(App):
    def build(self):
        self.icon = ''
        self.title = 'iPhone Calculator'
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = False
        self.last_button = None
        
        # প্রধান লেআউট (ভার্টিক্যাল)
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # ব্যাকগ্রাউন্ড কালার কালো সেট করা (iOS Style)
        Window.clearcolor = (0, 0, 0, 1)

        # ডিসপ্লে লেবেল
        self.result = Label(
            text="0",
            font_size=60,
            halign="right",
            valign="bottom",
            size_hint=(1, 0.3),
            color=(1, 1, 1, 1)
        )
        self.result.bind(size=self.result.setter('text_size'))
        main_layout.add_widget(self.result)

        # বাটন লেআউট (৫ সারি, ৪ কলাম)
        buttons = [
            ['C', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        grid = GridLayout(cols=4, spacing=10, size_hint=(1, 0.7))

        for row in buttons:
            for label in row:
                # রঙ নির্ধারণ (iOS Style)
                if label in ['C', '+/-', '%']:
                    bg_color = (0.65, 0.65, 0.65, 1) # হালকা ধূসর
                    text_color = (0, 0, 0, 1)
                elif label in ['/', '*', '-', '+', '=']:
                    bg_color = (1, 0.6, 0, 1)       # কমলা
                    text_color = (1, 1, 1, 1)
                else:
                    bg_color = (0.2, 0.2, 0.2, 1)   # গাঢ় ধূসর
                    text_color = (1, 1, 1, 1)

                # '0' বাটনটি বড় করার জন্য শর্ত
                if label == '0':
                    button = Button(
                        text=label,
                        background_normal='',
                        background_color=bg_color,
                        color=text_color,
                        font_size=30,
                        bold=True,
                        size_hint_x=2
                    )
                else:
                    button = Button(
                        text=label,
                        background_normal='',
                        background_color=bg_color,
                        color=text_color,
                        font_size=30,
                        bold=True
                    )

                button.bind(on_press=self.on_button_press)
                grid.add_widget(button)

        main_layout.add_widget(grid)
        return main_layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = "0"
        elif button_text == "+/-":
            if current != "0":
                if current.startswith("-"):
                    self.result.text = current[1:]
                else:
                    self.result.text = "-" + current
        elif button_text == "%":
            try:
                self.result.text = str(float(current) / 100)
            except Exception:
                self.result.text = "Error"
        elif button_text == "=":
            try:
                # হিসেব প্রক্রিয়া সম্পন্ন করা
                solution = str(eval(self.result.text))
                # দশমিকের পর ০ থাকলে তা মুছে ফেলা
                if solution.endswith('.0'):
                    solution = solution[:-2]
                self.result.text = solution
            except Exception:
                self.result.text = "Error"
        else:
            if current == "0" and button_text != ".":
                self.result.text = button_text
            else:
                self.result.text += button_text

if __name__ == '__main__':
    CalculatorApp().run()
