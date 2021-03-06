import pytest

def test_init(wpilib, hal_data):
    di = wpilib.DigitalInput(2)
    assert hal_data['dio'][2]['initialized']
    assert hal_data['dio'][2]['is_input']

def test_get(wpilib, hal_data):
    di = wpilib.DigitalInput(2)
    hal_data['dio'][2]['value'] = True
    assert di.get()

def test_is_analog_trigger(wpilib):
    di = wpilib.DigitalInput(2)
    assert not di.isAnalogTrigger()

