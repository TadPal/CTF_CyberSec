#include <stdio.h>>

int main(void)
{
    char entered_string[84];
    int x;
    uint sum_of_chars_modulo_nine;
    int i;

    //   setbuf(stdout,NULL);
    //   setbuf(stdin,NULL);

    //   flag = getenv("FLAG");

    //   setgroups(0,NULL);
    //   setgid(0x539);
    //   setuid(0x539);

    for (i = 0; i < 80; i++)
    {
        entered_string[i] = '\0';
    }

    //   puts("xxx");
    //   printf("xxx"); //print text

    scanf("%[^\n]s", entered_string); // read stirng until new line

    //   printf("xxx",entered_string); //print text
    //   puts("xxx");

    sum_of_chars_modulo_nine = 0;
    for (x = 0; x < 80; x++)
    {
        sum_of_chars_modulo_nine = (sum_of_chars_modulo_nine + (int)entered_string[x]) % 9;
        // putchar("."); // prints line of dots
        // FUN_00401160(10000); //sleep for a while
    }
    // puts("\nA je to!");
    printf("xxx", *(undefined8 *)(prezdivky + (ulong)sum_of_chars_modulo_nine * 8)); // This gets the value on location 00402008 we need 00401256
    // puts("xxx");

    return 0;
}
