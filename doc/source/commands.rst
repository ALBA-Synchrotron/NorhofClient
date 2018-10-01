************************
Norhof commands exported
************************

Basic SCPI commands:
====================
* **\*IDN?**: Request system identifier (SN).

System comands:
===============
* **:SYS:NAME?**: Request system name.
* **:SYS:INFO?**: About the system.
* **:SYS:STATUS?**: Report system status.

Measurements:
=============
* **:MEAS:TEMP?**: Ask temperature setting.
* **:MEAS:FLOW?**: Ask flow setting.
* **:TEMP <value>**: Set temperature to `value` [Celcius].
* **:FLOW <value>**: Set flow to `value` [mbar].

Pump operation commands:
========================
* **:PUMP:MODE?**: Request pump operation mode.
* **:PUMP:CONTROL?**: Request operation status.
* **:CONTROL <value>**: Set operation to `value` (0 = `standby`, 1 = 'active', 3 = `pumping`).
