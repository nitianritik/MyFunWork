import time
import socketio
import requests.exceptions

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.event
def connect_error(error):
    print('Failed to connect to server:', error)

@sio.event
def disconnect():
    print('Disconnected from server')

try:
    sio.connect('http://localhost:8000')
    while True:
        try:
            sio.emit('message', 'hello')
        except requests.exceptions.RequestException as e:
            print('Error sending message:', e)
        time.sleep(1)
except Exception as e:
    print('Error:', e)
finally:
    sio.disconnect()
