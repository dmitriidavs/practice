#include <stdio.h>
#include <stdlib.h>


/* BASICS */
int main()
{
    /*
    char characterName[] = "John";
    int characterAge = 23;
    float characterScore = 9.59;
    char characterGrade = 'A';

    printf("Hello world!\n");
    printf("It's %s here\n", characterName);
    printf("He is %d years old\n", characterAge);
    printf("His AVG score is %f, which is equivalent to %c\n", characterScore, characterGrade);
    characterAge = 50;
    printf("But he feels as if he was %d years old", characterAge);
    */

    /* CONSTANTS */
    /*
    const int NUM = 5;
    printf("I've chosen number %d\n", NUM);
    NUM = NUM + 5;
    printf("Num + 5 would be: %d", NUM);
    */

    /* INPUT */
    /* int age;
    printf("Enter your age: "); */
    /* user inputs val to var age (& - pointer to store val) */
    /* scanf("%d", &age);
    printf("You are %d years old", age); */


    /* Allocates memory for 20 chars in name */
    /*
    const int maxChars = 20;
    char name[maxChars];
    printf("Enter your name: ");
    */
    /* scanf grabs everything before the first space */
    /* fgets gets the whole line from stdin (standard input) */
    /*
    fgets(name, maxChars, stdin);
    printf("Your name is %s", name);
    */


    /* CALCULATOR */
    /*
    float num1;
    float num2;
    printf("Enter first number: ");
    scanf("%f", &num1);
    printf("Enter second number: ");
    scanf("%f", &num2);

    printf("Answer: %f", num1 + num2);
    */


    /* MADLIBS */
    char way[10];
    char verbInitForm[15];
    char actionNoun[15];
    char actionAdj[15];

    printf("Enter the way pointer: ");
    scanf("%s", way);
    printf("Enter verb in initial form: ");
    scanf("%s", verbInitForm);
    printf("Enter a verb for action ending with -ing and a noun describing it: ");
    scanf("%s%s", actionNoun, actionAdj);

    printf("I've had it %s to my neck\n", way);
    printf("What did the giraffe say when her neighbor wouldn't stop %s?\n", verbInitForm);
    printf("You're %s me %s!", actionNoun, actionAdj);

    return 0;
}
