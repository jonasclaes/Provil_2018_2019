/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 25 april 2019, 13:11
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    TRISB = 0x00;
    PORTB = 0xFF;
}
