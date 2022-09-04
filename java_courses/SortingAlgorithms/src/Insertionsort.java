public class Insertionsort {
    public static void insertionSort(double[] floatArray){
        int i, n;
        int length = floatArray.length;
        double temp;

        if (length < 2)
            return;

        for (n = 1; n < length; n++){
            temp = floatArray[n];
            i = n - 1;

            while (i >= 0 && floatArray[i] > temp){
                floatArray[i + 1] = floatArray[i];
                i--;
            }

            floatArray[i + 1] = temp;
        }
    }
}