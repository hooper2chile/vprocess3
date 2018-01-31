/*
uc_master
Write by: Felipe Hooper
Electronic Engineer
*/

#include <avr/wdt.h>
#include "mlibrary.h"


void setup() {
  wdt_disable();

  setup_default_relay();

  Serial.begin(9600);
  mySerial.begin(9600);

  message.reserve(65);

  wdt_enable(WDTO_8S);
}


void loop() {
  if ( stringComplete  ) {
      if ( validate() ) {
          //PORTB = 1<<PB0;

          switch ( message[0] ) {
              case 'r':  //lectura de sensores
                hamilton_sensors();
                daqmx();
                control_ph();
                heat_exchanger_controller();   //control de temperatura
                broadcast_setpoint(0);
                break;

              case 'w':  //setpoints
                setpoint();
                control_ph();
                heat_exchanger_controller();   //control de temperatura
                motor_set();
                broadcast_setpoint(1);
                daqmx();
                break;

              case 'c':  //calibracion de sensores
                sensor_calibrate();
                break;

              case 'u':  //umbrales actuadores motores
                actuador_umbral();
                break;

              case 'a': //autoclave set
                autoclave_sets();

              default:
                break;
          }

          //PORTB = 0<<PB0;
      }
      else {
        Serial.println("bad validate");
      }

    clean_strings();
    wdt_reset();
  }
}
