/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 13 mei 2019, 9:40
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    char switches;
    char previousSwitches;
    char count;
    
    TRISC = 0xFF;
    TRISD = 0x00;
    
    PORTD = 0x00;
    
    start:
    
    while (1) {
        previousSwitches = switches;
        switches = PORTC;
        
        if (switches == 0x01 && previousSwitches == 0x00) {
            while (1) {
                previousSwitches = switches;
                switches = PORTC;
                
                if (switches == 0x01 && previousSwitches == 0x00) {
                    goto start;
                }
                
                count++;
                PORTD = count;

                __delay_ms(50);
            }
        }
    }
}
