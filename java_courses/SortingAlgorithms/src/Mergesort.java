public class Mergesort {
    public static void mergeSort(double[] input, int low, int high){
        if (low < high){
            int middle = (low / 2) + (high / 2);

            mergeSort(input, low, middle);
            mergeSort(input, middle + 1, high);
            merge(input, low, middle, high);
        }
    }

    public static void mergeSort(double[] input){
        mergeSort(input, 0, input.length - 1);
    }

    private static void merge(double[] input, int low, int middle, int high){
        int left = low;
        int right = middle + 1;
        double[] tmp = new double[(high - low) + 1];
        int tmpIndex = 0;

        while ((left <= middle) && (right <= high)){
            if (input[left] < input[right]){
                tmp[tmpIndex] = input[left];
                left = left + 1;
            }
            else{
                tmp[tmpIndex] = input[right];
                right = right + 1;
            }
            tmpIndex = tmpIndex + 1;
        }

        if (left <= middle){
            while (left <= middle){
                tmp[tmpIndex] = input[left];
                left = left + 1;
                tmpIndex = tmpIndex + 1;
            }
        }

        if (right <= high){
            while (right <= high){
                tmp[tmpIndex] = input[right];
                right = right + 1;
                tmpIndex = tmpIndex + 1;
            }
        }

        for (int i = 0; i < tmp.length; i++)
            input[low + i] = tmp[i];
    }
}