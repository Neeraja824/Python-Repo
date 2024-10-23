import java.util.Scanner;
public class Min{
    public static int m(int x,int y){
        int a=x/y;
        int b=x%y;
        return a+b;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int x=sc.nextInt();
            int y=sc.nextInt();
            System.out.println(m(x,y));
        }
    }
}