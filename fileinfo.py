#include <stdio.h>
#include<unistd.h>
#include<Windows.h>
#define MAX_DIGITS 10
#define CLEAR "cls"
const int segments[10][7] = {
    {1, 1, 1, 1, 1, 1, 0}, // code for 0 
    {0, 1, 1, 0, 0, 0, 0}, // code for 1 
    {1, 1, 0, 1, 1, 0, 1}, // code for 2 
    {1, 1, 1, 1, 0, 0, 1}, // code for 3 
    {0, 1, 1, 0, 0, 1, 1}, // code for 4 
    {1, 0, 1, 1, 0, 1, 1}, // code for 5 
    {1, 0, 1, 1, 1, 1, 1}, // code for 6 
    {1, 1, 1, 0, 0, 0, 0}, // code for 7 
    {1, 1, 1, 1, 1, 1, 1}, // code for 8 
    {1, 1, 1, 1, 0, 1, 1}  // code for 9 
};

char digits[3][MAX_DIGITS * 4];

void clear_digits_array(void);//flush the canvas
void process_digits_array(int dight, int position);//paint
void print_digits_array(void);//print 
int display(int);//print an int 
void countdown_display(int);//countdown based on display

int main(void) 
{
    printf("Enter a positive integer: ");
    int n;
    scanf("%d",&n);
    if(n<=0)
    {
        printf("ERROR INPUT!\n");
        return -1;
    } 
    printf("%d can be displayed as:\n",n);
    //return display(n);
    countdown_display(n);
}

void clear_digits_array(void) 
{
   int i,j;
   for(i=0;i<3;i++)
    for(j=0;j<MAX_DIGITS*4;j++)
        digits[i][j]=' ';
}
void process_digits_array(int digit, int position) 
{
	if(position>=MAX_DIGITS)
		position=position-MAX_DIGITS;
	int n = position * 4;
    if (segments[digit][0])
        digits[0][n + 1] = '_';
    if (segments[digit][1])
        digits[1][n + 2] = '|';
    if (segments[digit][2])
        digits[2][n + 2] = '|';
    if (segments[digit][3])
        digits[2][n + 1] = '_';
    if (segments[digit][4])
        digits[2][n] = '|';
    if (segments[digit][5])
        digits[1][n] = '|';
    if (segments[digit][6])
        digits[1][n + 1] = '_';
}

void print_digits_array(void) 
{
    int i, j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < MAX_DIGITS * 4; j++) 
        {
            printf("\033[40;31m%c\033[0m",digits[i][j]);    //输出红色字体 
        }
        printf("\n");
    }
}
