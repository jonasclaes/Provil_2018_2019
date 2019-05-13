/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 6 mei 2019, 9:53
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    char switches;
    char count;
    
    TRISC = 0xFF;
    TRISD = 0x00;
    
    PORTD = 0x00;
    
    start:
    
    while (1) {
        switches = PORTC;
        
        if (switches) {
            count = 0;
            
            while (1) {
                switches = PORTC;
                
                if (!switches) {
                    goto start;
                }
                
                count++;
                PORTD = count;

                __delay_ms(20);
            }
        }
    }
}