#!/usr/bin/env python3

import os, datetime
import reports
import email.message
import smtplib
import mimetypes

#get the current time in GMT
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def generate_pdf(path):
    pdf = ""
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(path + file, 'r') as f:
                inline = f.readlines()
                name = inline[0].strip()
                weight = inline[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return pdf

if __name__ == "__main__":
    
    ## Generate PDF
    path = "supplier-data/descriptions/"
    title = "Process Updated on " + current_date 
    pdf_package = generate_pdf(path)
    reports.generate_report("/tmp/processed.pdf", title, pdf_package)
    
    ## Generate email information
    sender = "automation@example.com"
    receiver = "student-02-dde78dd51971@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"    
    
    ## Generate Message
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
    
    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)
    
    ## Send Message
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

## Formal alternativa para enviarlo con emails y no con email
# import emails
# if __name__ == "__main__":
#   path = "supplier-data/descriptions/"
#   title = "Process Updated on " + current_date 
#   #generate the package for pdf body
#   package = generate_pdf(path)
#   reports.generate_report("/tmp/processed.pdf", title, package)

#   #generate email information
#   sender = "automation@example.com"
#   receiver = "{}@example.com".format(os.environ["USER"])
#   subject = "Upload Completed - Online Fruit Store"
#   body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
#   attachment = "/tmp/processed.pdf"
  
#   #generate email for the online fruit store report and pdf attachment
#   message = emails.generate_email(sender, receiver, subject, body, attachment)
#   emails.send_email(message)
