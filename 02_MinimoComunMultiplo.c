#include <stdio.h>

unsigned int getMCM(unsigned int n1, unsigned int n2);
unsigned int numero1 = 0;
unsigned int numero2 = 0;

void main( void ) {
    printf("\n\tIntroduce a positive enter number: ");
    scanf("%d", &numero1);
    printf("\n\tIntroduce another positive enter number: ");
    scanf("%d", &numero2);

    printf("\n\tThe MCM number is: %d", getMCM(numero1, numero2) );
}

unsigned int getMCM(unsigned int n1, unsigned int n2)
{
    unsigned int mcm = 0;

    mcm = n1>n2 ? n1 : n2;

    while((mcm%n1!=0) || (mcm%n2!=0) )
    {
        mcm++;
    }
    return mcm;
}
