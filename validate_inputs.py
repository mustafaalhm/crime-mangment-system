from tkinter import messagebox


def validate_input_length(cr_no, cr_ccrime_type, cr_name, cr_nick, cr_father, cr_arrest, cr_d_crime, cr_address, cr_age, cr_occu, cr_mark, cr_gender, cr_wanted):

    if len(cr_no) == 0 or len(cr_name) == 0 or len(cr_nick) == 0 or len(cr_father) == 0 or len(cr_arrest) == 0 or len(cr_address) == 0 or len(cr_age) == 0 or len(cr_occu) == 0 or len(cr_mark) == 0 or len(cr_gender) == 0 or len(cr_wanted) == 0 or len(cr_d_crime) == 0 or len(cr_ccrime_type) == 0:

         messagebox.showinfo(title="Empty Field",
                        message="please complete all fields ")


# ,cr_father,cr_arrest,cr_address,cr_age,cr_occu,cr_mark,cr_gender,cr_wanted,cr_d_crime,cr_ccrime_type
