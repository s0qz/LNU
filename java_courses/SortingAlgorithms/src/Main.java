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

        double bubbleTime, insertionTime, mergeTime, quickTime;

        stopWatch.start();
        Bubblesort.bubbleSort(bubbleSort);
        stopWatch.stop();
        bubbleTime = stopWatch.getTime(TimeUnit.MILLISECONDS);
        stopWatch.reset();
        System.out.println("Bubble sort Done!");

        stopWatch.start();
        Insertionsort.insertionSort(insertionSort);
        stopWatch.stop();
        insertionTime = stopWatch.getTime(TimeUnit.MILLISECONDS);
        stopWatch.reset();
        System.out.println("Insertion sort Done!");

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

        System.out.println("Bubble sort: " + bubbleTime + " milliseconds");
        System.out.println("Insertion sort: " + insertionTime + " milliseconds");
        System.out.println("Mergesort: " + mergeTime + " microseconds");
        System.out.println("Quicksort: " + quickTime + " microseconds");
    }
}
