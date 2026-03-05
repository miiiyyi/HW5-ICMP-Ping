from socket import *

msg = "\r\nI love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.freesmtpservers.com", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
print("Connecting to:", mailserver)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM:<mita_test_sender@example.com>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO:<mita_test_recipient@example.com>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] not in ['250', '251']:
    print('250/251 reply not received from server.')

# Send DATA command and print server response.
dataCmd = "DATA\r\n"
clientSocket.send(dataCmd.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
message = (
    "From: <mita_test_sender@example.com>\r\n"
    "To: <mita_test_recipient@example.com>\r\n"
    "Subject: CMPE-148 SMTP Lab\r\n"
    "\r\n" 
)
clientSocket.send(message.encode())
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCmd = "QUIT\r\n"
clientSocket.send(quitCmd.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)

clientSocket.close()