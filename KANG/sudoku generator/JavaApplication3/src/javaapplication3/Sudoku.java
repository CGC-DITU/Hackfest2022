package javaapplication3;


/* This code has a simple logic
    firstly create a sudoku and then remove any random X elements from the formed sudoku
    so to form a sudoku we will firstly fill in the diagonal blcoks cause they wont interfere in each others' rows and columns
    nextly we will fill in the remaining elements row wise
    at the end we will remove any random K elements at random Locations
*/


public class Sudoku{
    int mat[][];
    int N=9;         // this is the size of the whole matrix
    int sqrtN;      // this is used to denote the size of the block
    
    Sudoku(){
        Double sN = Math.sqrt(N);
        sqrtN = sN.intValue();
        
        mat = new int[N][N];
    }
    
    void create(){
        fillDiagonal();
        fillRemaining(0,sqrtN);
    }
    
    void fillDiagonal(){
        for(int i=0;i<N;i=i+sqrtN)
            fillBox(i,i);
    }
    
    void fillBox(int row,int col){
        int num;
        for(int i=0;i<sqrtN;i++){
            for(int j=0;j<sqrtN;j++){
                do{
                    num=randomNumberGenerator(N);
                }while(!UsedInTheBox(row,col,num));
                mat[row+i][col+j] = num;
            }
        }
    }
    
    boolean UsedInTheBox(int row,int col,int x){
        for(int i=0;i<sqrtN;i++){
            for(int j=0;j<sqrtN;j++)
                if(mat[row+i][col+j]==x)
                    return false;
        }
        return true;
    }
    
    
    
    boolean CheckIfSafe(int i,int j,int num)
    {
        return (unUsedInRow(i, num) &&
                unUsedInCol(j, num) &&
                UsedInTheBox(i-i%sqrtN, j-j%sqrtN, num));
    }
    
    boolean unUsedInRow(int i,int num)
    {
        for (int j = 0; j<N; j++)
           if (mat[i][j] == num)
                return false;
        return true;
    }
 

    boolean unUsedInCol(int j,int num)
    {
        for (int i = 0; i<N; i++)
            if (mat[i][j] == num)
                return false;
        return true;
    }
 
    boolean fillRemaining(int i, int j)
    {
        if (j>=N && i<N-1)
        {
            i = i + 1;
            j = 0;
        }
        if (i>=N && j>=N)
            return true;
 
        if (i < sqrtN)
        {
            if (j < sqrtN)
                j = sqrtN;
        }
        else if (i < N-sqrtN)
        {
            if (j==(int)(i/sqrtN)*sqrtN)
                j =  j + sqrtN;
        }
        else
        {
            if (j == N-sqrtN)
            {
                i = i + 1;
                j = 0;
                if (i>=N)
                    return true;
            }
        }
 
        for (int num = 1; num<=N; num++)
        {
            if (CheckIfSafe(i, j, num))
            {
                mat[i][j] = num;
                if (fillRemaining(i, j+1))
                    return true;
 
                mat[i][j] = 0;
            }
        }
        return false;
    }
    
    int randomNumberGenerator(int num){
        return (int) Math.floor((Math.random()*num+1));
    }
    
    void remove(int x){
        int count = x;
        while(count!=0){
            int cell = randomNumberGenerator(N*N)-1;
            int i=cell/9;
            int j = cell%9;
            if(j!=0)
                j=j-1;
            if(mat[i][j]!=0)
            {
                mat[i][j]=0;
                count--;
            }
        }
    }
    
    void print(){
        for(int i=0;i<this.N;i++){
            for(int j=0;j<this.N;j++){
                System.out.print(mat[i][j]+" ");
            }
            System.out.print("\n");
        }
    }
    public static void main(String args[]){
        Sudoku s = new Sudoku();
        s.create(); 
       s.remove(s.randomNumberGenerator(80));
        s.print();
    }
}