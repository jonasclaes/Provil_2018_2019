/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 3 juni 2019, 9:02
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void ShiftLeft(void);
void ShiftRight(void);
void Flash(void);

void main(void) {
    TRISB = 0xFF;
    ANSEL = 0x00;
    ANSELH = 0x00;
    TRISC = 0x00;
    
    PORTC = 0x01;
    
    while (1) {
        switch(PORTB) {
            case 0x01:
                ShiftLeft();
                
                // Prevent from looping through leds, so wait until switch is released.
                while (PORTB != 0x00) {};
                __delay_ms(100);
                break;
            
            case 0x02:
                ShiftRight();
                
                // Prevent from looping through leds, so wait until switch is released.
                while (PORTB != 0x00) {};
                __delay_ms(100);
                break;
                
            case 0x04:
                Flash();
                break;
        }
    }
}

void ShiftLeft(void) {
    PORTC = PORTC << 1;
    
    // Check if port C is cleared.
    if (PORTC == 0x00) {
        PORTC = 0x80;
    }
}

void ShiftRight(void) {
    PORTC = PORTC >> 1;
    
    // Check if port C is cleared.
    if (PORTC == 0x00) {
        PORTC = 0x01;
    }
}

void Flash(void) {
    // Copy value to variable.
    char previousValue = PORTC;
    
    // Set port C to 0.
    PORTC = 0x00;
    __delay_ms(500);
    
    // Set port C to previous value.
    PORTC = previousValue;
    __delay_ms(500);
}