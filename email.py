import smtplib  # Module for sending emails via the Simple Mail Transfer Protocol (SMTP)
from email.mime.text import MIMEText  # For creating plain text email content
from email.mime.multipart import MIMEMultipart  # For creating email with multiple parts (e.g., text and attachments)
import os  # Module to interact with the operating system (used for environment variables)

# Function to send an email
def send_email(subject, body, to_email):
    """
    Sends an email with the specified subject and body to the given recipient email.
   
    Parameters:
        subject (str): The subject of the email.
        body (str): The content of the email.
        to_email (str): The recipient's email address.
    """
    # Fetch sender's email credentials from environment variables
    sender_email = os.getenv('EMAIL_ADDRESS')  # Your email address
    sender_password = os.getenv('EMAIL_PASSWORD')  # Your email password or app-specific password
   
    # Check if credentials are properly set
    if not sender_email or not sender_password:
        print("Error: Email credentials not set in environment variables.")
        return

    # The recipient's email address
    receiver_email = to_email

    # Create the email message
    msg = MIMEMultipart()  # Create a multipart email (supports text and attachments)
    msg['From'] = sender_email  # Set the sender's email address
    msg['To'] = receiver_email  # Set the recipient's email address
    msg['Subject'] = subject  # Set the email subject
    msg.attach(MIMEText(body, 'plain'))  # Attach the email body as plain text

    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server on port 587
        server.starttls()  # Start a TLS (Transport Layer Security) session to secure the connection
        server.login(sender_email, sender_password)  # Log in to the server with the sender's credentials
        server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
        server.quit()  # Close the connection to the server
        print("Email sent successfully!")  # Print a success message
    except Exception as e:
        # Catch and print any errors that occur
        print(f"Failed to send email: {e}")

# Main script to demonstrate email sending
if __name__ == "__main__":
    # Define the subject and body of the email
    subject = 'Monthly Report'
    body = 'Here is the monthly report.'
   
    # Define the recipient's email address
    recipient_email = 'receiver@example.com'
   
    # Call the send_email function to send the email
    send_email(subject, body, recipient_email)