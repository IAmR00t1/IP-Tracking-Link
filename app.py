from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def tracker():
    # Capture visitor details
    ip_address = request.headers.get('X-Forwarded-for', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    with open("log.txt", "a") as log:
        log.write(f"IP: {ip_address}, User-Agent: {user_agent}\n")

    # Redirect to another site
    return redirect("https://tinyurl.com/338zpvfu")  # Replace with your target site URL

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
