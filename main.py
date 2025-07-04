import mysql.connector as db
import smtplib
import random
# from email.message import EmailMessage
# from dashboard import dashboard
# Connect to MySQL
mydb = db.connect(
    host="localhost",
    user="root",
    password="root",
    database="netflix_data_analysis",
    auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()

def user_auth():
    count = 0  # Initialize count to 0
    email = input("Enter your email to login: ")
    fetch_query = "SELECT * FROM reg_users WHERE email = %s;"
    mycursor.execute(fetch_query, (email,))
    result = mycursor.fetchone()
    if result:
        print("Login Successful!")
        import dashboard
        count = 1
    if count == 0:
        print("Login Error! Email not registered.")

print("#" * 88)
print("******************* Enter 1 to LOGIN or 2 to REGISTER for new users *******************")
print("#" * 88)

try:
    inp = int(input("Enter your choice: "))
except ValueError:
    print("Invalid input. Please enter 1 or 2.")
    exit()

if inp == 1:
    user_auth()
elif inp == 2:
    name = input("ENTER YOUR NAME: ")
    email = input("ENTER YOUR EMAIL: ")
    otp = str(random.randint(100000, 999999))
    # Check if the email is already registered
    check_query = "SELECT * FROM reg_users WHERE email = %s;"
    mycursor.execute(check_query, (email,))
    result = mycursor.fetchone()

    if result:
        print("❌ Error: This email is already registered. Please log in instead.")
        exit()

    SUBJECT = "OTP for Login"
    TEXT = (
        f"HEY {name}!\n\n"
        f"Your OTP for login is: {otp}\n\n"
        "Please enter the OTP for further verification.\n\n"
        "Thank you!"
    )

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('captainyagami08@gmail.com', 'rkhh brso fiex qpnh')  # Replace with your email and password
        message = f"Subject: {SUBJECT}\n\n{TEXT}"
        s.sendmail('captainyagami08@gmail.com', email, message)  # Replace '$$' with your sender email
        s.quit()
        print("An OTP was sent to the entered email address.")
    except Exception as e:
        print(f"Error sending email: {e}")
        exit()

    try:
        answer = int(input("Please enter the OTP for verification: "))
    except ValueError:
        print("Invalid OTP format.")
        exit()

    if answer == int(otp):
        insert_query = "INSERT INTO reg_users (name, email) VALUES (%s, %s);"
        mycursor.execute(insert_query, (name, email))
        mydb.commit()
        print("You have been successfully registered. Now please follow the instructions to login.")
        user_auth()
    else:
        print("Login failed. Incorrect OTP.")
else:
    print("Invalid selection. Please restart and choose 1 or 2.")