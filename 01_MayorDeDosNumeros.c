#include <stdio.h>

unsigned int numero1 = 0;
unsigned int numero2 = 0;

void main( void ) {
    printf("\n\tIntroduce a positive enter number: ");
    scanf("%d", &numero1);
    printf("\n\tIntroduce another positive enter number: ");
    scanf("%d", &numero2);

    printf("\n\tThe greater number is: %d", (numero1 > numero2 ? numero1 : numero2) );
}
