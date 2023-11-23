import java.util.Random;
import java.util.Scanner;

public class test {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random rastgele = new Random();

        int[] hedefDegerler = {rastgele.nextInt(50) + 1, rastgele.nextInt(50) + 1, rastgele.nextInt(50) + 1};

        System.out.println("Hedef Değerler: " + hedefDegerler[0] + ", " + hedefDegerler[1] + ", " + hedefDegerler[2]);

        while (true) {
            try {
                System.out.print("Sayı tahmininizi girin: ");
                int tahmin1 = scanner.nextInt();

                if (tahmin1 == hedefDegerler[0] || tahmin1 == hedefDegerler[1] || tahmin1== hedefDegerler[2]) {
                    System.out.println("Tebrikler! Tahmin ettiniz.");
                    break;
                } else {
                    System.out.println("Maalesef, doğru tahminde bulunamadınız. Tekrar deneyin.");
                }
            } catch (java.util.InputMismatchException e) {
                System.out.println("Lütfen geçerli bir sayı girin.");
                scanner.next(); // Buffer'ı temizle
            }
        }

        scanner.close();
    }
}
