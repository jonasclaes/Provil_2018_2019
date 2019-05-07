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
    
    TRISB = 0xFF;
    TRISD = 0x00;
    
    while (1) {
        switches = PORTB;
        
        if (switches) {
            count = 0;
            
            while (1) {
                if (!switches) {
                    break;
                }
                
                count++;
                PORTD = count;

                __delay_ms(100);
            }
        }
    }
}