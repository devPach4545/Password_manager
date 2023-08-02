import random
from tkinter import *
from tkinter import messagebox

def gen_pwd():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + \
                    [random.choice(symbols) for char in range(nr_symbols)] + \
                    [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pwd_entry.insert(0,password)

#------Save passowrd-------#
def save_data():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = pwd_entry.get()
    save = messagebox.askyesno(title="Would you like to save your details?",
                               message="The info you entered:" + "\nWebsite: " + website_data  +
                                       "\nEmail: " + email_data + "\nPassword: " + password_data)

    if save:
        with open("data.txt", "a") as file:
            file.write(website_data + " | " + email_data + " | " + password_data + "\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        pwd_entry.delete(0, END)
    else:
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        pwd_entry.delete(0, END)

    




#-----UI set up------
window = Tk()
window.title("Dev's Password manager")
window.config(padx=60, pady=60, bg="Orange")

# Create a canvas in the frame
canvas = Canvas(width=500, height=500, highlightthickness=0)

# Load the image
image_pic = PhotoImage(file="logo.png")
image_item = canvas.create_image(250, 250, image=image_pic)
canvas.grid(row=0, column=1)

# Adding the labels
website = Label(text="Website: ", font=("Times New Roman", 16), bg="Yellow", fg="Red")
website.grid(row=1, column=0 )
email = Label(text="Email_Id/Username: ", font=("Times New Roman", 16), bg="Yellow", fg="Red")
email.grid(row=2, column=0)
password = Label(text="Password: ", font=("Times New Roman", 16), bg="Yellow", fg="Red")
password.grid(row=3, column=0)

# Adding the entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=0,columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(0, "dhaivatpachchigar@gmail.com")
email_entry.grid(row=2, column=0,columnspan=2)

pwd_entry = Entry(width=35)
pwd_entry.grid(row=3, column=0,columnspan=2)


#adding buttons
generate_button = Button(text="Generate Password", font=("Times New Roman", 16), bg="White",width=21, fg="Black",command=gen_pwd)
generate_button.grid(row=3, column=2,columnspan=2)

add_button = Button(text="Add", font=("Times New Roman", 16), bg="White",  fg="Black", width=36, command=save_data)
add_button.grid(row=4, column=0, columnspan=4, padx=5, pady=5)
window.mainloop()
