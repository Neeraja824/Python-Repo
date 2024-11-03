import java.util.Scanner;
public class even{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int x[]=new int[n];
        for(int i=0;i<n;i++){
            x[i]=sc.nextInt();
        }
        int c=0;
        for(int i=0;i<n;i++){
            if(x[i]%2==0){
                c++;
            }
        }
        if(c==n){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    }
}