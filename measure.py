import pyvisa

#code referenced from: https://testflowinc.com/blog/automate-rigol-oscilloscope-python-scpi-pyvisa-guide

try:
    rm = pyvisa.ResourceManager()

    #will print address of rigol multimeter, use to connect
    print(rm.list_resources())

    #connect to multimeter, use address here
    dm = rm.open_resource('')

    #confirm identity of multimeter by opening instrucment and sending *IDN? command
    print(dm.query('*IDN?'))


    #get measurement from multimeter, use command to get measurement
    measurement = dm.query(":MEASurement:VOLTage:DC?")

    print("Voltage Measurement: ", measurement)
except Exception as e:
    print("Error: ", e)
