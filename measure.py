import pyvisa

#code referenced from: https://testflowinc.com/blog/automate-rigol-oscilloscope-python-scpi-pyvisa-guide

rm = pyvisa.ResourceManager()

#will print address of rigol multimeter, use to connect
#print(rm.list_resources())

#connect to multimeter, use address here
dm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R223100938::INSTR')

#confirm identity of multimeter by opening instrucment and sending *IDN? command
print(dm.query('*IDN?'))

try:
    #get measurement from multimeter, use command to get measurement
    measurement = dm.query(":MEASure:VOLTage:DC?")
    measurement = float(measurement)
    print("Voltage Measurement: ", measurement, "V")
except Exception as e:
    print("type:", type(e).__name__)
    print("error:", e)
