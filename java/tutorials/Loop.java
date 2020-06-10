package tutorials;

public class Loop {
    public static void main(String[] args){
        char[] vowals = {'a', 'e', 'i', 'o', 'u'};

        for (int i=0; i < vowals.length; ++i){
            System.out.print(vowals[i]);
        }
        System.out.println();
        for (char c : vowals){
            System.out.print(c);
        }
    }
}