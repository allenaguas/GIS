ArcGIS: Layer to Print to Pdf

Background:
Our company provides utility maps to clients for requested regions. One dilemma many mappers had encountered is the time wasted trying to filter out maps that had no data. The simplest solution was to print all maps and deliver to our clientielle. The issues was the confusion of what maps were being charged, since we charge on a per map basis another possible solution was to label what maps were not tobe charged by editing the PDFs with a  "No Charge" text. This can be seriously time consuming when particular clients request vasts amounts of maps.

The Solution:
This script filters out records of areas that are not in our territoy, then proceeds to print the map series once done.

How does the script work?
1) User needs to select location (area of interest) manually before running script. "Select by Attribute": Once interest of area is selected, the script will select all records that you do NOT want and do an inverse selection. Esentaially selecting all the other areas you wish to proceed with.

![image](https://user-images.githubusercontent.com/79226456/188936960-2c9865c9-f691-463a-955d-002eb9ccef70.png)
 

2) "Copy Features": Selected features will be copied to new layer

![image](https://user-images.githubusercontent.com/79226456/188942793-dc7f7191-be70-4bd8-a629-1a8f6e068f66.png)


3) Last process is printing the map series into a PDF

