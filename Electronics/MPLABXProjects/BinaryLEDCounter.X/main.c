/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 29 april 2019, 9:08
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

#define LEDS PORTB
unsigned char count = 0x00;

void main(void) {
    TRISB = 0x00;
    while (1) {
        LEDS = count;
        count++;
        __delay_ms(100);
    }
}
