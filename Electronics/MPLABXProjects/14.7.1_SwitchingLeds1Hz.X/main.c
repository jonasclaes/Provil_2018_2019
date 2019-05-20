/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 20 mei 2019, 8:51
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void EvenLeds(void);
void OnevenLeds(void);

void main(void) {
    TRISD = 0x00;
    
    while (1) {
        EvenLeds();
        __delay_ms(500);
        OnevenLeds();
        __delay_ms(500);
    }
}

void EvenLeds(void) {
    PORTD = 0x55;
}

void OnevenLeds(void) {
    PORTD = 0xAA;
}