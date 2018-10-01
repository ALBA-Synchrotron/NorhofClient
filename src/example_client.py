#!/usr/bin/env python

import socket
import time


def cmd(scpi_cmd, host="84.89.227.57", port=11000):
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((host, port))
    cs.send("{0}<EOF>".format(scpi_cmd))
    data = cs.recv(4096)
    cs.close()
    return data


def test():

    idn = cmd('*IDN?')

    name = cmd(':SYS:NAME?')
    info = cmd(':SYS:INFO?')
    status = cmd(':SYS:STATUS?')

    temp = cmd(':MEAS:TEMP?')
    flow = cmd(':MEAS:FLOW?')

    mode = cmd(':PUMP:MODE?')
    control = cmd(':PUMP:CONTROL?')

    msg = 'System ID = {0}\n'.format(idn)
    msg += 'System name = {0}\n'.format(name)
    msg += 'System information = {0}'.format(info)
    msg += 'System status = {0}\n'.format(status)
    msg += 'Temperature setting = {0}\n'.format(temp)
    msg += 'Flow setting = {0}\n'.format(flow)
    msg += 'Pump mode = {0}\n'.format(mode)
    msg += 'Pump control = {0}'.format(control)
    print msg

    new_temp = -190
    new_flow = 10
    print 'Setting temperature = {0} and flow = {1}'.format(new_temp, new_flow)
    cmd(':TEMP %s' % new_temp)
    cmd(':FLOW %s' % new_flow)
    time.sleep(3)
    print 'Restoring original values (temperature = {0} and flow = {1}'.\
        format(temp, flow)
    cmd(':TEMP %s' % new_temp)
    cmd(':FLOW %s' % new_flow)

    print 'Start pumping'
    cmd(':PUMP:CONTROL %s' % 3)
    time.sleep(3)
    print 'Stop pumping'
    cmd(':PUMP:CONTROL %s' % 0)

    print '*** Test END ***'


if __name__ == "__main__":

    test()
