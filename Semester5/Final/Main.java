public class Main {
    public static void main(String[] args) {
        int[] b = {2, 3, 1, 4, 5, 2};
        int k = 10;

        // Selection Sort
        for (int i = 0; i < b.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < b.length; j++) {
                if (b[j] < b[minIndex]) {
                    minIndex = j;
                }
            }
            // Menukar elemen
            int temp = b[i];
            b[i] = b[minIndex];
            b[minIndex] = temp;
        }

        // Penjumlahan elemen dengan batas k
        int t = 0;
        for (int i = 0; i < b.length; i++) {
            if (t + b[i] <= k) {
                t += b[i];
            } else {
                break;
            }
        }

        // Output hasil
        System.out.println("Total: " + t);
    }
}
