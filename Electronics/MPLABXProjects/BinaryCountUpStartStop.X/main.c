/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 7 mei 2019, 13:37
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
        
        if (switches == 0x01) {
            while (1) {
                if (switches == 0x02) {
                    break;
                }
                
                count++;
                PORTD = count;

                __delay_ms(100);
            }
        }
    }
}
