import socket
import signal
import sys
import random

# Read a command line argument for the port where the server
# must run.
port = 8080
if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    print("Using default port 8080")

# Start a listening server socket on the port
sock = socket.socket()
sock.bind(('', port))
sock.listen(2)

logins = {k:v.strip() for (k,v) in [line.split(" ")  for line in open("passwords.txt").readlines()]}
secrets = {k:v.strip() for (k,v) in [line.split(" ")  for line in open("secrets.txt").readlines()]}
sessions = {}

### Contents of pages we will serve.
# Login form
login_form = """
   <form action = "http://localhost:%d" method = "post">
   Name: <input type = "text" name = "username">  <br/>
   Password: <input type = "text" name = "password" /> <br/>
   <input type = "submit" value = "Submit" />
   </form>
""" % port
# Default: Login page.
login_page = "<h1>Please login</h1>" + login_form
# Error page for bad credentials
bad_creds_page = "<h1>Bad user/pass! Try again</h1>" + login_form
# Successful logout
logout_page = "<h1>Logged out successfully</h1>" + login_form
# A part of the page that will be displayed after successful
# login or the presentation of a valid cookie
success_page = """
   <h1>Welcome!</h1>
   <form action="http://localhost:%d" method = "post">
   <input type = "hidden" name = "action" value = "logout" />
   <input type = "submit" value = "Click here to logout" />
   </form>
   <br/><br/>
   <h1>Your secret data is here:</h1>
""" % port

#### Helper functions
# Printing.
def print_value(tag, value):
    print( "Here is the", tag)
    print( "\"\"\"")
    print( value)
    print( "\"\"\"")
    print()

# Signal handler for graceful exit
def sigint_handler(sig, frame):
    print('Finishing up by closing listening socket...')
    sock.close()
    sys.exit(0)
# Register the signal handler
signal.signal(signal.SIGINT, sigint_handler)


# TODO: put your application logic here!
# Read login credentials for all the users
# Read secret data of all the users




### Loop to accept incoming HTTP connections and respond.
while True:
    client, addr = sock.accept()
    req = client.recv(1024)

    # Let's pick the headers and entity body apart
    header_body = req.decode("utf-8").split('\r\n\r\n')
    headers = header_body[0]
    body = '' if len(header_body) == 1 else header_body[1]
    print_value('headers', headers)
    print_value('entity body', body)

    # TODO: Put your application logic here!
    # Parse headers and body and perform various actions

    if headers == "": continue

    header_lines = headers.split("\n")
    (method, route, _t) = header_lines[0].split(" ")
    print(method, route, _t)
    header_data = {}

    for line in header_lines[1:]:
        (key, val) = line.split(":",1)
        val = val.strip()
        header_data[key] = val

    args = {}
    for line in body.split("&"):
        arg = line.split("=")
        args[arg[0]] = arg[1] if len(arg) > 1 else ""
    
    html_content_to_send = login_page
    headers_to_send = ''


    # You need to set the variables:
    # (1) `html_content_to_send` => add the HTML content you'd
    # like to send to the client.
    # Right now, we just send the default login page.
    # But other possibilities exist, including
    # html_content_to_send = success_page + <secret>
    # html_content_to_send = bad_creds_page
    # html_content_to_send = logout_page
    
    # (2) `headers_to_send` => add any additional headers
    # you'd like to send the client?
    # Right now, we don't send any extra headers.
    if method == "POST":
        if route == "/":
            if "username" in args and "password" in args:
                user, pw = args["username"], args["password"]
                if user in logins and logins[user] == pw:
                    html_content_to_send = success_page+secrets[user]
                    rand_val = random.getrandbits(64)
                    headers_to_send = 'Set-Cookie: token=' + str(rand_val) + '\r\n'
                    sessions[rand_val] = user
                else:
                    html_content_to_send = bad_creds_page
            elif "action" in args:
                action = args["action"]
                if action == "logout":
                    if "Cookie" in header_data:
                        sessions[header_data["Cookie"]] = None
    elif method == "GET":
        if "Cookie" in header_data:
            cookie = sessions[header_data["Cookie"]]
            if sessions[cookie]:
                html_content_to_send = success_page+secrets[sessions[cookie]]
            else:
                html_content_to_send = bad_creds_page
        else:
            pass



    # Construct and send the final response
    response  = 'HTTP/1.1 200 OK\r\n'
    response += headers_to_send
    response += 'Content-Type: text/html\r\n\r\n'
    response += html_content_to_send
    print_value('response', response)    
    client.send(response.encode("utf-8"))
    client.close()
    
    print("Served one request/connection!")
    print

# We will never actually get here.
# Close the listening socket
sock.close()
