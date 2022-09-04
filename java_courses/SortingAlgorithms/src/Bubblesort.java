public class Bubblesort {
    public static void bubbleSort(double[] floatArray){
        for (int i = floatArray.length - 1; i > 0; i--){
            for (int j = 0; j <= i - 1; j++){
                if (floatArray[j] > floatArray[j + 1]){
                    double highValue = floatArray[j];
                    floatArray[j] = floatArray[j + 1];
                    floatArray[j + 1] = highValue;
                }
            }
        }
    }
}
