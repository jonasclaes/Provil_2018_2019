/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 29 april 2019, 9:26
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    TRISB = 0x00;
    while (1) {
        PORTB = 0x55;
        __delay_ms(100);
        PORTB = 0xAA;
        __delay_ms(100);
    }
}
