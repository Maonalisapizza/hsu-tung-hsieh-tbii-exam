import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from datetime import date
from datetime import datetime
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk

# Variables
subpage_title_font = ("Helvetica", 30, "bold")
button_icon_font = ("Helvetica", 30, "bold")
button_font = ("Helvetica", 20, "bold")
registration_font = ("Helvetica", 20)
label_font = ("Helvetica", 16)
suggestion_label_font = ("Helvetica", 20, "bold")
reference_font = ("Helvetica", 12, "italic")

button_color = "white"
theme_color = "#faf4e9"

mainpage_frame_width = 1000
mainpage_frame_height = 625
subpage_frame_width = 1000
subpage_frame_height = 625
scrollable_frame_width = subpage_frame_width-50
scrollable_frame_height = subpage_frame_height-150

suggestion_label_width = 70
suggestion_label_height = 4

# For the export function
sex = ""
surgery = ""
pronoun = ""
temperature_record_list = []
medicine_record_list = []

pressed_about_medicine = True
pressed_famous_diseases = True

def ask_birthday():
    global birthday_label, calendar, confirm_button, name, bg_birthday_label
    name = patient_name_entry.get().title()

    # Clear previous widgets
    patient_name_label.place_forget()
    patient_name_entry.place_forget()
    patient_name_button.place_forget()
    bg_cover_label.place_forget()

    bg_birthday_label = tk.Label(root, image=birthday_image)
    bg_birthday_label.place(x=0, y=0, relwidth=1, relheight=1)

    birthday_label = tk.Label(root, text=f"Select {name}'s birthday", bg=theme_color, font=registration_font, pady=10)
    birthday_label.place(x=456, y=50)

    calendar = DateEntry(root, font=registration_font, selectmode="day")
    calendar.place(x=456, y=95)

    confirm_button = tk.Button(root, text="Confirm", bg=button_color, font=button_font,
                               command=lambda: calculate_age(calendar.get_date()))
    confirm_button.place(x=456, y=150)


def calculate_age(selected_birthday):
    global age_years, age_months, age_export
    today = date.today()
    age_years = today.year - selected_birthday.year - ((today.month, today.day) < (selected_birthday.month, selected_birthday.day))

    if age_years == 0:
        age_months = today.month - selected_birthday.month
        if age_months < 0:
            age_years -= 1  # Make it negative to show that the patient is under 1 year old
            age_months += 12  # Add 12 months to the negative month difference

    if age_years <= 0:
        age_export = (f"{age_months} months old")
    else:
        age_export = (f"{age_years} years old")

    ask_height_weight()

def ask_height_weight():
    global height_label, height_entry, weight_label, weight_entry, submit_button, bg_height_and_weight_label

    birthday_label.place_forget()
    calendar.place_forget()
    confirm_button.place_forget()
    bg_birthday_label.place_forget()

    bg_height_and_weight_label = tk.Label(root, image=height_and_weight_image)
    bg_height_and_weight_label.place(x=0, y=0, relwidth=1, relheight=1)

    height_label = tk.Label(root, text=f"Enter {name}'s height (cm):", font=registration_font, bg=theme_color, pady=10)
    height_label.place(x=560, y=100)

    height_entry = tk.Entry(root, font=registration_font)
    height_entry.place(x=560, y=145)

    weight_label = tk.Label(root, text=f"Enter {name}'s weight (kg):", font=registration_font, bg=theme_color, pady=10)
    weight_label.place(x=560, y=190)

    weight_entry = tk.Entry(root, font=registration_font)
    weight_entry.place(x=560, y=235)

    submit_button = tk.Button(root, text="Submit", bg=button_color, font=button_font,
                              command=process_height_weight)
    submit_button.place(x=560, y=300)


def process_height_weight():
    global weight, height
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        if 30 <= height <= 300 and 0 <= weight <= 700:
            ask_sex_assigned_at_birth()
        else:
            messagebox.showerror("Invalid Input", "The height must be 30cm~300cm\nThe weight must be 0kg~700kg")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for height and weight")


def ask_sex_assigned_at_birth():
    global sex_label, male_button, female_button, bg_sex_label
    # Clear previous widgets
    height_label.place_forget()
    height_entry.place_forget()
    weight_label.place_forget()
    weight_entry.place_forget()
    submit_button.place_forget()
    bg_height_and_weight_label.place_forget()

    bg_sex_label = tk.Label(root, image=sex_image)
    bg_sex_label.place(x=0, y=0, relwidth=1, relheight=1)

    sex_label = tk.Label(root, text=f"Select {name}'s sex assigned at birth:", font=registration_font, bg=theme_color, pady=10)
    sex_label.place(x=560, y=300)

    male_button = tk.Button(root, text="Male", bg=button_color, font=button_font,
                            command=lambda: get_sex("Male"))
    male_button.place(x=560, y=345)

    female_button = tk.Button(root, text="Female", bg=button_color, font=button_font,
                              command=lambda: get_sex("Female"))
    female_button.place(x=660, y=345)


def get_sex(selected_sex):
    global sex
    sex = selected_sex
    ask_gender_affirmation()


def ask_gender_affirmation():
    global affirmation_label, yes_button, no_button, bg_affirmation_label
    # Clear previous widgets
    sex_label.place_forget()
    male_button.place_forget()
    female_button.place_forget()
    bg_sex_label.place_forget()

    bg_affirmation_label = tk.Label(root, image=affirmation_image)
    bg_affirmation_label.place(x=0, y=0, relwidth=1, relheight=1)

    # New widgets for asking about gender affirmation surgery
    affirmation_label = tk.Label(root, text=f"Has {name} ever undergone\nGender Affirmation Surgery?", justify="left", font=registration_font, bg=theme_color, pady=10)
    affirmation_label.place(x=500, y=170)

    yes_button = tk.Button(root, text="Yes", bg=button_color, font=button_font,
                           command=lambda: handle_affirmation_response(True))
    yes_button.place(x=500, y=245)

    no_button = tk.Button(root, text="No", bg=button_color, font=button_font,
                          command=lambda: handle_affirmation_response(False))
    no_button.place(x=580, y=245)

def handle_affirmation_response(undergone_surgery):
    global surgery
    if undergone_surgery:
        messagebox.showinfo("Notice", "This application acknowledges the complexities involved in Gender Affirmation Surgery, which is a significant medical decision. Such matters require careful consideration and are best addressed under the guidance of qualified healthcare professionals who specialize in gender-related healthcare.\n\nFor comprehensive support and tailored medical advice, we recommend consulting with appropriate healthcare providers. Thank you for understanding.")
    else:
        surgery = "No"
        ask_preferred_pronoun()

def ask_preferred_pronoun():
    global pronoun_label, pronoun_dropdown, pronoun_entry, submit_button, pronoun_var, bg_pronoun_label

    affirmation_label.place_forget()
    yes_button.place_forget()
    no_button.place_forget()
    bg_affirmation_label.place_forget()

    bg_pronoun_label = tk.Label(root, image=pronoun_image)
    bg_pronoun_label.place(x=0, y=0, relwidth=1, relheight=1)

    pronoun_label = tk.Label(root, text=f"What are {name}'s preferred pronouns?", font=registration_font, bg=theme_color, pady=10)
    pronoun_label.place(x=470, y=150)

    pronoun_options = ["He / Him", "She / Her", "They / Them", "Other (please specify)"]
    pronoun_var = tk.StringVar(root)
    pronoun_dropdown = tk.OptionMenu(root, pronoun_var, *pronoun_options)
    pronoun_dropdown.config(font=registration_font, bg=theme_color, width=15)
    pronoun_dropdown.place(x=550, y=280)

    pronoun_entry = tk.Entry(root, font=registration_font)
    pronoun_entry.place(x=550, y=325)

    submit_button = tk.Button(root, text="Submit", bg=button_color, font=button_font,
                              command=lambda: submit_pronouns(pronoun_var.get(), pronoun_entry.get()))
    submit_button.place(x=550, y=370)

def submit_pronouns(selected_pronoun, custom_pronoun=""):
    global pronoun
    if selected_pronoun == "Other (please specify)":
        selected_pronoun = custom_pronoun
        pronoun = custom_pronoun
    elif selected_pronoun != "Other (please specify)":
        pronoun = pronoun_var.get()
    # Proceed to terms and conditions page
    show_terms_and_conditions()

def show_terms_and_conditions():
    global terms_and_conditions_label, agree_button, disagree_button, bg_terms_and_conditions_label

    pronoun_label.place_forget()
    pronoun_dropdown.place_forget()
    pronoun_entry.place_forget()
    submit_button.place_forget()
    bg_pronoun_label.place_forget()

    bg_terms_and_conditions_label = tk.Label(root, image=tc_image)
    bg_terms_and_conditions_label.place(x=0, y=0, relwidth=1, relheight=1)

    terms_and_conditions_text = ("Terms and Conditions:\n"
                                 "\n"
                                 "1. This application is intended as a supplementary aid and should not replace professional medical advice.\n"
                                 "\n"
                                 "2. Consult a doctor or healthcare provider for any medical concerns or questions.\n"
                                 "3. This program does not assume responsibility for any outcomes resulting from the use of this application.\n"
                                 "\n"
                                 "4. This application is not suitable for emergency medical situations. In case of an emergency, please contact emergency services immediately.\n"
                                 "\n"
                                 "5. The information provided in this application may not be up-to-date or complete. Always verify with a healthcare professional.\n"
                                 "\n"
                                 "6. Any medication dosages and schedules recommended by this application should be double-checked with a healthcare provider.\n"
                                 "\n"
                                 "7. The developers of this application reserve the right to make updates and changes to the terms and conditions at any time.\n"
                                 "\n"
                                 "Please read the terms and conditions carefully."
                                 )

    terms_and_conditions_label = tk.Label(root,
                           text=f"Thank you for filling in {name}'s personal information.\n\n{terms_and_conditions_text}",
                           font="Helvetica 14",
                           bg=theme_color,
                           justify="left",
                           wraplength=400,
                           pady=20)
    terms_and_conditions_label.place(x=400, y=20)

    agree_button = tk.Button(root, text="Agree and Proceed", bg=button_color, font=button_font, command=create_logo_background)
    agree_button.place(x=400, y=520)

    disagree_button = tk.Button(root, text="Disagree", bg=button_color, font=button_font, command=disagree_warning)
    disagree_button.place(x=630, y=520)


def disagree_warning():
    messagebox.showwarning("Disagree", "You must agree to the terms and conditions to proceed.")


#create a constant background under each subpage
def create_logo_background():
    bg_logo_label = tk.Label(root, image=logo_image)
    bg_logo_label.place(x=0, y=0, relwidth=1, relheight=1)

    create_homepage()


def create_homepage():
    global home_frame, home_label

    terms_and_conditions_label.place_forget()
    agree_button.place_forget()
    disagree_button.place_forget()

    home_frame = tk.Frame(root, width=mainpage_frame_width, height=mainpage_frame_height)
    home_frame.place(x=0, y=0, relwidth=1, relheight=1)

    bg_homepage_label = tk.Label(home_frame, image=homepage_image)
    bg_homepage_label.place(x=0, y=0, relwidth=1, relheight=1)

    # All the Buttons on the homepage (image settings are placed at the end of the code)
    button_knowledge = tk.Button(home_frame, image=book_image, command=create_knowledge_page)
    button_knowledge.place(x=mainpage_frame_width-208, y=0)

    button_medicine = tk.Button(home_frame, image=medicine_image, command=create_medicine_page)
    button_medicine.place(x=mainpage_frame_width-200, y=mainpage_frame_height-172)

    button_temperature = tk.Button(home_frame, image=thermometer_image, command=create_temperature_page)
    button_temperature.place(x=84, y=171)

    button_doctor = tk.Button(home_frame, image=stethoscope_image, command=create_doctor_page)
    button_doctor.place(x=342, y=505)

    button_export = tk.Button(home_frame, image=printer_image, command=export_confirmation)
    button_export.place(x=0, y=460)


def create_temperature_page():
    global temp_frame, temp_entry, temp_date_entry, temp_time_entry, submit_temp_button, temp_listbox

    home_frame.place_forget()

    temp_frame = tk.Frame(root, bg=theme_color)
    root.minsize(width=subpage_frame_width, height=subpage_frame_height)
    temp_frame.grid(column=1, row=0, rowspan=2, padx=10, pady=10, sticky="ne")

    return_button = tk.Button(temp_frame, text="🏠", font=button_font, width=5, height=2,
                              command=return_to_homepage_from_temp)
    return_button.grid(column=0, row=0, sticky=tk.S+tk.W, columnspan=2, pady=10)

    canvas = tk.Canvas(temp_frame, width=scrollable_frame_width, height=scrollable_frame_height, bg=theme_color)
    canvas.grid(row=1, column=0, sticky="nsew")

    v_scrollbar = tk.Scrollbar(temp_frame, orient="vertical", command=canvas.yview)
    v_scrollbar.grid(row=1, column=1, sticky="ns")
    h_scrollbar = tk.Scrollbar(temp_frame, orient="horizontal", command=canvas.xview)
    h_scrollbar.grid(row=2, column=0, sticky="ew")

    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    scrollable_frame = tk.Frame(canvas, bg=theme_color)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    # Create a window inside the canvas on which the scrollable frame will be displayed
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    temp_label = tk.Label(scrollable_frame, text="Body Temperature 🌡️", font=subpage_title_font, pady=20, bg=theme_color)
    temp_label.grid(column=0, row=0, sticky=tk.W)

    temperature_tracker_label = tk.Label(scrollable_frame, text="\nBody Temperature Tracker", font="Helvetica 25 bold", bg=theme_color)
    temperature_tracker_label.grid(column=0, row=1, columnspan=2, sticky=tk.W, pady=10)

    temp_entry_label = tk.Label(scrollable_frame, text="Enter body temperature (°C):", font=label_font, bg=theme_color)
    temp_entry_label.grid(column=0, row=2, sticky=tk.W)
    temp_entry = tk.Entry(scrollable_frame, font=label_font)
    temp_entry.grid(column=1, row=2, sticky=tk.W, pady=10)

    temp_date_label = tk.Label(scrollable_frame, text="Date of measurement:", font=label_font, bg=theme_color)
    temp_date_label.grid(column=0, row=3, sticky=tk.W)
    temp_date_entry = DateEntry(scrollable_frame, font=label_font)
    temp_date_entry.grid(column=1, row=3, sticky=tk.W, pady=10)

    temp_time_label = tk.Label(scrollable_frame, text="Time of measurement (HH:MM):", font=label_font, bg=theme_color)
    temp_time_label.grid(column=0, row=4, sticky=tk.W)
    temp_time_entry = tk.Entry(scrollable_frame, font=label_font)
    temp_time_entry.grid(column=1, row=4, sticky=tk.W, pady=10)

    c = datetime.now()
    current_time = c.strftime("%H:%M")
    current_time_button = tk.Button(scrollable_frame, text="set current time", bg=button_color,
                                    font=button_font,
                                    command=lambda: set_current_time_entry_temp(current_time)
                                    )
    current_time_button.grid(column=1, row=5, sticky=tk.W, columnspan=2, pady=0)

    submit_temp_button = tk.Button(scrollable_frame, text="Add to list", bg=button_color, font=button_font,
                                   command=submit_temperature)
    submit_temp_button.grid(column=0, row=6, sticky=tk.W, columnspan=2, pady=20)

    # Listbox to show recorded temperatures
    temp_listbox_label = tk.Label(scrollable_frame, text="Recorded Temperatures:", font=label_font)
    temp_listbox_label.grid(column=0, row=8, sticky=tk.W)
    temp_listbox = tk.Listbox(scrollable_frame, font=label_font, width=50)
    temp_listbox.grid(column=0, row=8, sticky=tk.W, columnspan=2, pady=10)

    # Populate the Listbox with existing records
    for record in temperature_record_list:
        temp_listbox.insert(tk.END, record)


def submit_temperature():
    global temp_listbox
    temperature = temp_entry.get()
    measure_date = temp_date_entry.get()
    measure_time = temp_time_entry.get()

    try:
        temperature = float(temperature)
        # Check if temperature is within the valid range (20 to 50°C)
        if 20 <= temperature <= 50:
            record = f"Temperature: {temperature}°C - Date: {measure_date} - Time: {measure_time}"
            temperature_record_list.append(record)
            temp_listbox.insert(tk.END, record)
            messagebox.showinfo("Temperature Recorded", record)
        else:
            messagebox.showerror("Invalid Input", "Temperature must be between 20°C and 50°C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for temperature")

    temp_entry.delete(0, tk.END)  # Clear the entry after submission


def set_current_time_entry_temp(text):
    temp_time_entry.delete(0,tk.END)
    temp_time_entry.insert(0,text)


def return_to_homepage_from_temp():
    global home_frame

    temp_frame.grid_forget()
    #Show the homepage again
    home_frame.place(x=0, y=0, relwidth=1, relheight=1)


def create_medicine_page():
    global med_frame, med_dropdown, med_amount_entry, med_date_entry, med_time_entry, submit_med_button, med_listbox, current_time

    home_frame.place_forget()

    med_frame = tk.Frame(root, bg=theme_color)
    root.minsize(width=subpage_frame_width, height=subpage_frame_height)
    med_frame.grid(column=1, row=0, rowspan=2, padx=10, pady=10, sticky="ne")

    return_button = tk.Button(med_frame, text="🏠", font=button_font, width=5, height=2,
                              command=return_to_homepage_from_med)
    return_button.grid(column=0, row=0, sticky=tk.S + tk.W, columnspan=2, pady=10)

    canvas = tk.Canvas(med_frame, width=scrollable_frame_width, height=scrollable_frame_height, bg=theme_color)
    canvas.grid(row=1, column=0, sticky="nsew")

    # Add vertical and horizontal scrollbars to the canvas
    v_scrollbar = tk.Scrollbar(med_frame, orient="vertical", command=canvas.yview)
    v_scrollbar.grid(row=1, column=1, sticky="ns")
    h_scrollbar = tk.Scrollbar(med_frame, orient="horizontal", command=canvas.xview)
    h_scrollbar.grid(row=2, column=0, sticky="ew")

    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    scrollable_frame = tk.Frame(canvas, bg=theme_color)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Medicine page label
    med_label = tk.Label(scrollable_frame, text="Medicine Intake 💊", font=subpage_title_font, pady=20, bg=theme_color)
    med_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)

    instruction_text = (
        "Disclaimer:\n"
        "1. This program does not provide instructions on medicine intake for children under 6.\n"
        "2. Please consult physicians if you are pregnant, have a catastrophic illness, a family disease, or a chronic disease.\n"
        "3. Dosage may differ between different brands. Please refer to the package inserts from the manufacturers.\n"
        "4. The information below is for reference only. Regulations differ from country to country.\n"
        "5. Please read the dosage instructions below before taking the medicine."
    )
    instruction_label = tk.Label(scrollable_frame, text=instruction_text, font=label_font, justify="left", wraplength=800, bg=theme_color)
    instruction_label.grid(column=0, row=1, columnspan=2, sticky=tk.W, pady=10)

    treeview_frame = tk.Frame(scrollable_frame)
    treeview_frame.grid(column=0, row=3, columnspan=2, sticky=tk.W)

    #To be able to adjust the rowheight of the treeview
    style = ttk.Style()
    style.configure("Treeview", rowheight=80)

    treeview = ttk.Treeview(treeview_frame, columns=("#1", "#2", "#3", "#4"))

    treeview.column("#0", width=330)
    treeview.heading("#0", text="Medicine Name")

    treeview.column("#1", width=310)
    treeview.heading("#1", text="Single Dose")

    treeview.column("#2", width=130)
    treeview.heading("#2", text="Dose Interval")

    treeview.column("#3", width=300)
    treeview.heading("#3", text="Maximum Self-care Intake")

    treeview.column("#4", width=1100)
    treeview.heading("#4", text="Source")

    paracetamol_adult_source = ("https://www.nhs.uk/medicines/paracetamol-for-adults/how-and-when-to-take-paracetamol-for-adults/")
    ibuprofen_adult_source = ("1. https://www.nhs.uk/medicines/ibuprofen-for-adults/how-and-when-to-take-ibuprofen/#:~:text=The%20usual%20dose%20for%20adults,under%20supervision%20of%20a%20doctor.\n"
                             "2. https://www.nhs.uk/medicines/ibuprofen-for-adults/about-ibuprofen-for-adults/\n"
                             "3. https://www.nhs.uk/medicines/ibuprofen-for-adults/about-ibuprofen-for-adults/"
                              )
    aspirin_adult_source = ("1. https://www.nhs.uk/medicines/aspirin-for-pain-relief/how-and-when-to-take-aspirin-for-pain-relief/\n"
                            "2. DOI: 10.1007/s40268-016-0138-8"
                            )
    paracetamol_teen_source = ("1. https://www.nhs.uk/medicines/paracetamol-for-adults/how-and-when-to-take-paracetamol-for-adults/\n"
                               "2. https://www.event.panadol.com.tw/download/Film-coated.pdf"
                               )
    ibuprofen_teen_source = ("1. https://www.nhs.uk/medicines/ibuprofen-for-adults/how-and-when-to-take-ibuprofen/#:~:text=The%20usual%20dose%20for%20adults,under%20supervision%20of%20a%20doctor.\n"
                             "2. https://mcp.fda.gov.tw/fileshow/trans05064e4621a0-b2b2-4150-8a8d-7e21b63ddf45\n"
                             "3. https://www.nhs.uk/medicines/ibuprofen-for-adults/about-ibuprofen-for-adults/"
                              )
    aspirin_teen_source = ("1. https://www.mayoclinic.org/diseases-conditions/reyes-syndrome/symptoms-causes/syc-20377255\n"
                           "2. https://chrc.nhri.edu.tw/professionals/files/%E8%A1%9B%E6%95%992.pdf"
                           )

    paracetamol_child_source = ("1. https://www.nhs.uk/medicines/paracetamol-for-children/how-and-when-to-give-paracetamol-for-children/\n"
                                "2. https://www.event.panadol.com.tw/download/Film-coated.pdf\n"
                                "3. https://www.hch.gov.tw/?aid=626&pid=81&page_name=detail&iid=949"
                                )
    ibuprofen_child_source = ("1. https://www.nhs.uk/medicines/ibuprofen-for-children/how-and-when-to-give-ibuprofen-for-children/\n"
                              "2. https://mcp.fda.gov.tw/fileshow/trans05064e4621a0-b2b2-4150-8a8d-7e21b63ddf45\n"
                              "3. https://www.nhs.uk/medicines/ibuprofen-for-children/about-ibuprofen-for-children/\n"
                              "4. https://www.hch.gov.tw/?aid=626&pid=81&page_name=detail&iid=949"
                              )
    aspirin_child_source = ("1. https://www.mayoclinic.org/diseases-conditions/reyes-syndrome/symptoms-causes/syc-20377255\n"
                            "2. https://chrc.nhri.edu.tw/professionals/files/%E8%A1%9B%E6%95%992.pdf"
                            )


    #The "values" here counts from #1 instead of #0
    instruction_adult = treeview.insert("",
                                  tk.END,
                                  text="Dosage Instructions for ADULTS over 18\n"
                                       "(tablets, oral routes)",
                                  )
    paracetamol_adult = treeview.insert(instruction_adult,tk.END,
                                  text="Paracetamol (Acetaminophen)",
                                  values=("500mg/tablet, 1~2 tablets", "Every 4~6 hours", "4000mg per 24 hours.", paracetamol_adult_source)
                                  )
    ibuprofen_adult = treeview.insert(instruction_adult,
                                  tk.END,
                                  text="Ibuprofen",
                                  values=("200mg/tablet, 1~2 tablets", "Every 4~6 hours", "1200mg per 24 hours.", ibuprofen_adult_source)
                                  )

    aspirin_adult = treeview.insert(instruction_adult,
                                      tk.END,
                                      text="Aspirin",
                                      values=("300mg/tablet, 1~2 tablets", "Every 4~6 hours", "3000~4000mg per 24 hours", aspirin_adult_source)
                                    )

    instruction_teen = treeview.insert("",
                                        tk.END,
                                        text="Dosage Instructions for TEENAGERS Aged 11 to 17\n"
                                             "(tablets, oral routes)",
                                        )
    paracetamol_teen = treeview.insert(instruction_teen,
                                        tk.END,
                                        text="Paracetamol (Acetaminophen)",
                                        values=("500mg/tablet, 1~2 tablets", "Every 4~6 hours", "4000mg per 24 hours", paracetamol_teen_source)
                                        )
    ibuprofen_teen = treeview.insert(instruction_teen,
                                      tk.END,
                                      text="Ibuprofen",
                                      values=("200mg/tablet, 1~2 tablets", "Every 4~6 hours", "1200mg per 24 hours", ibuprofen_teen_source)
                                      )
    aspirin_teen = treeview.insert(instruction_teen,
                                    tk.END,
                                    text="Aspirin",
                                    values=("Should NOT be given to childrens and teenagers\n"
                                            "under 18 as it may cause Reye's syndrome\n"
                                            "(unless recommended by physicians).", "-", "-",aspirin_teen_source)
                                    )

    instruction_child = treeview.insert("",
                                        tk.END,
                                        text="Dosage Instructions for CHILDREN Aged 6 to 11\n"
                                             "(unit: mg. oral routes)",
                                        )
    paracetamol_child = treeview.insert(instruction_child,
                                        tk.END,
                                        text="Paracetamol (Acetaminophen)",
                                        values=("10~15mg/kg/dose.\n"
                                                "Please note the units of measurement.", "Every 4~6 hours", "4 times per 24 hours. No longer than 3 days", paracetamol_child_source)
                                        )
    ibuprofen_child = treeview.insert(instruction_child,
                                      tk.END,
                                      text="Ibuprofen",
                                      values=("5~10mg/kg/dose.\n"
                                              "Please note the units of measurement.", "Every 6~8 hours", "4 times per 24 hours. No longer than 3 days", ibuprofen_child_source)
                                      )

    aspirin_child = treeview.insert(instruction_child,
                                    tk.END,
                                    text="Aspirin",
                                    values=("Should NOT be given to childrens and teenagers\n"
                                            "under 18 as it may cause Reye's syndrome\n"
                                            "(unless recommended by physicians).", "-", "-", aspirin_child_source)
                                    )
    treeview.pack(fill="both", expand=True)

    medication_tracker_frame = tk.Frame(scrollable_frame, bg=theme_color)
    medication_tracker_frame.grid(column=0, row=4, columnspan=2, sticky=tk.W)

    medication_tracker_label = tk.Label(medication_tracker_frame, text="\nMedication Tracker", font="Helvetica 25 bold", bg=theme_color)
    medication_tracker_label.grid(column=0, row=4, columnspan=2, sticky=tk.W, pady=10)

    med_options = ["Paracetamol (Acetaminophen)", "Ibuprofen", "Aspirin"]
    med_var = tk.StringVar(medication_tracker_frame)
    med_var.set(med_options[0])
    med_dropdown_label = tk.Label(medication_tracker_frame, text="Select Medicine:", font=label_font, bg=theme_color)
    med_dropdown_label.grid(column=0, row=5, sticky=tk.W)
    med_dropdown = tk.OptionMenu(medication_tracker_frame, med_var, *med_options)
    med_dropdown.config(font=label_font)
    med_dropdown.grid(column=1, row=5, sticky=tk.W, pady=10)

    med_amount_label = tk.Label(medication_tracker_frame, text="Enter amount taken (mg):", font=label_font, bg=theme_color)
    med_amount_label.grid(column=0, row=6, sticky=tk.W)
    med_amount_entry = tk.Entry(medication_tracker_frame, font=label_font)
    med_amount_entry.grid(column=1, row=6, sticky=tk.W, pady=10)

    med_date_label = tk.Label(medication_tracker_frame, text="Date of intake:", font=label_font, bg=theme_color)
    med_date_label.grid(column=0, row=7, sticky=tk.W)
    med_date_entry = DateEntry(medication_tracker_frame, font=label_font)
    med_date_entry.grid(column=1, row=7, sticky=tk.W, pady=10)

    med_time_label = tk.Label(medication_tracker_frame, text="Time of intake (HH:MM):", font=label_font, bg=theme_color)
    med_time_label.grid(column=0, row=8, sticky=tk.W)
    med_time_entry = tk.Entry(medication_tracker_frame, font=label_font)
    med_time_entry.grid(column=1, row=8, sticky=tk.W, pady=0)

    c = datetime.now()
    current_time = c.strftime("%H:%M")
    current_time_button = tk.Button(medication_tracker_frame, text="set current time", bg=button_color, font=button_font,
                                    command=lambda: set_current_time_entry_med(current_time)
                                    )
    current_time_button.grid(column=1, row=9, sticky=tk.W, columnspan=2, pady=0)

    submit_med_button = tk.Button(medication_tracker_frame, text="Add to list", bg=button_color, font=button_font,
                                  command=lambda: submit_medicine(med_var.get()))
    submit_med_button.grid(column=0, row=10, sticky=tk.W, columnspan=2, pady=20)

    med_listbox_label = tk.Label(medication_tracker_frame, text=f"{name}'s medicine intake record:", font="Helvetica 16 bold", bg=theme_color)
    med_listbox_label.grid(column=0, row=11, sticky=tk.W)
    med_listbox = tk.Listbox(medication_tracker_frame, font=label_font, width=70)
    med_listbox.grid(column=0, row=12, sticky=tk.W, columnspan=2, pady=10)

    # Put existing records on the list to the list box
    for record in medicine_record_list:
        med_listbox.insert(tk.END, record)

    # Give special warning to some of the patients
    if weight < 50 and age_years >= 18:
        messagebox.showinfo("Warning", f"{name} is an adult but weighs less than 50kg. Please consult doctors or pharmacists about the dosage.")

    if age_years < 6:
        messagebox.showinfo("Warning",
                            f"{name} is under 6 years old. Please consult doctors or pharmacists about the dosage.")

    if age_years < 18:
        messagebox.showinfo("Warning",
                            f"{name} is under 18 years old. Please DO NOT take Aspirin or salicylate-containing medicine unless recommended by a physician.")


def set_current_time_entry_med(text):
    med_time_entry.delete(0,tk.END)
    med_time_entry.insert(0,text)


def submit_medicine(medicine):
    global med_listbox
    amount = med_amount_entry.get()
    intake_date = med_date_entry.get()
    intake_time = med_time_entry.get()

    try:
        amount = float(amount)
        # Check if amount is within the valid range (no more than 2000mg)
        if amount <= 2000:
            record = f"Medicine: {medicine} - Amount: {amount}mg - Date: {intake_date} - Time: {intake_time}"
            medicine_record_list.append(record)
            med_listbox.insert(tk.END, record)
            messagebox.showinfo("Medicine Recorded", record)
        else:
            messagebox.showerror("Invalid Input", "Medicine amount cannot exceed 2000mg")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for medicine amount")

    med_amount_entry.delete(0, tk.END)  # Clear the entry after submission


def return_to_homepage_from_med():
    med_frame.grid_forget()
        # Show home page widgets
    home_frame.place(x=0, y=0, relwidth=1, relheight=1)


def create_knowledge_page():
    global know_frame, about_medicine_frame, image_frame, famous_diseases_frame, image_frame

    home_frame.place_forget()

    know_frame = tk.Frame(root, bg=theme_color)
    root.minsize(width=subpage_frame_width, height=subpage_frame_height)
    know_frame.grid(column=1, row=0, rowspan=2, padx=10, pady=10, sticky="ne")

    canvas = tk.Canvas(know_frame, width=scrollable_frame_width, height=scrollable_frame_height, bg=theme_color)
    canvas.grid(row=1, column=0, sticky="nsew")

    v_scrollbar = tk.Scrollbar(know_frame, orient="vertical", command=canvas.yview)
    v_scrollbar.grid(row=1, column=1, sticky="ns")
    h_scrollbar = tk.Scrollbar(know_frame, orient="horizontal", command=canvas.xview)
    h_scrollbar.grid(row=2, column=0, sticky="ew")

    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    scrollable_frame = tk.Frame(canvas, bg=theme_color)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    return_button = tk.Button(know_frame, text="🏠", font=button_font, width=5, height=2,
                              command=return_to_homepage_from_know)
    return_button.grid(column=0, row=0, sticky=tk.S + tk.W, columnspan=2, pady=10)

    know_label = tk.Label(scrollable_frame, text="Medical Knowledge 📚", font=subpage_title_font, pady=20,
                          bg=theme_color)
    know_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)

    button_frame = tk.Frame(scrollable_frame, bg=theme_color)
    button_frame.grid(column=0, row=1, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

    # for buttons under "About Medicine"
    about_medicine_frame = tk.Frame(button_frame, bg=theme_color)
    # for buttons under "Famous Fever-causing Diseases"
    famous_diseases_frame = tk.Frame(button_frame, bg=theme_color)
    # for showing the infographic images
    image_frame = tk.Frame(scrollable_frame, bg=theme_color)


    def show_acetaminophen_vs_ibuprofen():
        global image_frame
        image_frame.destroy()
        image_frame = tk.Frame(scrollable_frame, bg=theme_color)
        image_frame.grid(column=1, row=1, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

        acetaminophen_vs_ibuprofen_label = tk.Label(image_frame, image=acetaminophen_vs_ibuprofen_image, bg=theme_color)
        acetaminophen_vs_ibuprofen_label.grid(column=0, row=0, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

    def show_myths_about_medicine():
        global image_frame
        image_frame.destroy()
        image_frame = tk.Frame(scrollable_frame, bg=theme_color)
        image_frame.grid(column=1, row=1, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

        myths_about_medicine_label = tk.Label(image_frame, image=myths_image, bg=theme_color)
        myths_about_medicine_label.grid(column=0, row=0, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

    def show_hide_about_medicine():
        global pressed_about_medicine, about_medicine_frame

        if pressed_about_medicine:
            about_medicine_frame.grid(column=0, row=1, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

            paracetamol_vs_ibuprofen_button = tk.Button(about_medicine_frame, text="Paracetamol vs. Ibuprofen",
                                                        font=label_font, pady=20, bg="white", width=30, anchor="center",
                                                        command=show_acetaminophen_vs_ibuprofen)
            paracetamol_vs_ibuprofen_button.grid(column=0, row=0, columnspan=10, sticky=tk.W)

            myths_about_medicine_button = tk.Button(about_medicine_frame, text="Myths about Medicine ",
                                                   font=label_font, pady=20, bg="white", width=30, anchor="center",
                                                    command=show_myths_about_medicine)
            myths_about_medicine_button.grid(column=0, row=1, columnspan=10, sticky=tk.W)

            pressed_about_medicine = False

        else:
            about_medicine_frame.grid_forget()
            image_frame.grid_forget()
            pressed_about_medicine = True


    def show_gastroenteritis():
        global image_frame
        image_frame.destroy()
        image_frame = tk.Frame(scrollable_frame, bg=theme_color)
        image_frame.grid(column=1, row=1, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

        gastroenteritis_label = tk.Label(image_frame, image=gastroenteritis_image, bg=theme_color)
        gastroenteritis_label.grid(column=0, row=0, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

    def show_rheumatic_fever():
        global image_frame
        image_frame.destroy()
        image_frame = tk.Frame(scrollable_frame, bg=theme_color)
        image_frame.grid(column=1, row=1, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

        rheumatic_fever_label = tk.Label(image_frame, image=rheumatic_fever_image, bg=theme_color)
        rheumatic_fever_label.grid(column=0, row=0, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

    def show_dengue_fever():
        global image_frame
        image_frame.destroy()
        image_frame = tk.Frame(scrollable_frame, bg=theme_color)
        image_frame.grid(column=1, row=1, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

        dengue_fever_label = tk.Label(image_frame, image=dengue_fever_image, bg=theme_color)
        dengue_fever_label.grid(column=0, row=0, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")


    def show_hide_famous_diseases():
        global pressed_famous_diseases, famous_diseases_frame

        if pressed_famous_diseases:
            famous_diseases_frame.grid(column=0, row=4, rowspan=2, padx=10, pady=5, ipadx=10, sticky="ne")

            gastroenteritis_button = tk.Button(famous_diseases_frame, text="Gastroenteritis",
                                               font=label_font, pady=20, bg="white", width=30, anchor="center",
                                               command=show_gastroenteritis)
            gastroenteritis_button.grid(column=0, row=0, columnspan=10, sticky=tk.W)

            rheumatic_fever_button = tk.Button(famous_diseases_frame, text="Rheumatic Fever",
                                               font=label_font, pady=20, bg="white", width=30, anchor="center",
                                               command=show_rheumatic_fever)
            rheumatic_fever_button.grid(column=0, row=1, columnspan=10, sticky=tk.W)

            dengue_fever_button = tk.Button(famous_diseases_frame, text="Dengue Fever",
                                            font=label_font, pady=20, bg="white", width=30, anchor="center",
                                            command=show_dengue_fever)
            dengue_fever_button.grid(column=0, row=2, columnspan=10, sticky=tk.W)

            pressed_famous_diseases = False

        else:
            famous_diseases_frame.grid_forget()
            image_frame.grid_forget()
            pressed_famous_diseases = True


    about_medicine_button = tk.Button(button_frame, text="About Medicine💊", font=button_font, pady=5, bg=theme_color,
                                     command=show_hide_about_medicine)
    about_medicine_button.grid(column=0, row=0, columnspan=2, sticky=tk.W)

    famous_diseases_button = tk.Button(button_frame, text="Famous Fever-Causing Diseases🌡️", font=button_font, pady=5, bg=theme_color,
                                     command=show_hide_famous_diseases)
    famous_diseases_button.grid(column=0, row=3, columnspan=2, sticky=tk.W)


def return_to_homepage_from_know():
    know_frame.grid_forget()
    home_frame.place(x=0, y=0, relwidth=1, relheight=1)


def create_doctor_page():
    global doctor_frame, doctor_smart_scrollable_frame

    home_frame.place_forget()

    doctor_frame = tk.Frame(root, bg=theme_color)
    root.minsize(width=subpage_frame_width, height=subpage_frame_height)
    doctor_frame.grid(column=1, row=0, rowspan=2, padx=10, pady=10, sticky="ne")

    return_button = tk.Button(doctor_frame, text="🏠", font=button_font, width=5, height=2,
                              command=return_to_homepage_from_doctor)
    return_button.grid(column=0, row=0, sticky=tk.S+tk.W, columnspan=2, pady=10)

    canvas = tk.Canvas(doctor_frame, width=scrollable_frame_width, height=scrollable_frame_height, bg=theme_color)
    canvas.grid(row=1, column=0, sticky="nsew")

    v_scrollbar = tk.Scrollbar(doctor_frame, orient="vertical", command=canvas.yview)
    v_scrollbar.grid(row=1, column=1, sticky="ns")
    h_scrollbar = tk.Scrollbar(doctor_frame, orient="horizontal", command=canvas.xview)
    h_scrollbar.grid(row=2, column=0, sticky="ew")

    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    doctor_smart_scrollable_frame = tk.Frame(canvas, bg=theme_color)
    doctor_smart_scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=doctor_smart_scrollable_frame, anchor="nw")


    doctor_label = tk.Label(doctor_smart_scrollable_frame, text="Dr. Smart 🩺", font=subpage_title_font, pady=20, bg=theme_color)
    doctor_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)

    patient_info_text = (f"Dr. Smart gives different suggestions based on the age provided. {name} is {age_export}.\n"
                         f"By filling in the information below, Dr. Quick will tell you whether {name} should go see a doctor.")
    patient_info_label = tk.Label(doctor_smart_scrollable_frame, text=patient_info_text, font=label_font, pady=20, bg=theme_color, justify="left")
    patient_info_label.grid(column=0, row=1, columnspan=2, sticky=tk.W)

    doctor_smart_temp_entry_label = tk.Label(doctor_smart_scrollable_frame, text=f"Enter {name}'s body temperature (°C):", font=label_font, bg=theme_color)
    doctor_smart_temp_entry_label.grid(column=0, row=2, sticky=tk.W)
    doctor_smart_temp_entry = tk.Entry(doctor_smart_scrollable_frame, font=label_font)
    doctor_smart_temp_entry.grid(column=1, row=2, sticky=tk.W, pady=10)

    duration_options = ["<24 hours", "1 day", "2 days", "3 days", "4 days", "5 days or above"]
    duration_var = tk.StringVar(doctor_smart_scrollable_frame)
    duration_var.set("(please select)")
    duration_dropdown_label = tk.Label(doctor_smart_scrollable_frame, text=f"How long has {name} had a fever?",font=label_font, bg=theme_color)
    duration_dropdown_label.grid(column=0, row=3, sticky=tk.W)
    duration_dropdown = tk.OptionMenu(doctor_smart_scrollable_frame, duration_var, *duration_options)
    duration_dropdown.config(font=label_font)
    duration_dropdown.grid(column=1, row=3, sticky=tk.W, pady=10)

    medicine_effect_options = ["Yes, it was effective", "Yes, but the body temperature did not go down", "No, haven't taken any yet"]
    medicine_effect_var = tk.StringVar(doctor_smart_scrollable_frame)
    medicine_effect_var.set("(please select)")
    medicine_effect_dropdown_label = tk.Label(doctor_smart_scrollable_frame, text=f"Did {name} take fever-reducing medicine? What was the effect?", font=label_font,
                                       bg=theme_color)
    medicine_effect_dropdown_label.grid(column=0, row=4, sticky=tk.W, pady=10)
    medicine_effect_dropdown = tk.OptionMenu(doctor_smart_scrollable_frame, medicine_effect_var, *medicine_effect_options)
    medicine_effect_dropdown.config(font=label_font)
    medicine_effect_dropdown.grid(column=1, row=4, sticky=tk.W, pady=10)

    submit_button = tk.Button(doctor_smart_scrollable_frame, text="Submit", bg=button_color, font=button_font,
                              command=lambda: submit_doctor_smart(doctor_smart_temp_entry.get(), duration_var.get(), medicine_effect_var.get()))
    submit_button.grid(column=0, row=5, sticky=tk.W, columnspan=2, pady=20)

    doctor_smart_reference_text = "Reference for the medical information used on this page:\n" \
                                  "1. https://newsroom.clevelandclinic.org/2023/04/11/when-to-give-your-child-fever-reducing-medication\n" \
                                  "2. https://my.clevelandclinic.org/health/symptoms/10880-fever\n" \
                                  "3. https://www.msdmanuals.com/home/infections/biology-of-infectious-disease/fever-in-adults\n" \
                                  "4. https://health.clevelandclinic.org/kids-fevers-when-to-worry-when-to-relax\n" \
                                  "5. https://www.mayoclinic.org/diseases-conditions/fever/symptoms-causes/syc-20352759\n"
    doctor_smart_reference_label = tk.Label(doctor_smart_scrollable_frame, text=doctor_smart_reference_text,font=reference_font, bg=theme_color, justify="left")
    doctor_smart_reference_label.grid(column=0, row=8, sticky=tk.W, columnspan=2, pady=20)

def return_to_homepage_from_doctor():
    doctor_frame.grid_forget()
        # Show home page widgets
    home_frame.place(x=0, y=0, relwidth=1, relheight=1)


def submit_doctor_smart(temperature, duration, medicine_effect):

    temperature = float(temperature)
    medicine_effect = str(medicine_effect)

    if duration == "<24 hours":
        duration = 0
    elif duration == "1 day":
        duration = 1
    elif duration == "2 days":
        duration = 2
    elif duration == "3 days":
        duration = 3
    elif duration == "4 days":
        duration = 4
    elif duration == "5 days or above":
        duration = 5

    print(temperature, duration, medicine_effect)

    doctor_smart_analyze(temperature, duration, medicine_effect)

def doctor_smart_analyze(temperature, duration, medicine_effect):
    fever_temperature = 38.0

    if temperature >= fever_temperature:

        if age_years <= 0 and age_months < 3:  # Infants under 3 months
            give_suggestion_emergency()

        elif age_years <= 0 and age_months >= 3 and age_months <= 6:  # Infants 3 to 6 months
            if temperature > 38.9:
                give_suggestion_emergency()
            elif temperature <= 38.9 and duration < 3:
                if medicine_effect == "No, haven't taken any yet":
                    give_suggestion_try_medication()
            else:
                check_general_conditions(temperature, duration, medicine_effect)

        elif age_years <= 0 and age_months > 6 and age_months <= 12:  # Infants 7 to 12 months
            if temperature > 38.9 and duration >= 1:
                give_suggestion_emergency()
            elif temperature >= 40:
                give_suggestion_emergency()
            elif duration < 3 and medicine_effect == "No, haven't taken any yet":
                give_suggestion_try_medication()
            else:
                check_general_conditions(temperature, duration, medicine_effect)

        elif age_years >= 1 and age_years <= 2:  # Toddlers 1 to 2 years
            if temperature > 38.9 and duration >= 1:
                give_suggestion_emergency()
            elif temperature >= 40:
                give_suggestion_emergency()
            elif duration < 3 and medicine_effect == "No, haven't taken any yet":
                give_suggestion_try_medication()
            else:
                check_general_conditions(temperature, duration, medicine_effect)

        elif age_years >= 3 and age_years < 12:  # Children 3 to 12 years
            if temperature >= 40:
                give_suggestion_emergency()
            elif duration < 3 and medicine_effect == "No, haven't taken any yet":
                give_suggestion_try_medication()
            else:
                check_general_conditions(temperature, duration, medicine_effect)

        elif age_years >= 12:  # Individuals 12 years and older
            if temperature >= 39.4:
                give_suggestion_emergency()
            elif duration < 3 and medicine_effect == "No, haven't taken any yet":
                give_suggestion_try_medication()
            else:
                check_general_conditions(temperature, duration, medicine_effect)

    else:
        give_no_fever_suggestion()

def check_general_conditions(temperature, duration, medicine_effect):
    # General Conditions (for all ages)
    if duration >= 3:
        give_suggestion_emergency()
    elif medicine_effect == "Yes, but the body temperature did not go down":
        give_suggestion_emergency()
    elif temperature < 38.3:
        give_suggestion_mild_fever()
    else:
        give_suggestion_stay_home()

def give_suggestion_mild_fever():
    suggestion_text = f"{name} has a mild fever. But no medication is needed yet."
    suggestion_color = "#D3D3D3"
    suggestion_label = tk.Label(doctor_smart_scrollable_frame, text=suggestion_text,font=suggestion_label_font, bg=suggestion_color,
                                width=suggestion_label_width, height=suggestion_label_height)
    suggestion_label.grid(column=0, row=6, sticky=tk.W, columnspan=2, pady=20)

def give_suggestion_emergency():
    suggestion_text = f"{name} should go see a doctor"
    suggestion_color = "#FF474C"
    suggestion_label = tk.Label(doctor_smart_scrollable_frame, text=suggestion_text,font=suggestion_label_font, bg=suggestion_color,
                                width=suggestion_label_width, height=suggestion_label_height)
    suggestion_label.grid(column=0, row=6, sticky=tk.W, columnspan=2, pady=20)

def give_suggestion_try_medication():
    suggestion_text = f"Please try taking some medicine first"
    suggestion_color = "yellow"
    suggestion_label = tk.Label(doctor_smart_scrollable_frame, text=suggestion_text,font=suggestion_label_font, bg=suggestion_color,
                                width=suggestion_label_width, height=suggestion_label_height)
    suggestion_label.grid(column=0, row=6, sticky=tk.W, columnspan=2, pady=20)

def give_suggestion_stay_home():
    suggestion_text = f"{name} can stay home. Stay hydrated"
    suggestion_color = "#90EE90"
    suggestion_label = tk.Label(doctor_smart_scrollable_frame, text=suggestion_text,font=suggestion_label_font, bg=suggestion_color,
                                width=suggestion_label_width, height=suggestion_label_height)
    suggestion_label.grid(column=0, row=6, sticky=tk.W, columnspan=2, pady=20)

def give_no_fever_suggestion():
    suggestion_text = f"{name} has a body temperature lower than the normal fever temperature"
    suggestion_color = "white"
    suggestion_label = tk.Label(doctor_smart_scrollable_frame, text=suggestion_text,font=suggestion_label_font, bg=suggestion_color,
                                width=suggestion_label_width, height=suggestion_label_height)
    suggestion_label.grid(column=0, row=6, sticky=tk.W, columnspan=2, pady=20)

#For the printer button
def export_confirmation():
    answer = askyesno(title="confirmation",
                      message=f"Are you sure that you want to export {name}'s personal information and records?")
    if answer:
        export_data()
def export_data():

    height_export = (f"{height}cm")
    weight_export = (f"{weight}kg")

    personal_info = {
        "Name": name,
        "Birthday (MM/DD/YY)": calendar.get(),
        "Age": age_export,
        "Height": height_export,
        "Weight": weight_export,
        "Sex assigned at birth": sex,
        "Gender Affirmation Surgery History": surgery,
        "Preferred Pronouns": pronoun
    }

    temperature_records = temp_listbox.get(0, tk.END)
    medicine_records = med_listbox.get(0, tk.END)

    data = f"Personal Information:\n{personal_info}\n\nTemperature Records:\n{temperature_records}\n\nMedicine Records:\n{medicine_records}"

    # Ask user for the file path to save
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(data)
            messagebox.showinfo("Data Exported", f"Patient data has been exported to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data.\nError: {str(e)}")



# Main application window
root = tk.Tk()
root.title("I HAVE A FEVER")
root.minsize(mainpage_frame_width, mainpage_frame_height)

#all the images
cover_image = Image.open('cover.png')
cover_image = cover_image.resize((mainpage_frame_width, mainpage_frame_height))
cover_image = ImageTk.PhotoImage(cover_image)

birthday_image = Image.open('birthday.png')
birthday_image = birthday_image.resize((mainpage_frame_width, mainpage_frame_height))
birthday_image = ImageTk.PhotoImage(birthday_image)

height_and_weight_image = Image.open('height_and_weight.png')
height_and_weight_image = height_and_weight_image.resize((mainpage_frame_width, mainpage_frame_height))
height_and_weight_image = ImageTk.PhotoImage(height_and_weight_image)

sex_image = Image.open('sex.png')
sex_image = sex_image.resize((mainpage_frame_width, mainpage_frame_height))
sex_image = ImageTk.PhotoImage(sex_image)

affirmation_image = Image.open('affirmation.png')
affirmation_image = affirmation_image.resize((mainpage_frame_width, mainpage_frame_height))
affirmation_image = ImageTk.PhotoImage(affirmation_image)

pronoun_image = Image.open('pronoun.png')
pronoun_image = pronoun_image.resize((mainpage_frame_width, mainpage_frame_height))
pronoun_image = ImageTk.PhotoImage(pronoun_image)

tc_image = Image.open('t&c.png')
tc_image = tc_image.resize((mainpage_frame_width, mainpage_frame_height))
tc_image = ImageTk.PhotoImage(tc_image)

homepage_image = Image.open('homepage.png')
homepage_image = homepage_image.resize((mainpage_frame_width, mainpage_frame_height))
homepage_image = ImageTk.PhotoImage(homepage_image)

medicine_image = Image.open('medicine.png')
medicine_image = medicine_image.resize((200,172)) #original: 256*221
medicine_image = ImageTk.PhotoImage(medicine_image)

printer_image = Image.open('printer.png')
printer_image = printer_image.resize((224, 164))
printer_image = ImageTk.PhotoImage(printer_image)

thermometer_image = Image.open('thermometer.png')
thermometer_image = thermometer_image.resize((156, 86))
thermometer_image = ImageTk.PhotoImage(thermometer_image)

book_image = Image.open('book.png')
book_image = book_image.resize((208, 220))
book_image = ImageTk.PhotoImage(book_image)

stethoscope_image = Image.open('stethoscope.png')
stethoscope_image = stethoscope_image.resize((138, 102))
stethoscope_image = ImageTk.PhotoImage(stethoscope_image)

logo_image = Image.open('logo.png')
logo_image = logo_image.resize((mainpage_frame_width, mainpage_frame_height))
logo_image = ImageTk.PhotoImage(logo_image)

# Images for the knowledge page
acetaminophen_vs_ibuprofen_image = Image.open('acetaminophen_vs_ibuprofen.jpg')
acetaminophen_vs_ibuprofen_image = acetaminophen_vs_ibuprofen_image.resize((500, 2224)) # original 600*2670
acetaminophen_vs_ibuprofen_image = ImageTk.PhotoImage(acetaminophen_vs_ibuprofen_image)

myths_image = Image.open('myths.png')
myths_image = myths_image.resize((520, 901)) # original 1040*1803
myths_image = ImageTk.PhotoImage(myths_image)

gastroenteritis_image = Image.open('gastroenteritis.jpg')
gastroenteritis_image = gastroenteritis_image.resize((500, 1106)) # original 800*1770
gastroenteritis_image = ImageTk.PhotoImage(gastroenteritis_image)

rheumatic_fever_image = Image.open('rheumatic_fever.jpg')
rheumatic_fever_image = rheumatic_fever_image.resize((500, 1338)) # original 800*2141
rheumatic_fever_image = ImageTk.PhotoImage(rheumatic_fever_image)

dengue_fever_image = Image.open('dengue_fever.jpg')
dengue_fever_image = dengue_fever_image.resize((500, 1217)) # original 800*1947
dengue_fever_image = ImageTk.PhotoImage(dengue_fever_image)




#The very first page (welcome page to with a name entry)
bg_cover_label = tk.Label(root, image=cover_image)
bg_cover_label.place(x=0, y=0, relwidth=1, relheight=1)

patient_name_label = tk.Label(root, text="Enter the patient's name", bg=theme_color, font=registration_font, pady=10,)
patient_name_label.place(x=566, y=485)

patient_name_entry = tk.Entry(root, font=registration_font)
patient_name_entry.place(x=566, y=530)

patient_name_button = tk.Button(root, text="Enter", bg=button_color, font=button_font, command=ask_birthday)
patient_name_button.place(x=820, y=530)


temp_listbox = tk.Listbox(root)
med_listbox = tk.Listbox(root)

root.mainloop()