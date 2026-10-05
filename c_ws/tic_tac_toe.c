#include <stdio.h> 
int find_line(int board[3][3])
{
    //char line;
    int winner = 0;
    for(int i = 0; i < 3;i++ ){
        if(board[0][i] == board[1][i] && board[0][i] == board[2][i] && (board[0][i] == 1 || board[0][i] == 2)){
            winner = board[0][i];
            break;
        }
    }
    for(int i = 0; i < 3;i++ ){
        if(board[i][0] == board[i][1] && board[i][0] == board[i][2] && (board[i][0] == 1 || board[i][0] == 2)){
            winner = board[i][0];
            break;
        }
    }
    if(board[0][0] == board[1][1] && board[0][0] == board[2][2] && (board[0][0] == 1 || board[0][0] == 2)){
        winner = board[0][0];
    }
    if(board[0][2] == board[1][1] && board[0][2] == board[2][0] && (board[0][2] == 1 || board[0][2] == 2)){
    winner = board[0][2];
    }
    return winner;
}
void show_board(int board[3][3])
{
    printf("   A B C\n");
    for(int j = 0;j<3;j++)
    { 
        printf("%d∥",j+1);
        for(int i = 0;i<3;i++)
        {
            if (board[j][i] == 1){
                printf("O");
            }else if(board[j][i] == 2){
                printf("X");
            }else{
                printf(" ");
            }
            printf("|");
        }
        printf("\n");
    }

}
int main(void)
{   
    int winner;
    char col;
    int row;
    int board[3][3] = {{0,0,0},
                       {0,0,0},
                       {0,0,0}};
    while(1){
        show_board(board);
        printf("please select box ex)A2\n");
        while(1){
            scanf("%c%d",&col,&row);
            if(board[row-1][col-'A'] == 0 && 0 <= row-1 && row-1 <=2 && 0<= col-'A' && col-'A'<=2){
                board[row-1][col-'A'] = 1;
                break;
            }else{
                printf("you can't choose there!%d,%d,%d,%d,%d\n",board[row-1][col-'A'] == 0 , 0 <= row-1 , row-1 <=2 , 0<= col-'A' , col-'A'<=2);
            }
            
        }
        // scanf("%c%d",&col,&row);
        // board[row-1][col-'A'] = 1;
        winner = find_line(board);
        if (winner)
        {   
            show_board(board);
            printf("player %d win!\n",winner);
            break;
        }
    }
    return 0;
}