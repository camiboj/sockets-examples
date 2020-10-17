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
  port = int(os.environ.get("PORT", args.port))
  address = (host, port)
  print(f"adress - host: {host}, port: {port}")

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print('Binding...')
  sock.bind(address)
  print('Binding ok')
  sock.listen(1)

  while True:
    conn, addr = sock.accept()
    if not conn:
      break

    print("Accepted connection from {}".format(addr))

    filename = f"./file-{get_timestamp()}.bin"
    f = open(filename, "wb")
    bytes_received = 0

    size = int(conn.recv(CHUNK_SIZE).decode())
    conn.send(b'start')

    while bytes_received < size:
      data = conn.recv(CHUNK_SIZE)
      bytes_received += len(data)
      f.write(data)

    print(f"Received file {filename}")

    # Send number of bytes received
    conn.send(str(bytes_received).encode())

    f.close()

  sock.close()

if __name__ == "__main__":
    print("Inilcializando server...")
    main()
