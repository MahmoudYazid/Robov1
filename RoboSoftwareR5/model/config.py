connection={
    "connectionstring": "./rdb.db"
}

TablesSchima = {
    "QDB": {
    "nameofsymp": 0,
	"answer": 1,
	"question": 2,
	"state": 3,
	"SymptomId": 4,
	"KindId": 5,
	"id": 6,
    },
    "ODB": {
        "Id": 0,
        "OrganName": 1,
    },
    "EDB": {
	"Id": 0,
	"effectorName": 1,
	"effectorType": 2,
    },
    "BDB": {

	"SympId": 0,
	"effectorName": 1,
	"place": 2,
	"type_effector": 3,
	"EffectorId": 4,
	"blockId": 5,
	"id": 6,
    },
    "ADB": {
	"state": 0,
	"KindId": 1,
	"place": 2,
	"id": 3, }


}
PortsConfig={
    
    "eye_pin" : 17,
    "blood_nose_pin" : 27,
    "blood_mouth_pin" : 22,
    "water_nose_pin" : 25,
    "water_mouth_pin" : 18,

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
    
 
    "SlowMove":12,
    "StopMotor":0,
    "FastMove":50,
    "EyeContract":1,
    "EyeDilute":70
}

# PwmStart["start"]
PwmStart={
    "start":50

}

sleepConfigTimer={
    "BloodWater_MotorDelay":.5,
    "SlowMove_MotorDelay": 2,
    "FastMove_MotorDelay": .5,
    "Eye_MotorDelay": .5,
    
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

