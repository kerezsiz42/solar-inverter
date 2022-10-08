# python 3.10
# pip install pyserial libscrc
import serial
import libscrc

slave_address = 0x01
function_code = 0x03


def create_pdu(addr: int):
    return bytes([slave_address, function_code,
                  addr // 256, addr % 256, 0x00, 0x10])


with open("output.txt", "w+") as f:
    with serial.Serial('COM3', 9600, timeout=0.1) as ser:
        for addr in range(0, 65536, 16):
            pdu = create_pdu(addr)
            crc: bytes = libscrc.modbus(pdu).to_bytes(2, "little")
            adu = pdu + crc
            req = adu.hex("-")
            ser.write(adu)
            ser.flush()
            res = ser.readline().hex('-')
            print(f"{req}::{res}")
            f.write(f"{req}::{res}\n")
            f.flush()
