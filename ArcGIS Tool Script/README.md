ArcGIS: Tool Script

Background:
Our company had an influx of new ArcGIS users and there was a need to train all the individuals coming in  and out.
The Tool Script allows users with 

The Solution:
This script filters out records of areas that are not in our territoy, then proceeds to print the map series once done.

How does the script work?
1) User needs to select location (area of interest) manually before running script. "Select by Attribute": Once interest of area is selected, the script will select all records that you do NOT want and do an inverse selection. Esentaially selecting all the other areas you wish to proceed with.

![image](https://user-images.githubusercontent.com/79226456/188936960-2c9865c9-f691-463a-955d-002eb9ccef70.png)
 

2) "Copy Features": Selected features will be copied to new layer

![image](https://user-images.githubusercontent.com/79226456/188942793-dc7f7191-be70-4bd8-a629-1a8f6e068f66.png)


3) Last process is printing the map series into a PDF

