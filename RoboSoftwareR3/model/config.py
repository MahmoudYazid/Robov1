connection={
    "connectionstring": "mongodb://localhost:27017"
}

PortsConfig={
    "glucose_pin" : 4,
    "eye_pin" : 17,
    "blood_nose_pin" : 27,
    "blood_mouth_pin" : 18,
    "water_nose_pin" : 22,
    "water_mouth_pin" : 25,

    "act_en_pin" : 2,
    "act_dir1_pin" : 23,
    "act_dir2_pin" : 24,

    "convulsion_en_pin" : 16,
    "convulsion_dir1_pin" : 20,

    "led_en_pin" : 5,
    "led_dir1_pin" : 6,

    "heating_pin" : 26,

}

DegreesConfig={
    "HyperGlu": 12,
    "HypoGlu":1.5,
    "NormalGlu":6,
    "SlowMove":12,
    "StopMotor":0,
    "FastMove":50,
    "EyeContract":1,
    "EyeDilute":12
}

# PwmStart["start"]
PwmStart={
    "start":2.5

}

sleepConfigTimer={
    "BloodWater_MotorDelay":.5,
    "SlowMove_MotorDelay": 2,
    "FastMove_MotorDelay": .5,
    "Eye_MotorDelay": .5,
    "Glu_MotorDelay": 1,
    "HyperBreath_MotorDelay":.5,
    "HyperThermia_delay":.5,
    "HypoBreath_MotorDelay":[1,2,1],
    "NormalBreath_MotorDelay": 1,
    "pigmentation_MotorDelay":.5,

}

Digital={
    "on":1,
    "off":0
}

