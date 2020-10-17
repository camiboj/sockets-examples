import argparse
import socket
import time
import os
from constants import CHUNK_SIZE

def get_timestamp():
  return int(round(time.time()*1000))

def parse_arguments():
  parser = argparse.ArgumentParser()

  parser.add_argument("-H", "--host", default="127.0.0.1")
  parser.add_argument("-P", "--port", type=int, default="8080")

  return parser.parse_args()

def main():
  args = parse_arguments()
  host = args.host
  port = args.port #int(os.environ.get("PORT", args.port))
  address = (host, port)
  print(f"adress - host: {host}, port: {port}")

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print('Binding...')
  sock.bind(address)
  print('Binding ok')
  print('Liten...')
  sock.listen(1)
  print('Liten ok')

  while True:
    conn, addr = sock.accept()
    if not conn:
      break

    print(f"{get_timestamp()} - Accepted connection from {addr}")

    bytes_received = 0

    size = conn.recv(CHUNK_SIZE).decode()
    print(f"Size? - {size}")
    if not size:
      continue
    size = int(size)
    print(f"Size - {size}")
    conn.send(b'start')

    print(f"Receiving...")
    while bytes_received < size:
      data = conn.recv(CHUNK_SIZE)
      bytes_received += len(data)
      print(f"data: {data}")

    print(f"Receiving ok")

    # Send number of bytes received
    conn.send(str(bytes_received).encode())


  sock.close()

if __name__ == "__main__":
    print("Inilcializando server...")
    main()
