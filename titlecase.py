
def title_case(f_name,l_name):
    if f_name=="" or l_name=="":
     return "You didn't provide valid inputs."


    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name}{formated_l_name}"


f_name=input("What is your first name?:")
l_name=input("What is your last name?:")

formated_string=title_case(f_name,l_name)
print(formated_string)

