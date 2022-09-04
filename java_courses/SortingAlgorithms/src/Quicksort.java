public class Quicksort {
    public static void quickSort(double[] floatArray){
        quickSort(floatArray, 0, floatArray.length - 1);
    }

    private static void quickSort(double[] floatArray, int left, int right){
        if (left < right){
            int pivot = partition(floatArray, left, right);

            if (pivot > 1)
                quickSort(floatArray, left, pivot - 1);
            if (pivot + 1 < right)
                quickSort(floatArray, pivot + 1, right);

        }
    }

    private static int partition(double[] floatArray, int left, int right){
        double pivot = floatArray[left];
        while (true){
            while (floatArray[left] < pivot)
                left++;

            while (floatArray[right] > pivot)
                right--;

            if (left < right){
                if (floatArray[left] == floatArray[right])
                    return right;

                double temp = floatArray[left];
                floatArray[left] = floatArray[right];
                floatArray[right] = temp;
            }
            else
                return right;
        }
    }
}