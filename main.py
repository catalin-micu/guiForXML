from tkinter import *
from PIL import ImageTk, Image
from controller import FileParser
from datetime import datetime


def main():

    def open_window(text: str, title: str, master):
        new_window = Toplevel(master)
        new_window.title(title)
        Label(new_window, text=text, bg='#313131', fg='#ffffff', padx=10, pady=10).pack(fill='both')

    def clear_output(text_widget: Text):
        text_widget.delete(1.0, END)

    def apply_query(text_widget: Text, result, starter: str='text starter \n'):
        text_widget.insert(END, 'Action log - {}\n'.format(datetime.now().isoformat()))
        text_widget.insert(END, starter + '\n' + str(result) + '\n\n')

    controller = FileParser()

    root = Tk()
    root.title('XML and JSON Parser')
    root.iconbitmap('./images/city_logo.ico')

    # ********************************************* header *********************************************

    header = LabelFrame(root, padx=5, pady=5, bg='#313131', fg='#ffffff')

    header_text = Label(header, text='Micu Marius Catalin, \ntema la materia XIS', height=7, padx=5, pady=5,
                        bg='#313131', fg='#ffffff')
    header_text.grid(row=0, column=1)

    acs_logo = ImageTk.PhotoImage(Image.open('./images/acs_logo.png'))
    logo_label = Label(header, image=acs_logo, padx=5, pady=5, bg='#313131')
    logo_label.grid(row=0, column=0)

    header.pack(fill=X)

    # end of header.
    body = LabelFrame(root, padx=5, pady=5, bg='#313131', fg='#ffffff')
    body.pack(fill=X)
    # ********************************************* menu buttons *********************************************
    btns_frame = LabelFrame(body, padx=5, pady=5, text='Menu', bg='#313131', fg='#ffffff')

    browse_xml = Button(btns_frame, text='Browse for XML file ', bg='#053597', fg='#ffffff', activebackground='#313131',
                        activeforeground='#ffffff',
                        command=lambda: apply_query(query_result, controller.browse_for_xml(), 'Loaded XML file:'))
    browse_xml.grid(row=0, column=0, padx=5, pady=2.5)

    display_xml = Button(btns_frame, text='Parse XML file ', bg='#0859fc', fg='#ffffff', activebackground='#313131',
                   activeforeground='#ffffff',
                   command=lambda: apply_query(query_result, controller.display_xml(), 'Parsed XML file:\n\n'))
    display_xml.grid(row=0, column=1, padx=5, pady=2.5)

    browse_json = Button(btns_frame, text='Browse for JSON file', bg='#053597', fg='#ffffff', activebackground='#313131',
                         activeforeground='#ffffff',
                         command=lambda: apply_query(query_result, controller.browse_for_json(), 'Loaded JSON file:'))
    browse_json.grid(row=1, column=0, padx=5, pady=2.5)
    display_json = Button(btns_frame, text='Parse JSON file', bg='#0859fc', fg='#ffffff', activebackground='#313131',
                         activeforeground='#ffffff',
                         command=lambda: apply_query(query_result, controller.display_json(), 'Parsed JSON file:\n\n'))
    display_json.grid(row=1, column=1, padx=5, pady=2.5)

    browse_xsl = Button(btns_frame, text='Browse for XSL file   ', bg='#053597', fg='#ffffff', activebackground='#313131',
                        activeforeground='#ffffff',
                        command=lambda: apply_query(query_result, controller.browse_for_xsl(), 'Loaded XSL file:'))
    browse_xsl.grid(row=2, column=0, padx=5, pady=2.5)
    use_xsl_style = Button(btns_frame, text='Use XSL style format', bg='#0859fc', fg='#ffffff',
                           activebackground='#313131', activeforeground='#ffffff',
                           command=lambda: apply_query(query_result, controller.render_xsl(), 'Applied XSL style\n\n'))
    use_xsl_style.grid(row=2, column=1, padx=5, pady=2.5)

    btns_frame.grid(row=0, column=0, padx=3)

    # ********************************************* dropdown menus *********************************************
    boxes_frame = LabelFrame(body, padx=5, pady=8, text='Dynamic Query', bg='#313131', fg='#ffffff')

    label1 = Label(boxes_frame, text='Comediant', bg='#313131', fg='#ffffff', padx=5, pady=2.5)
    label1.grid(row=0, column=0)
    selected1 = StringVar()
    selected1.set('-')
    options1 = ["-", "Teo", "Vio", "Costel", "Nae Nicolae", "Mihai Bobonete", "Adrian Vancica", "Constantin Dita",
                "Mihai Rait", "Cristi Popesco", "Radu Bucale", "Sorin Parcalab", "Ionut Rusu", "Radu Bucalae",
                "George Tanase", "State", "Catalin Bordea", "Cosmin Nedelcu Micutzu", "George Adrian", "Sergiu Mirica",
                "Cirje", "Dan Badea", "Horatiu Malaele", "Bogdan Malaele"]
    drop1 = OptionMenu(boxes_frame, selected1, *options1)
    drop1.config(width=20, bg='#26aae0', fg='#ffffff', activebackground='#313131', activeforeground='#ffffff')
    drop1.grid(row=0, column=1)

    label2 = Label(boxes_frame, text='Oras', bg='#313131', fg='#ffffff', padx=5, pady=2.5)
    label2.grid(row=1, column=0)
    selected2 = StringVar()
    selected2.set('-')
    options2 = ["-", "Bucuresti", "Craiova", "Targu Mures", "Bacau"]
    drop2 = OptionMenu(boxes_frame, selected2, *options2)
    drop2.config(width=20, bg='#26aae0', fg='#ffffff', activebackground='#313131', activeforeground='#ffffff')
    drop2.grid(row=1, column=1)

    label3 = Label(boxes_frame, text='Pret', bg='#313131', fg='#ffffff', padx=5, pady=2.5)
    label3.grid(row=2, column=0)
    selected3 = StringVar()
    selected3.set('-')
    options3 = ['-', 'sub 300 ron', 'sub 250 ron', 'sub 200 ron', 'sub 175 ron', 'sub 150 ron', 'sub 120 ron']
    drop3 = OptionMenu(boxes_frame, selected3, *options3)
    drop3.config(width=20, bg='#26aae0', fg='#ffffff', activebackground='#313131', activeforeground='#ffffff')
    drop3.grid(row=2, column=1)

    boxes_frame.grid(row=0, column=1)

    apply = Button(body, text='Apply query', bg='#26aae0', fg='#ffffff', activebackground='#313131',
                   activeforeground='#ffffff',
                   command=lambda: apply_query(query_result, controller.dynamic_query(selected1.get(), selected2.get(), selected3.get(),),
                                               'Result of dynamic query:\n'))
    apply.grid(row=0, column=2, padx=10)
    # ********************************************* output *********************************************
    output = LabelFrame(root, padx=5, pady=5, bg='#313131', fg='#ffffff', text='Console:')
    output.pack(fill=X)

    query_result = Text(output, relief='sunken', height=15, width=85)
    query_result.grid(row=0, column=0, padx=5)
    scrollbar = Scrollbar(output)
    scrollbar.grid(row=0, column=1, sticky=N+S)
    scrollbar.config(command=query_result.yview)
    query_result.config(yscrollcommand=scrollbar.set)

    clear_btn = Button(output, text='Clear', bg='#053597', fg='#ffffff', activebackground='#313131',
                       activeforeground='#ffffff', command=lambda: clear_output(query_result))
    clear_btn.grid(row=1, pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
