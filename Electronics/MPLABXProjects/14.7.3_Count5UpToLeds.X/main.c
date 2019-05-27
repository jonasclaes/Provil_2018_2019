/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 20 mei 2019, 9:49
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

char Som(char x, char y);

void main(void) {
    // Configure inputs and outputs.
    ANSEL = 0x00;
    ANSELH = 0x00;
    TRISB = 0xFF;
    TRISC = 0x00;
    
    char switches;
    char previousSwitches;
    char count;
    char previousCount;
    
    count = 0;
    
    while (1) {
        previousSwitches = switches;
        switches = PORTB;
        
        if (switches == 0x01 && previousSwitches == 0x00) {
            previousCount = count;
            count = Som(count, 5);
            if (previousCount > count) {
                count = 0;
                
                for (char i = 0; i < 5; i++) {
                    PORTC = 0x00;
                    __delay_ms(1000);

                    PORTC = 0xFF;
                    __delay_ms(1000);
                }
            }
            
            PORTC = count;
        }
    }
}

char Som(char x, char y) {
    return x + y;
}