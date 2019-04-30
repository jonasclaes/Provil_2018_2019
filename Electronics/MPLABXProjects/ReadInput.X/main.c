/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 30 april 2019, 14:59
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    char Switches_B;
    
    // Analoge functie van AD pins uitschakelen
    ANSEL = 0x00;
    ANSELH = 0x00;
    
    TRISD = 0x00;               // PORTD = OUTPUT
    TRISB = 0xFF;               // PORTB = INPUT
    
    while (1) {
        Switches_B = PORTB;     // Lees de waarde van poort B in in variabele Switches_B
        PORTD = Switches_B;     // Lees de waarde van variabele Switches_B in in poort D
    }
}
