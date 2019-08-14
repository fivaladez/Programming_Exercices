#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void is_letter(char * phrase);

unsigned int cantidad_casos = 0;
char phrase[10];

void main( void ) {
    printf("\n\tIntroduce the qty of cases: ");
    scanf("%d", &cantidad_casos);

    for(int cnt = 0; cnt < cantidad_casos; cnt++)
    {
        printf("\n\tIntroduce a phrase: ");
        fflush(stdin);
        gets( phrase );
        is_letter( phrase );
    }

}

void is_letter(char * phrase)
{
    unsigned char status = 1;

    for(unsigned int cnt = 0; *(phrase + cnt) != NULL; cnt++)
    {
        if( *(phrase + cnt) >= 'a' && *(phrase + cnt) <= 'z' )
        {

        }else if( *(phrase + cnt) >= 'A' && *(phrase + cnt) <= 'Z' )
        {

        }else if( *(phrase + cnt) == ' ' )
        {

        }
        else
        {
            printf("\n\tYou have a non-letter character: %c", *(phrase + cnt));
            status = 0;
        }
    }
    if( status == 1)
        printf("\n\tAll your sentence is with letters");
    else
        printf("\n\tYou have a non-letter character.");
}
