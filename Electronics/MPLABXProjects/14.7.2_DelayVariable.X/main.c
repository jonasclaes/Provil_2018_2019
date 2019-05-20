/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 20 mei 2019, 9:20
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void Delay(int time);

void main(void) {
    TRISC = 0x00;
    
    int delay = 10000;
    
    while (1) {
        PORTC = 0x00;
        Delay(delay);
        PORTC = 0xFF;
        Delay(delay);
    }
}

void Delay(int time) {
    for (time; time > 0; time--) {
        __delay_us(1);
    }
}