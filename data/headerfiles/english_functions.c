//Include header files
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

const int BUCKETS = 500;
const int LENGTH = 45;
const int DEFINITION = 1000;

typedef struct node{
    char word[46];
    char meaning[1000];
    struct node *next;
}node;

//hash table
node *hash_table[500];

//function prototypes
unsigned int hash(char *word);
void set_table2null();
bool load_words();
node *create_node();
bool insert_node(node *s);
void print_table();
bool find_word(char *s);

unsigned int hash(char *word){
    unsigned long int hash_value = 65579;
    for (int i = 0; i < strlen(word); i++){
        hash_value = hash_value * (33 * 33 * toupper(word[i]));
    }
    return hash_value % BUCKETS;
}


bool load_words(){

    //set table values to null
    char string_read[LENGTH +1];
    FILE *file = fopen("english-words.txt", "r");
    if (file == NULL){
        printf("Error: Unable to load file.\n");
        return false;
    }


    while(fscanf(file, "%s", string_read) != EOF){
        node *temporary = create_node();
        strcpy(temporary->word, string_read);

        if (!insert_node(temporary))
        {
            return false;
        }
    }
    fclose(file);
    print_table();
    return true;
    
}

void set_table2null(){
    for (int i =0; i < BUCKETS; i++){
        hash_table[i] = NULL;
    }
}

node *create_node(){
    //Allocate memory for temporary node
    node *tmp = malloc(sizeof(node));

    //if NULL, return null
    if (tmp == NULL){
        return NULL;
    }

    tmp->next = NULL;
    return tmp;
}

bool insert_node(node *s){
    if (s == NULL){
        return false;
    }

    int index = hash(s->word);

    //insert node into the table
    s->next = hash_table[index];
    hash_table[index] = s;
    return true;
}

void print_table(){
    
    for (int i =0; i < BUCKETS; i ++)
    {
        printf("%i\n", i);
        node *tmp = hash_table[i];
        while(tmp != NULL){
            printf ("%s ->", tmp->word);
            tmp = tmp->next;

        }
    }
}

void free_memory(){
    for (int i = 0; i < BUCKETS; i++){
        node*head = hash_table[i];

        while(head != NULL){
            node *tmp = head->next;
            free(head);
            head = tmp;
        }
    }
}

bool find_word(char *s){
    for (int i = 0; i < BUCKETS; i ++){

        node *head = hash_table[hash(s)];
        while (head != NULL){
            node *tmp = head->next;
            if (tmp-> word == s){
                return true;
                break;
            }
        }
    }

    return false;
}

int main(void){
    load_words();
    char *s = "brain";
    if (find_word(s)){
        printf("Found");
    }
}
