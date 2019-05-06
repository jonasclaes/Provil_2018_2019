/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 6 mei 2019, 9:32
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    char count;
    
    TRISD = 0x00;
    
    while (1) {
        count++;
        PORTD = count;
        
        if (count == 255) {
            __delay_ms(2000);
        } else {
            __delay_ms(40);
        }
    }
}
