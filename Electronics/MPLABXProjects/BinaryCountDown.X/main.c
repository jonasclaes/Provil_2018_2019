/*
 * File:   main.c
 * Author: Jonas
 *
 * Created on 6 mei 2019, 8:57
 */


#include <xc.h>
#define _XTAL_FREQ 4000000

#pragma config CONFIG1 = 0xEFE4
#pragma config CONFIG2 = 0xFFFF

void main(void) {
    char count;
    
    TRISD = 0x00;
    
    while (1) {
        count = 255;
        while (count > 0) {
            PORTD = count;
            count--;
            __delay_ms(50);
        }
    }
}
