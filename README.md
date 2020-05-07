# Best Strategies in repeated oneVmany games: Dead by Daylight


## Abstract



## Running the code

_**The ASL recognition class**_



```
model = ASLRecognition()
```





_**Training the Model**_


This starts a video frame that waits for a command:
                
       - Esc: cancel prediction
       - s: take static image for (a-y) prediction not including J
       - d: take recording until d hit again, captures dynamic sign and predicts either J or Z
