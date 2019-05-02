/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 2 mei 2019, 13:18
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    OPTION_REG = OPTION_REG & 0b01111111;
    WPUB = 0xFF;
    
    char Switches_B;
    
    // Analoge functie van AD pins uitschakelen
    ANSEL = 0x00;
    ANSELH = 0x00;
    
    TRISC = 0x00;               // PORTC = OUTPUT
    TRISB = 0xFF;               // PORTB = INPUT
    
    while (1) {
        Switches_B = PORTB;     // Lees de waarde van poort B in in variabele Switches_B
        PORTC = Switches_B;     // Lees de waarde van variabele Switches_B in in poort C
    }
}
