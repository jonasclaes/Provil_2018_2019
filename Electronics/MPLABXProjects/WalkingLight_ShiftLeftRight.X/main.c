/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 13 mei 2019, 9:03
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    char leds = 0x01;
    
    TRISD = 0x00;
    
    while (1) {
        for (int i = 0; i < 7; i++) {
            PORTD = leds;
            leds = leds << 1;
            __delay_ms(75);
        }
        
        for (int i = 0; i < 7; i++) {
            PORTD = leds;
            leds = leds >> 1;
            __delay_ms(75);
        }
    }
}
