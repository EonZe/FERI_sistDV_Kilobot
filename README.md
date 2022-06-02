# FERI_sistDV_Kilobot
Programming kilobot:

Make sure that your kilobot id matches your aruco marker id. Your id should be only one character long(for id 10 use kilobot id 'A', for 11 use 'B'...).

If you use F446 with NRF shield, then use rf_gateway_nrf for your gateway.

Kilobot commands:
first character in a command is kilobot id. In examples below the id will mostly be 5:

5T ...  test kilobot with id 5
1. PWM1 is set to 2000 for 1 s, LED gets toggled
2. PWM1 is set to 0 and PWM2 is set to 2000 for 1 s, LED gets toggled
3. PWM2 is set to 0, LED gets toggled

5P2000 0100 ... set PWM on kilobot with id 5 (PWM1 is set as 2000, PWM2 is set as 0100)   !! Always use 4 digit numbers !!

you can send multiple commands at once, by seperating them with semicolon:
5T;1P2000 0100;6P2000 0100;7P2000 0100...

Maximum serial message lenght is 256 characters. All messages must also be terminated with \n character. Maximum NRF command lenght, including id is 32 bytes.
