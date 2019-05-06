/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 6 mei 2019, 9:21
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    char leds = 1;
    
    TRISD = 0x00;
    
    while (1) {
        while (leds != 128) {
            leds = leds * 2;
            PORTD = leds;
            __delay_ms(500);
        }
        
        while (leds != 1) {
            leds = leds / 2;
            PORTD = leds;
            __delay_ms(500);
        }
    }
}
