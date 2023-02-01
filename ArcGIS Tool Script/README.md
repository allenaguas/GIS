ArcGIS: Tool Script

Background:
Our company had an influx of new ArcGIS users (little to no GIS experience) which resulted a need to train all individuals on how to use the interface to produce maps of the area of interest they wanted. The amount of time to train these individals has resulted in a loss of productivity and deffered other important tasks.
 

The Solution:
The Tool Script allows users with little to no expericence to select the area they want printed by simplifiying the steps needed for the user.

How to set up script tool:
1) Right click Toolboxes in Catalog and create "New Toolbox(.atbx)" (Skip this step if you already have a (.atbx) toolbox you want to use)

![image](https://user-images.githubusercontent.com/79226456/215905039-bc0444f4-3ae2-4a6e-8d19-cec9be98a5c0.png)

2) Right click Toolbox, add new script tool.

![image](https://user-images.githubusercontent.com/79226456/215905372-72f8d2ca-724e-4498-8b45-566e4e40d05b.png)

3) Find script tool and open "Properties" (right click and open)

![image](https://user-images.githubusercontent.com/79226456/215906189-fc154fcc-7256-4615-aadc-fba03d8541ac.png)

4) Add Python script and alter parameters.

Clear "Execution" and paste Python script within. You can also open and alter the script in a script editor if needed.  

![image](https://user-images.githubusercontent.com/79226456/216122229-6469ab64-0d94-4d49-8a0d-7acf966e4017.png)

In "Parameters" we will need to create an output folder for where to save our PDF map(s). It is important to note that the parameters in the script (Ex: Output_Folder = arcpy.GetParameterAsText(0)) need to match the naming convention in the "Parameters" Name as well. By default both the script and "Parameters" name has already set to "Output_Folder".

![image](https://user-images.githubusercontent.com/79226456/216123115-5f8355ce-345c-46c9-9a12-8533714337fa.png)








How to run script tool:
1) Click on area of interest ("Select by" tool ).

![image](https://user-images.githubusercontent.com/79226456/215903252-f41f0d24-6f23-4719-8f38-d786e70e2172.png)


