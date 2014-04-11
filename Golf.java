package edu.berkeley.ischool.aep;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by honestyhuang on 4/4/14.
 */
public class Golf {

    private List<Integer> inputArray;
    private final int MAX_MEMBERS_IN_GROUP = 4;

    public Golf(Integer[] inputArray) {
        this.inputArray = new ArrayList<Integer>(Arrays.asList(inputArray));
    }

    public int getNumberOfGroups(){
        //return 3;
        int ret_val =0;
        Integer sum =0;
        int counter =0;

        //added this new condition for base case.
        if(inputArray.size() == 1 && inputArray.get(0) <= 4) return 1;

        while(inputArray.size() > 0 && counter < inputArray.size()){
            sum += inputArray.get(counter);
            if(sum == MAX_MEMBERS_IN_GROUP){
                ret_val ++;
                sum =0;
                inputArray.remove(counter);
//                counter++;
            }
            else if(sum > MAX_MEMBERS_IN_GROUP){
                sum -= inputArray.get(counter);
                counter++;
            }
            else {
                if(counter == inputArray.size()-1) ret_val +=1;
                inputArray.remove(counter);
                counter = 0;
            }

        }
        if(sum > 0) ret_val ++;
        return ret_val;


    }

}