from django.http import HttpResponse
import os
import time

def htop_view(request):
    name = "Your_Full_Name"
    username = os.getenv('USER', 'unknown')
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    top_output = os.popen('top -bn1').read()
    
    response = f"""
    <h1>System Info</h1>
    <p>Name: {name}</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)
