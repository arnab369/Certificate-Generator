from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from io import BytesIO
import qrcode

if not os.path.exists('certificates/images'):
    os.makedirs('certificates/images')
if not os.path.exists('certificates/pdf'):
    os.makedirs('certificates/pdf')

# CSV file (Comma Separated Values)
file_path = "C:/Users/ASUS/Desktop/work/Certificate_generator/Gulal3.csv"
df = pd.read_csv(file_path)

for index, j in df.iterrows():

    # Add name
    # Save in jpg format
    font = ImageFont.truetype('arialbd.ttf', 35)
    img = Image.open('C:/Users/ASUS/Desktop/work/Certificate_generator/image.jpg')

    # Open the image file in RGBA mode
    try:
        img = Image.open('image.png')
    except FileNotFoundError:
        print("The image file does not exist.")

    # Convert the image to RGB mode
    img = img.convert('RGB')

    # Save the image in JPEG format
    img.save('image.jpg')

    draw = ImageDraw.Draw(img)
    draw.text(xy=(86, 590), text='{}'.format(j['name']), fill=(255, 255, 255), font=font)

    # Add QR code
    qr = qrcode.QRCode(version=1, box_size=12.5, border=6)
    ticket_data = f'Registration No.: {j["regno"]}\nName: {j["name"]}'
    qr.add_data(ticket_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color='black', back_color='white')
    # qr_width, qr_height = qr_img.size
    # img_width, img_height = img.size
    # draw_qr_x = 1398  # adjust the x coordinate as necessary 1398, 45
    # draw_qr_y = 45  # adjust the y coordinate as necessary 1954, 605
    # img.paste(qr_img, (draw_qr_x, draw_qr_y))
    #draw.text(xy=(49, 590), text='{}'.format(j['qr_img']), fill=(255, 255, 255), font=font)

    byte_stream = BytesIO()
    qr_img.save(byte_stream, format="PNG")
    byte_stream.seek(0)

    qr_img = Image.open(byte_stream)
    img.paste(qr_img, (1406, 59))

    if j['GENDER'] == 'Male':
        reporting_ground = 'BH7 Ground'
    else:
        reporting_ground = 'GH2 Ground'
    font = ImageFont.truetype('arialbd.ttf', 35)
    draw.text(xy=(994, 590), text=reporting_ground, fill=(255, 255, 255), font=font)

    img.save('certificates/images/{}.jpg'.format(j['name']))

    # Add certificate no.
    # Save in pdf format and jpg format
    font = ImageFont.truetype('arialbd.ttf', 35)
    draw.text(xy=(569, 591), text='{}'.format(j['regno']), fill=(255, 255, 255), font=font)
    #draw.text(xy=(2930.41, 136.96), text='{}'.format(reporting_ground), fill=(0, 0, 0), font=font)
    img.save('certificates/pdf/{}.pdf'.format(j['name']))
    img.save('certificates/images/{}.jpg'.format(j['name']))

message = 'Successful!'

# print the string message
print(message)




# from PIL import Image, ImageDraw, ImageFont
# import pandas as pd
# import os
# import qrcode
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication

# # CSV file (Comma Separated Values)
# file_path = "C:/Users/ASUS/Desktop/work/Certificate_generator/HOLI.csv"
# df = pd.read_csv(file_path)

# # Email credentials
# sender_email = 'amarnabmajumder951@gmail.com'
# sender_password = '#Bimal@3678'
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587

# if not os.path.exists('certificates/images'):
#     os.makedirs('certificates/images')


# for index, j in df.iterrows():

#     # Add name
#     # Save in jpg format
#     font = ImageFont.truetype('arialbd.ttf', 100)
#     img = Image.open('C:/Users/ASUS/Desktop/work/Certificate_generator/image.jpg')
#     draw = ImageDraw.Draw(img)
#     draw.text(xy=(2030.22, 1020.21), text='{}'.format(j['name']), fill=(0, 0, 0), font=font)

#     # Add QR code
#     qr = qrcode.QRCode(version=1, box_size=10, border=5)
#     ticket_data = f'Ticket No.: {j["regno"]}\nName: {j["name"]}'
#     qr.add_data(ticket_data)
#     qr.make(fit=True)
#     qr_img = qr.make_image(fill_color='black', back_color='white')
#     qr_width, qr_height = qr_img.size
#     img_width, img_height = img.size
#     draw_qr_x = img_width - qr_width - 100  # adjust the x coordinate as necessary
#     draw_qr_y = 200  # adjust the y coordinate as necessary
#     img.paste(qr_img, (draw_qr_x, draw_qr_y))

#     if j['GENDER'] == 'Male':
#         reporting_ground = 'Reporting on BH1 ground'
#     else:
#         reporting_ground = 'Reporting on GH1 ground'
#     font = ImageFont.truetype('arial.ttf', 50)
#     draw.text(xy=(2030.22, 1120.21), text=reporting_ground, fill=(0, 0, 0), font=font)

#     img.save('certificates/images/{}.jpg'.format(j['name']))

#     # Add certificate no.
#     # Save in pdf format and jpg format
#     font = ImageFont.truetype('arialbd.ttf', 60)
#     draw.text(xy=(2924.41, 57.96), text='{}'.format(j['regno']), fill=(255, 255, 255), font=font)
#     draw.text(xy=(2930.41, 136.96), text='{}'.format(reporting_ground), fill=(0, 0, 0), font=font)
#     img.save('certificates/pdf/{}.pdf'.format(j['name']))
#     img.save('certificates/images/{}.jpg'.format(j['name']))

#     # Send email
#     receiver_email = j['email']
#     message = MIMEMultipart()
#     message['Subject'] = 'Certificate for {}'.format(j['name'])
#     message['From'] = sender_email
#     message['To'] = receiver_email




#     # Attach JPG
#     with open('certificates/images/{}.jpg'.format(j['name']), 'rb') as f:
#         img_data = f.read()
#         msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename='{}.jpg'.format(j['name']))

#     with open('certificates/pdf/{}.pdf'.format(j['name']), 'rb') as f:
#         pdf_data = f.read()
#         msg.add_attachment(pdf_data, maintype='application', subtype='octet-stream', filename='{}.pdf'.format(j['name']))

# # Send Email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(email_address, email_password)
#     smtp.send_message(msg)

# message = 'Successful!'

# # # print the string message
# print(message)
