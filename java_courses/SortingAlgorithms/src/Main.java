import java.lang.Math;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.time.StopWatch;

public class Main {
    public static void main(String[] args) {
        double[] bubbleSort = new double[100000];
        double[] insertionSort = new double[100000];
        double[] mergeSort = new double[100000];
        double[] quickSort = new double[100000];

        for (int i = 0; i < 100000; i++)
            bubbleSort[i] = Math.random();

        for (int i = 0; i < 100000; i++)
            insertionSort[i] = Math.random();

        for (int i = 0; i < 100000; i++)
            mergeSort[i] = Math.random();

        for (int i = 0; i < 100000; i++)
            quickSort[i] = Math.random();

        StopWatch stopWatch = new StopWatch();

        double bubbleTime = - 1, insertionTime = - 1, mergeTime = - 1, quickTime = -1;

        stopWatch.start();
        Bubblesort.bubbleSort(bubbleSort);
        stopWatch.stop();
        bubbleTime = stopWatch.getTime(TimeUnit.MILLISECONDS);
        stopWatch.reset();
        System.out.println("Bubblesort Done!");

        stopWatch.start();
        Insertionsort.insertionSort(insertionSort);
        stopWatch.stop();
        insertionTime = stopWatch.getTime(TimeUnit.MILLISECONDS);
        stopWatch.reset();
        System.out.println("Insertionsort Done!");

        stopWatch.start();
        Mergesort.mergeSort(mergeSort);
        stopWatch.stop();
        mergeTime = stopWatch.getTime(TimeUnit.MICROSECONDS);
        stopWatch.reset();
        System.out.println("Mergesort Done!");

        stopWatch.start();
        Quicksort.quickSort(quickSort);
        stopWatch.stop();
        quickTime = stopWatch.getTime(TimeUnit.MICROSECONDS);
        stopWatch.reset();
        System.out.println("Quicksort Done!");

        System.out.println("Bubblesort: " + bubbleTime + " milliseconds");
        System.out.println("Insertionsort: " + insertionTime + " milliseconds");
        System.out.println("Mergesort: " + mergeTime + " microseconds");
        System.out.println("Quicksort: " + quickTime + " microseconds");
    }
}