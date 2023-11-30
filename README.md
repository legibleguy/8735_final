# Final Project for the Unsupervised Learning class

For now, all this code is just data processing to get it all prepared for the actual implementation.

Before running anything, unzip FPS Video Games.csv.zip. This was archived just to surpass GitHub's 100Mb limit.

This comes with two csv files that you would typically generate with the provided scipts. Unfortunately, some of the hardware o the list is not sold on Neweggs anymore so cpu_prices and gpu_prices might have missing prices. Example csv's attached here have those gaps filled out.

What each script does:

* list_games.py - just prints all the game names that you can punch into get_cost_per_frame.py
* get_prices.py - will go through all the GPUs and CPUs in the reference database and gets their prices on Newegg. Generates two new files: cpu_prices.csv and gpu_pricea.csv
* get_cost_per_frame.py - generates the cost per frame database based on gpu_prices.csv and cpu_prices.csv. Generates cost_per_frame_{GAME_NAME}.csv

Original proposal:

Choosing hardware for a new computer build often involves considering its ability to run modern games. These games, while entertaining, also stress test machines with complex geometry, materials, lighting effects, and other calculations in real time.
Solution
We propose a system that ranks computer specifications using the FPS in Video Games dataset from OpenML. FPS, Frames per Second, reflects the smoothness of a game and thus, performance.
We will also calculate a Cost per Frame value, derived from average FPS divided by the hardware cost. This is key in our solution as it helps determine value for money. For example, if two setups have similar FPS but differing costs per frame, the cheaper one might be the better deal.
We will categorize PC builds into four groups: Cheap with Bad Performance, Cheap with Good Performance, Expensive with Bad Performance, and Expensive with Good Performance.
Dataset
This dataset has FPS (Frames Per Second) data from video games played on computers. Each row tells you the FPS for a game on a specific computer. The type of CPU and GPU in the computer is also included.
Work Distribution
Andy: Prepare dataset for Daniel's clustering algorithm, calculate cost per frame
Daniel: Implement and evaluate fuzzy c means and probabilistic c means clustering algorithms using iVAT and silhouette coefficient
Both of us will be working on the presentation and the final report
Timeline
11/19 have the dataset prepared for the clustering problem
11/26 have both fuzzy c means and probabilistic c means implemented
11/29 have both iVAT and silhouette coefficient implemented
12/3 have the presentation finished
12/10 have the final report finished
